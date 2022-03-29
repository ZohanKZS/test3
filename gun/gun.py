import pygame

class gun():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load('img/pixil-frame-0.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom-50

    def output(self):
        self.screen.blit(self.image,self.rect)

    def upd(self):
        self.rect.x+=5
        if self.rect.x>1200:
            self.rect.x=0


