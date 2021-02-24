import pygame
import math #needed for square root function



pygame.init()#initializes Pygame
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

isBig = False

print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200
circY = 200
radius = 100

#drawing cookie
CookiePic = pygame.image.load("cookieyeet.jpeg")
CookieRect = CookiePic.get_rect(topleft = (100,100))

CookiePic2 = pygame.image.load("cookieyeet.jpeg")
CookieRect2 = CookiePic2.get_rect(topleft = (90,90))
#score
font = pygame.font.Font('freesansbold.ttf', 32)
text1 = font.render('score', False, (66,245,164))
text2 = font.render(str(int(numClicks)), 1, (66,245,164))
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
      if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2)<radius:
        numClicks+=1
      print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2)<radius:
          isBig = True
        else:
          isBig = False
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    print("clicks:", numClicks) #uncomment this once collision is set up

    if isBig == False: #MO changed "=" to "=="" and added a colon at the end of the line.
      screen.blit(CookiePic,CookieRect)
    else:
      screen.blit(CookiePic2,CookieRect2) #MO changed a typo in how you spelled "blit" (you said bit)

    text2 = font.render(str(int(numClicks)), 1, (66,245,164))
    screen.blit(text1, (10,10))
    screen.blit(text2, (110,10))
    #screen.blit(CookiePic, CookieRect) #MO commented this out (you should only draw cookies inside that if statement)    
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()



