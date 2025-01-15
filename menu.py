import pygame
from os.path import join

class Menu:
    def __init__(self, game):
        self.myGame = game
        self.image = pygame.image.load(join('assets', 'menu.png'))
        self.startBut = pygame.rect.Rect(200, 124, 200, 50)
        self.quitBut = pygame.rect.Rect(200, 199, 200, 50)
        self.display_surface = pygame.display.get_surface()

    def drawMenu(self):
        self.display_surface.blit(self.image, (0,0))
            
    def clickPos(self, pos):
        if self.startBut.collidepoint(pos):
            self.myGame.currScreen = 1
        if self.quitBut.collidepoint(pos):
            self.myGame.running = False
