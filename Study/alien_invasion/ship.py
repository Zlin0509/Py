import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        # 初始化
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取外界矩形
        self.image = pygame.image.load('images/002.jpg')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # 将每个飞船放在屏幕中间底部
        self.rect.midbottom = self.screen_rect.midbottom

        # 用一个浮点树x来储存rext的位置
        self.x = float(self.rect.x)

        # 移动判断
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据输入来更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # 根据self.x来更新self.rect.x
        self.rect.x = self.x

    def blitme(self):
        # 绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船重新放在最中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)