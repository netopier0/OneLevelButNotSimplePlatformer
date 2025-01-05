import pygame
import json

class World:
    def __init__(self):
        self.currLevel = "1"
        self.colliders = []
        self.movingColl = []
        self.moves = []
        self.movingConst = [] #[(direction, d, min, min), currD]
        self.buttons = []
        self.exits = []
        self.jumpPads = []
        self.extraJump = []
        
        self.conditionalMovingCollider = []

        self.pressedButtons = set()
        self.display_surface = pygame.display.get_surface()

    def reloadCollider(self):
        self.colliders = []
        
        with open('levelData.json', 'r') as file:
            data = json.load(file)[self.currLevel][0]

        for val in data["walls"][0].values():
            if len(val) == 4 or (all([x in self.pressedButtons for x in val[5].split(",")]) and val[4] == "True") or (not all([x in self.pressedButtons for x in val[5].split(",")]) and val[4] == "False"):
                    self.colliders.append(pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])))

    def drawWorld(self):
        for coll in self.buttons:
            pygame.draw.rect(self.display_surface, (0,0,255), coll[0])

        for coll in self.exits:
            pygame.draw.rect(self.display_surface, (0,255,255), coll[0])

        for coll in self.movingColl:
            pygame.draw.rect(self.display_surface, (255,0,0), coll)

        for coll in self.jumpPads:
            pygame.draw.rect(self.display_surface, (255,0,255), coll)
            
        for coll in self.extraJump:
            pygame.draw.rect(self.display_surface, (127,127,127), coll)

        for coll in self.colliders:
            pygame.draw.rect(self.display_surface, (0,255,0), coll)

    def loadWorldFromFile(self, level):
        '''
        self.colliders.append(pygame.Rect(200, 250, 25, 25))
        self.colliders.append(pygame.Rect(100, 200, 25, 25))
        self.colliders.append(pygame.Rect(0, 300, 600, 10))
        '''
        self.currLevel = level
        self.colliders = []
        self.buttons = []
        self.exits = []
        self.movingColl = []
        self.moves = []
        self.movingConst = []
        self.jumpPads = []
        self.extraJump = []
        self.conditionalCollider = []
        self.conditionalMovingCollider = []

        with open('levelData.json', 'r') as file:
            data = json.load(file)[level][0]
            #print(data)
        for val in data["walls"][0].values():
            if len(val) == 4 or (all([x in self.pressedButtons for x in val[5].split(",")]) and val[4] == "True") or (not all([x in self.pressedButtons for x in val[5].split(",")]) and val[4] == "False"):
                    self.colliders.append(pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])))
        if "buttons" in data:
            for val in data["buttons"][0].values():
                self.buttons.append([pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])), val[4]])
        if "exits" in data:
            for val in data["exits"][0].values():
                self.exits.append([pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])), val[4]])
        if "wallsMove" in data:
            for val in data["wallsMove"][0].values():
                self.movingColl.append(pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])))
                self.movingConst.append([(val[4], int(val[5]), int(val[6]), int(val[7])), int(val[8])])
                self.moves.append([0, 0])
                if len(val) == 10:
                    self.conditionalMovingCollider.append(val[9])
                else:
                    self.conditionalMovingCollider.append("")
        if "jumpPad" in data:
            for val in data["jumpPad"][0].values():
                self.jumpPads.append(pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])))
        if "extraJump" in data:
            for val in data["extraJump"][0].values():
                self.extraJump.append(pygame.Rect(int(val[0]), int(val[1]), int(val[2]), int(val[3])))
    


    def move(self, delta):
        for i in range(len(self.movingConst)):
            if self.conditionalMovingCollider[i] != "" and self.conditionalMovingCollider[i] not in self.pressedButtons:
                self.moves[i] = [0, 0]
                continue
            self.moves[i] = [self.movingColl[i].x, self.movingColl[i].y]
            moveC = self.movingConst[i][0]
            if moveC[0] == "X":
                self.movingColl[i].x += self.movingConst[i][1] * round(moveC[1] * delta)
                self.movingColl[i].x = max(self.movingColl[i].x, moveC[2])
                self.movingColl[i].x = min(self.movingColl[i].x, moveC[3])
                if self.movingColl[i].x in [moveC[2], moveC[3]]:
                    self.movingConst[i][1] *= -1
            elif moveC[0] == "Y":
                self.movingColl[i].y += self.movingConst[i][1] * round(moveC[1] * delta)
                self.movingColl[i].y = max(self.movingColl[i].y, moveC[2])
                self.movingColl[i].y = min(self.movingColl[i].y, moveC[3])
                if self.movingColl[i].y in [moveC[2], moveC[3]]:
                    self.movingConst[i][1] *= -1
            self.moves[i][0] = (self.movingColl[i].x - self.moves[i][0])/delta
            self.moves[i][1] = (self.movingColl[i].y - self.moves[i][1])/delta


    def getColliders(self):
        return self.colliders + self.movingColl
