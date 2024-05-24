import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射子弹的类"""

    def __init__(self, ai_game):
        """在当前飞船位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0，0）先创建一个子弹矩形，然后放在真确位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_heigth)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 储存子弹位置,用浮点数，方便改变速度
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新位置
        self.y -= self.settings.bullet_speed
        # 更新矩形位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)