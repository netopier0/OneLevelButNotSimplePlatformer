import pygame

class Player:
    def __init__(self, x, y, w, h, world, puzzle):
        self.rect = pygame.rect.Rect((x, y, w, h))
        self.jumpRect = pygame.rect.Rect((x, y+h-1, w, 2))
        self.display_surface = pygame.display.get_surface()
        self.direction = [0, 0]
        self.state = "air"
        self.midAirControl = True
        self.extraJump = True
        self.WPressed = False
        self.onPlatformMove = False
        self.myWorld = world
        self.myPuzzle = puzzle

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if self.WPressed and not keys[pygame.K_w]:
            self.WPressed = False

        if self.state == "air":
            self.direction[1] += 9.81
            if keys[pygame.K_s]:
                self.direction[1] += 30
            if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.extraJump:
                if self.extraJumpCheck() and not self.WPressed:
                    self.extraJump = False
                    self.direction[1] = -300

        # No mid air control
        if not self.midAirControl and self.state == "ground":
            self.direction[0] = 0
            self.checkPlatformMove()
            if keys[pygame.K_a]:
                self.direction[0] -= 100

            if keys[pygame.K_d]:
                self.direction[0] += 100


        #Mid air control
        if self.midAirControl:
            self.direction[0] = 0
            self.checkPlatformMove()
            if keys[pygame.K_a]:
                self.direction[0] -= 100

            if keys[pygame.K_d]:
                self.direction[0] += 100

        if self.state == "ground" and (keys[pygame.K_SPACE] or keys[pygame.K_w]):
            if self.jumpPadCheck():
                self.direction[1] = -500
            else:
                self.direction[1] = -300
            self.state = "air"
            self.WPressed = True

        self.direction[1] = min(self.direction[1], 700)
        
        self.rect.x += round((self.direction[0]) * dt)
        self.rect.y += round((self.direction[1]) * dt)
        
        #Walls Screen
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, 600)
        
        if round((self.direction[1]) * dt) != 0 or self.onPlatformMove:
            self.verticalCollision(round((self.direction[1]) * dt), round((self.direction[0]) * dt), dt)
        if round((self.direction[0]) * dt) != 0 or self.onPlatformMove:
            self.horizontalCollision(round((self.direction[0]) * dt), round((self.direction[1]) * dt), dt)

        self.checkCollision()

        #Move jump collider
        self.jumpRect.left = self.rect.left
        self.jumpRect.top = self.rect.bottom-1

        #Check Jump
        self.updateJump()

    def verticalCollision(self, d, d1, dt):
        for block in self.myWorld.colliders:
            if block.colliderect(self):
                if self.rect.left - d1 >= block.right or self.rect.right - d1 <= block.left:
                    continue
                if d < 0:# and (sel\f.rect.top - d > block.bottom) != (self.rect.top > block.bottom):
                    self.rect.top = block.bottom
                    self.direction[1] = 0
                    #print("Ciel")
                elif d > 0:#if (self.rect.bottom - d > block.top) != (self.rect.bottom > block.top):
                    self.rect.bottom = block.top
                    self.direction[1] = 0
                    self.extraJump = True
                    self.state = "ground"
                    #print("Bott")
                    
        for i, block in enumerate(self.myWorld.movingColl):
            if block.colliderect(self):
                md = d - round((self.myWorld.moves[i][1]) * dt)
                md1 = d1 - round((self.myWorld.moves[i][0]) * dt)
                if self.rect.left - md1 >= block.right or self.rect.right - md1 <= block.left or md == 0:
                    continue
                a = abs(self.rect.top - block.bottom + md)
                b = abs(self.rect.bottom - block.top + md)
                if a < b:
                    self.rect.top = block.bottom
                    self.direction[1] = 9.81
                    #print("Ciel")
                else:
                    self.rect.bottom = block.top
                    self.direction[1] = 0
                    self.extraJump = True
                    self.state = "ground"
                    #print("Bott")
        

    def horizontalCollision(self, d, d1, dt):
        for block in self.myWorld.colliders:
            if block.colliderect(self):
                if self.rect.top - d1 >= block.bottom or self.rect.bottom - d1 <= block.top:
                    continue
                #print(self.direction[1])
                if d < 0:# and (self.rect.left - d > block.right):# != (self.rect.left > block.right):
                    self.rect.left = block.right
                    #print("Left")
                    self.direction[0] = 0
                elif d > 0:#if (self.rect.right - d < block.left):# != (self.rect.right > block.left):
                    self.rect.right = block.left
                    #print("Right")
                    self.direction[0] = 0
                    
        for i, block in enumerate(self.myWorld.movingColl):
            if block.colliderect(self):
                md = d - round((self.myWorld.moves[i][0]) * dt)
                md1 = d1 - round((self.myWorld.moves[i][1]) * dt)
                if self.rect.top - d1 >= block.bottom or self.rect.bottom - d1 <= block.top or md == 0:
                    continue
                a = abs(self.rect.left - block.right + md)
                b = abs(self.rect.right - block.left + md)
                if a < b:# and (self.rect.left - d > block.right):# != (self.rect.left > block.right):
                    self.rect.left = block.right
                    #print("Left")
                    self.direction[0] = 0
                else:#if (self.rect.right - d < block.left):# != (self.rect.right > block.left):
                    self.rect.right = block.left
                    #print("Right")
                    self.direction[0] = 0

    def updateJump(self):
        for block in self.myWorld.getColliders():
            if block.colliderect(self.jumpRect):
                self.direction[1] = 0
                self.extraJump = True
                self.state = "ground"
                break
        else:
            self.state = "air"

    def jumpPadCheck(self):
        for block in self.myWorld.jumpPads:
            if block.colliderect(self.jumpRect):
                return True
        return False

    def extraJumpCheck(self):
        for block in self.myWorld.extraJump:
            if block.colliderect(self.jumpRect):
                return True
        return False
            
    def checkPlatformMove(self):
        for i, block in enumerate(self.myWorld.movingColl):
            if block.colliderect(self.jumpRect):
                self.direction[0] += self.myWorld.moves[i][0]
                self.direction[1] += self.myWorld.moves[i][1]
                self.onPlatformMove = True
                break
        else:
            self.onPlatformMove = False

    def checkCollision(self):
        for but in self.myWorld.buttons:
            if but[0].colliderect(self):
                if but[1] not in self.myWorld.pressedButtons:
                    self.myWorld.pressedButtons.add(but[1])
                    self.myWorld.reloadCollider()
                
        for ex in self.myWorld.exits:
            if ex[0].colliderect(self):
                x, y = self.myPuzzle.moving(ex[1])
                self.setPlayerPos(x, y)

    def setPlayerPos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.direction[0] = 0
        self.direction[1] = 0

    def fix(self, obj):
        if False and  self.collider.y + self.collider.height//2 > obj.y and self.collider.y + self.collider.height//2 < obj.y + obj.height:
            if self.collider.x + self.collider.width > obj.x and self.collider.x + self.collider.width < obj.x + obj.width:
                self.rect.right = min(self.rect.right, obj.x)
            if self.collider.x > obj.x and self.collider.x < obj.x + obj.width:
                self.rect.left = max(self.rect.left, obj.x + obj.width)
        
        if self.forceVec[1] != 0:
            if self.collider.y + self.collider.height > obj.y and self.collider.y + self.collider.height < obj.y + obj.height:
                self.rect.bottom = min(self.rect.bottom, obj.y-1)
                self.forceVec[1] = 0
            if self.collider.y > obj.y and self.collider.y < obj.y + obj.height:
                self.rect.top = max(self.rect.top, obj.y + obj.height)
                self.forceVec[1] = 0.01
            
        self.collider.updatePosition(self.rect.left, self.rect.top)

    def draw(self):
        pygame.draw.rect(self.display_surface, (255,0,0), self.rect)
        pygame.draw.rect(self.display_surface, (0,0,255), self.jumpRect)

    def update(self, dt):
        self.move(dt)
        self.draw()
