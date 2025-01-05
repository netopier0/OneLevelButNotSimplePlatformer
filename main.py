from sys import exit as End
import pygame
from player import Player
from world import World
from puzzle import Puzzle

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((600, 600))
        self.running = True
        self.clock = pygame.time.Clock()        
        self.world = World()
        self.puzzle = Puzzle(self.world)
        self.game = True #Todo edit
        self.player = Player(40,450,16,16,self.world,self.puzzle)

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
                if event.type == pygame.KEYDOWN and False:
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
                    if event.key == 109:
                        self.game = False
                    elif event.key == 110:
                        self.game = True
                if event.type == pygame.MOUSEBUTTONUP and not self.game:
                    self.puzzle.clickPos(pygame.mouse.get_pos())

            self.display_surface.fill((255,255,255))
            #pygame.draw.rect(self.display_surface, (255,0,0), self.player.rect)
            if self.game:
                self.world.move(deltaTime)
                self.world.drawWorld()
                self.player.update(deltaTime)
            else:
                self.display_surface.fill((200,200,255))
                self.puzzle.drawPuzzle()

            pygame.display.update()
            

        print("Exit")
        pygame.quit()
        End()

if __name__ == '__main__':
    game = Game()
    game.run()
