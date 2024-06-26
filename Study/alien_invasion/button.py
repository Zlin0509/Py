import pygame.font

class Button:
    """为游戏创建按钮的类"""

    def __init__(self, ai_game, msg):
        """初始化按钮属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 设置按钮的其他属性
        self.width, self.heigth = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect并居中
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像,并放在按钮上方"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮并填充文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)