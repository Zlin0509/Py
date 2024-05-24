import sys
import pygame
from time import sleep

from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBroad

class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, 
            self.settings.screen_heighth)
            )
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用来储存游戏统计信息的实例
        self.stats = GameStats(self)
        self.sb = ScoreBroad(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 设置背景色
        self.bg_color = (230, 230, 230)

        self.game_active = False
        # 创建play按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_alien()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # 听取键盘和鼠标输入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家按下按钮后开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 重置游戏的统计信息
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的外星人舰队，把飞船放在屏幕中间底部
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏光标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """相应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """相应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _create_fleet(self):
        """创建一个外星人舰队"""
        # 创建单个外星人并加入aliens群组
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width, alien_heigth = alien.rect.size
        current_x, current_y = alien_width, alien_heigth
        while current_y < (self.settings.screen_heighth - 3 * alien_heigth):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 填满一行后，重置current_x，并递增current_y
            current_x = alien_width
            current_y += alien_heigth * 2

    def _create_alien(self, x_position, y_position):
        """创建一个外星人并让在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        # new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """处理到达边界的外星人"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """将舰队向下移动，并改变左右移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """创建一个子弹,并加入编组bullets"""
        if len(self.bullets) <= self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """更新子弹位置并删除超出边界的子弹"""
        # 更新位置
        self.bullets.update()
        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """相应子弹和外星人的碰撞"""
        # 检查是否有子弹命中外星人,如果有，删除对应的外星人和子弹
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 通关，更新等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_alien(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检查外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_screen(self):
        """更新屏幕上的图像，切换新屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # 显示得分
        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        # 让最近的绘制屏幕可见
        pygame.display.flip()

    def _ship_hit(self):
        """相应飞船和外星人的碰撞"""
        if self.stats.ships_left > 0:
            # ships_left减1，表示损失一条飞船
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 清空外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            #创建一个新的外新人舰队和飞船
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(1.0)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _chcek_alien_bottom(self):
            """检查是否有外星人到达屏幕底部"""
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= self.settings.screen_heighth:
                    # 当成飞创碰撞处理
                    self._ship_hit()
                    break

if __name__ == '__main__':
    # 创建游戏并运行
    ai = AlienInvasion()
    ai.run_game()
