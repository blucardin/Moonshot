import pygame
import random
import time 

pygame.init()

pygame.display.set_caption("Snake")

color = (225,225 , 225 )

winxlength = 1118
winywidth = 948
win = pygame.display.set_mode((winxlength, winywidth))

font = pygame.font.Font('freesansbold.ttf', 80)    
StartGame = font.render('Start Game', True, (255,0,0)) 
textRect = StartGame.get_rect()
textRect.center = (winxlength / 2, winywidth / 2) 

font2 = pygame.font.Font('freesansbold.ttf', 40)   
byNoahV = font2.render('© 2020 by Noah V', True, (255,0,0)) 
textRect2 = byNoahV.get_rect()
textRect2.center = (winxlength / 2, (winywidth / 8) * 6) 

class asteroid:
    def __init__(self, x, y, radius):
        self.x = x 
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, (0, 0, 225), (self.x, self.y), self.radius)

    def moveup(self, vel):
        self.y = self.y - vel

class layzer:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(win, (0, 225, 0), (self.x, self.y, self.width, self.height))

    def movedown(self, vel):
        self.y = self.y + vel

def titlescreen():
    run = True
    while run:
        win.fill((0,0,0))

        mousepos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        font2 = pygame.font.Font('freesansbold.ttf', 40)   
        byNoahV = font2.render('© 2020 by Noah V', True, (255,0,0)) 
        textRect2 = byNoahV.get_rect()
        textRect2.center = (winxlength / 2, (winywidth / 8) * 6) 

        pygame.draw.rect(win, (0,0,0), textRect)

        pygame.draw.rect(win, (0,0,0), textRect2)

        if mousepos[0] >= textRect2[0] and mousepos[0] <= textRect2[0] + textRect2[2] and mousepos[1] >= textRect2[1] and mousepos[1] <= textRect2[1] + textRect2[3]:
            byNoahV = font2.render('Dedicated to grade 9 geography classes', True, (0, 255, 0)) 
            textRect2 = byNoahV.get_rect()
            textRect2.center = (winxlength / 2, (winywidth / 8) * 6) 
            
        win.blit(byNoahV, textRect2)

        if mousepos[0] >= textRect[0] and mousepos[0] <= textRect[0] + textRect[2] and mousepos[1] >= textRect[1] and mousepos[1] <= textRect[1] + textRect[3]:
            StartGame = font.render('Start Game', True, (0, 255, 0)) 

        else:
            StartGame = font.render('Start Game', True, (255, 0, 0)) 

        win.blit(StartGame, textRect)

        pygame.display.update()  



def gamescreen():

    x = winxlength / 2
    y = 0 
    height = 50 
    width = 60
    asteroids = []
    asteroidvel = 4
    roketvelactual = 4
    direction = []
    roketvel = roketvelactual
    count = 0
    layzers = []
    layzervel = 4

    for i in range(0, 100):
        asteroids.append(asteroid(random.randint(0, winxlength), (i * 100) + winywidth, 50))

    run = True
    while run:
        win.fill((0,0,0))
        
        mousepos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(win, (0, 0, 225), (x, y, width, height))

        if pygame.mouse.get_pressed()[0] == True:
            asteroids.clear()
            for i in range(0, 100):
                asteroids.append(asteroid(random.randint(0, winxlength), (i * 100) + winywidth, 50))

        if keys[pygame.K_SPACE] == True:
            layzers.append(layzer(x, y, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if mousepos[0] > x + width:
            x = x + roketvel
            direction.append("right")

        elif mousepos[0] < x :
            x = x - roketvel
            direction.append("left")

        for c in asteroids:
            if c.y - c.radius <= winywidth:
                c.draw()
            c.moveup(asteroidvel)

        counter = 0
        for o in layzers:
            o.draw()
            o.movedown(layzervel)
            if o.y >= winywidth:
                layzers.pop(counter)
            counter = counter + 1

        pygame.display.update()  


titlescreen()
gamescreen()