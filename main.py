from sys import exit as End
import pygame
from player import Player
from world import World
from puzzle import Puzzle
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((600, 600))
        self.running = True
        self.clock = pygame.time.Clock()        
        self.world = World()
        self.puzzle = Puzzle(self.world)
        self.menu = Menu(self)
        self.currScreen = 0 # 0-Menu, 1-levels, 2-puzzle
        self.player = Player(40,450,16,25,self.world,self.puzzle)

    def run(self):
        self.world.loadWorldFromFile("1")
        self.player.collisionBlocks = self.world.colliders
        while self.running:
            deltaTime = self.clock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == 27:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == 114:
                    self.player.rect.x = 300
                    self.player.rect.y = 250
                    self.player.direction = [0, 0]
                if event.type == pygame.KEYDOWN:
                    if event.key == 49:
                        self.world.loadWorldFromFile("1")
                    elif event.key == 50:
                        self.world.loadWorldFromFile("2")
                    elif event.key == 51:
                        self.world.loadWorldFromFile("3")
                    elif event.key == 52:
                        self.world.loadWorldFromFile("4")
                    elif event.key == 53:
                        self.world.loadWorldFromFile("5")
                    elif event.key == 54:
                        self.world.loadWorldFromFile("6")
                    elif event.key == 55:
                        self.world.loadWorldFromFile("7")
                    elif event.key == 56:
                        self.world.loadWorldFromFile("8")
                if event.type == pygame.KEYDOWN:
                    if self.currScreen == 1  and event.key == 109:
                        self.currScreen = 2
                    elif self.currScreen == 2 and event.key == 110:
                        self.currScreen = 1
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.currScreen == 0:
                        self.menu.clickPos(pygame.mouse.get_pos())
                    if self.currScreen == 2:
                        self.puzzle.clickPos(pygame.mouse.get_pos())

            self.display_surface.fill((255,255,255))
            if self.currScreen == 0:
                self.menu.drawMenu()
            elif self.currScreen == 1:
                self.world.move(deltaTime)
                self.world.drawWorld()
                self.player.update(deltaTime)
            elif self.currScreen == 2:
                self.puzzle.drawPuzzle()

            pygame.display.update()
            

        print("Exit")
        pygame.quit()
        End()

if __name__ == '__main__':
    game = Game()
    game.run()
