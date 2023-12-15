import pygame


class Gun:

    def __init__(self, screen):
        """pushka init"""

        self.screen = screen
        self.image = pygame.image.load('push.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.y = float(self.rect.bottom)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """Рисование пушки"""

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 2.5
        if self.mup and self.rect.top > self.screen_rect.top:
            self.y -= 2.5
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.y += 2.5

        self.rect.centerx = self.center
        self.rect.bottom = self.y

    def create_gun(self):
        self.center = self.screen_rect.centerx
