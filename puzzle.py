import pygame
import json
from os.path import join

class Puzzle:
    def __init__(self, world):
        self.currLevel = 1
        self.myWorld = world
        self.field = dict()
        self.images = []

        for i in range(9):
            self.field[i+1] = [pygame.rect.Rect((25+(200*(i%3)), 25+(200*(i//3)), 150, 150)), (i//3, i%3), []]
            if i+1 != 9:
                self.images.append(pygame.image.load(join('assets', str(i+1) + '.png')))

        self.display_surface = pygame.display.get_surface()

        #Load Exits
        with open('levelData.json', 'r') as file:
            data = json.load(file)
            for i in range(1, 9):
                for val in data[str(i)][0]["exits"][0].values():
                    self.field[i][2].append(val[4])

    def drawPuzzle(self):
        self.display_surface.fill((200,200,255))
        for k in self.field.keys():
            if k == 9:
                continue
            if k > self.myWorld.biggestPessed:
                pygame.draw.rect(self.display_surface, (0,0,255), self.field[k][0])
            else:
                self.display_surface.blit(self.images[k-1], self.field[k][0].topleft)
            
    def clickPos(self, pos):
        for k in self.field.keys():
            if k == 9:
                continue
            if self.field[k][0].collidepoint(pos):
                if distTuple(self.field[k][1], self.field[9][1]) == 1:
                    self.swapPos(k, 9)
                break
                
    def swapPos(self, a, b):
        self.field[a][0].x, self.field[b][0].x = self.field[b][0].x, self.field[a][0].x
        self.field[a][0].y, self.field[b][0].y = self.field[b][0].y, self.field[a][0].y
        self.field[a][1], self.field[b][1] = self.field[b][1], self.field[a][1]

    def moving(self, d):
        y, x = self.field[self.currLevel][1]
        if d[0] == "R":
            x += 1
        elif d[0] == "L":
            x -= 1
        elif d[0] == "U":
            y -= 1
        elif d[0] == "D":
            y += 1

        if x < 0 or x > 2 or y < 0 or y > 2:
            return getCoordsByDir(d)

        nextLevel = self.currLevel
        for i in range(1, 9):
            if self.field[i][1] == (y, x):
                nextLevel = i
                break

        rd = reverseDir(d)
        if nextLevel == self.currLevel or rd not in self.field[nextLevel][2] or nextLevel > self.myWorld.biggestPessed:
            return getCoordsByDir(d)

        self.currLevel = nextLevel

        self.myWorld.loadWorldFromFile(str(nextLevel))
        return getCoordsByDir(rd)


def distTuple(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def reverseDir(d):
    if d[0] == "R":
        return "L" + d[1:]
    if d[0] == "L":
        return "R" + d[1:]
    if d[0] == "D":
        return "U" + d[1:]
    if d[0] == "U":
        return "D" + d[1:]

def getCoordsByDir(d):
    if d == "R1":
        return (540, 35)
    if d == "R2":
        return (540, 210)
    if d == "R3":
        return (540, 510)
    if d == "L1":
        return (50, 35)
    if d == "L2":
        return (50, 210)
    if d == "L3":
        return (50, 510)
    if d == "U3":
        return (540, 50)
    if d == "D3":
        return (500, 525)

