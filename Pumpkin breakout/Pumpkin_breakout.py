import pygame # library
import math
import random
import webbrowser
pygame.init()



class pumpkin:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.length = 80
        self.width = 80
        self.color = (random.randint(-20, 20), random.randint(-10, 10), random.randint(-10, 10))
        self.Color = (234, 117, 24)
        self.alive = True
        if random.randint(0,100) == 1:
            self.Color = (234,244,244)
    def draw(self,screen):
        if self.alive:
            pygame.draw.rect(screen, (50, 200, 10), (self.xPos+self.length/2.5,self.yPos-15, 20, 20))#STEM
            pygame.draw.ellipse(screen, (self.Color[0]+self.color[0], self.Color[1]+self.color[1], self.Color[2]+self.color[2]), (self.xPos,self.yPos, self.length, self.width))

            pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/4,self.yPos+self.width/8,self.length/4,self.width/4), 0, math.pi, 4)#eyes
            pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/1.9,self.yPos+self.width/8,self.length/4,self.width/4), 0, math.pi, 4)#eyes

            pygame.draw.arc(screen, (0,0,0), (self.xPos+self.length/4,self.yPos+40,self.length/2,self.width/2), math.pi, 0, 7)#mouth
    def collide(self, x, y):
        if self.alive:
            if math.sqrt((x-self.xPos)*(x-self.xPos)+(y-self.yPos)*(y-self.yPos))<80:
                self.alive = False
                return True
        return False

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("breakout")
clock = pygame.time.Clock()
controller = pygame.joystick.Joystick(0)
controller.init()
font = pygame.font.Font("freesansbold.ttf", 50)


doExit = False
px = 300
py = 450

bx = 200
by = 200

bVx = 5
bVy = 5

gamestate = 0

# create a bunch of bricks!


bricklist = list()
for i in range(10):
    bricklist.append(pumpkin(i*70, 0))
while not doExit: #__________________game loop_____________

    #I/O section.....................................
    
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    if gamestate == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            px -= 5
        if keys[pygame.K_d]:
            px += 5

        px += controller.get_axis(0)*5
        px += controller.get_axis(1)*5
    
        # physics section...........................
    
        #move the ball 
        bx += bVx
        by += bVy
    
        # bounce of ceiling floor and walls
        if bx < 0 or bx > 680:
            bVx *= -1
        if by < 0 or by > 480:
            bVy *= -1
    
        #paddle bounce collision
        if by + 20 > py and bx + 20 > px and bx < px + 100:
            bVy *= -1
    
    
        #render section.......................................
        screen.fill((0,0,0))
    
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 100, 20))
        pygame.draw.circle(screen, (255, 255, 255),(bx, by), 15)
    
        done = -0
        for i in range(len(bricklist)):
            if bricklist[i].collide(bx,by):
                bVy *=-1
            bricklist[i].draw(screen)
        
            if bricklist[i].alive==False:
                done += 1 # checks if the whole list is dead
            if done == len(bricklist):
                gamestate = 1
    
        done = 0
    if gamestate == 1:
        screen.fill((0,0,0))#troll code
        mousePos = pygame.mouse.get_pos()
        mouseButtons = pygame.mouse.get_pressed(3)
        text = font.render("CLICK HERE FOR FRE", True, (255,255,255))
        text2 = font.render("B BUCK", True, (255, 255, 255))
        if mousePos[0] > 200 and mousePos[0] < 400 and mousePos[1] > 100 and mousePos[1] < 300 and mouseButtons[0]:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        pygame.draw.rect(screen, (255, 0, 0), (200, 100, 200, 200))
        screen.blit(text, (100, 110))
        screen.blit(text2, (200, 150))
    pygame.display.flip()
            
print("You are congradulation!")
print("Click here for free ninteen dolar fortnight card")
webbrowser.open("https://downloadmoreram.com/")
#end game loop_______________________
pygame.quit()