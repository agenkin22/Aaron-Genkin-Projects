

#include required modules
import pygame, sys, random
from math import sqrt
import math
from random import randint
#import the local constants for later use
from pygame.locals import *



#GAME SETUP
# Initialize Pygame
pygame.init()
# Define colors using tuples
BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (0,255,0)
PURPLE = (128,0,128)
BLUE = (0,0,255)
"""
above^^^ importing all nessesary modules, and defining important colors for the game.
"""
"""
below, this is the first class of my game, meant for words and text.
"""
class Text_Game(pygame.sprite.Sprite):
  #initializing the class
  def __init__(self,size,color,x,y,text, font = None):
    super().__init__()

    #defining all the variables based on inputs
    self.size = size
    #setting the size and font (in this case no font) of text
    self.font = pygame.font.Font(font, size)
    self.color = color
    self.text = text

    #rendering the words so it can be drawn on the screen
    self.image = self.font.render(self.text, 1, self.color)
    #convert to rect
    self.rect = self.image.get_rect()
    #x and y coordinate of text
    self.rect.x = x
    self.rect.y = y

  def updates(self):
    #this class function is for actually displaying the word on the screen, useful in the main code of the game
    self.image = self.font.render(self.text, 1, self.color)
    screen.blit(self.image, (self.rect.x, self.rect.y))

#This class is eirie similar to the class Text_Game, with the one being the previous class being for text, and this one"
#being for the score. I could have made them part of the same parent class, saving space in my code, but ended up just letting them be different classes"

class Scoreboard(pygame.sprite.Sprite):
  def __init__(self,score,size,color,x,y,font=None):
    #initializing the class
    super().__init__()

    #defining variables from the class similar to the class Text_Game
    #the major differece here is that I use self.score in defining self.text, as this class is for defining classes
    #this aspect made me make this class and Text_Game seperate, as I thought coding it would be faster that way.
    self.color = color
    self.font = pygame.font.Font(font, size)
    self.score = score
    # again the self.score and self.text of this class is the main difference
    self.text = str(self.score)
    self.image = self.font.render(self.text, 1, self.color)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  #def draw(self):
  #def score_update:
#updtae the text of the scoreboard
  def updates(self):
    # this class function is similar to the one in Text_Game, however this class function in adition to displayng the text, can constantly
    #update the score in the game loop
    self.text = "Score: " + str(self.score)
    self.image = self.font.render(self.text, 1, self.color)
    screen.blit(self.image, (self.rect.x, self.rect.y))

#this class is for the target. This is a very simple class. Instead of putting the functionality,
#in a class function, (every time it collides with the player, it teleports)
#I thought it would just be easier to have that in the Game loop
class Target(pygame.sprite.Sprite):
  def __init__(self, x, y, colors, screen):

    super().__init__()

    #initializing variables
    self.colors = colors
    self.x = x
    self.y = y
    self.screen = screen

    #drawing square target on the screen
    pygame.draw.rect(self.screen, self.colors, (self.x,self.y, 50, 50))

  def draw_target(screen, a, b):
    #updating target position
    pygame.draw.rect(screen, BLUE, (a,b, 50, 50))

#this class again is similar to target class when it comes to variables. The difference is this one in __init__ creates
#a circle for the player, and not a rect like for the target
class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, screen):

    super().__init__()

    #initializing variables
    self.x = x
    self.y = y

    #drawing player circle on the screen
    pygame.draw.circle(screen, WHITE, (self.x,self.y),30)

  def draw_player(screen):
    #this class function is crucial for the game, as it is responsible for drawing the circle
    #at the position of the mouse. Using this function, allows for the effect of the player following the mouse around

    #I found this function pygame.mouse.get_pos() when scrounging the internet,
    #https://stackoverflow.com/questions/23841128/pygame-how-to-check-mouse-coordinates

    #stack overflow, as alwats is helpful when coding
    a,b = pygame.mouse.get_pos()

    #drawing circle at mouse position
    pygame.draw.circle(screen, WHITE, (a, b), 30)

# Set the height and width of the screen
width, height = 800, 600

#create the screen surface
screen = pygame.display.set_mode((width, height))
screen.fill(BLACK)

#creating the player and target sprites using my two classes, Player and Target
plastic = Player(100,100, screen)
target = Target(700,300,BLUE,screen)

#creating scoreboard sprite using my scoreboard class
scores = Scoreboard(0,50,WHITE,590,30)

#here I just use my text_game class to create a bunch of text for the homescreen. none of these sprites will have game functionality,
#its just for the player to read when they start playing the game.
start1 = Text_Game(50,WHITE,0,150,"Click on player ^^^")
start2 = Text_Game(50,WHITE,0,200,"to start game")
start3 = Text_Game(50,WHITE,400,0," << Avoid this obstacle")
start4 = Text_Game(50,WHITE,400,250,"Pick up as many ")
start5 = Text_Game(50,WHITE,400,300," facemasks as >>")
start6 = Text_Game(50,WHITE,400,350,"as possible to")
start7 = Text_Game(50,WHITE,400,400,"clean environment")

#created a sprite for the gameover screen, also using the Text_Game class. I think in some ways, the Text_Game and Scoreboard classes
#can be used with similar functionality
gameover = Text_Game(100,WHITE,0,300,"Your Score: "+ str(scores.score))
#create a sprite group to hold all the sprites
#all_sprites = pygame.sprite.Group()
"""
I ended up not grouping all the sprites into all_sprites, simply because in my game I didn't see the necessity for it
"""
#add the player sprite to the group
#all_sprites.add(plastic)
#all_sprites.add(target)
#ll_sprites.add(scores)

#GAME LOOP


clock = pygame.time.Clock()

 #set the initial crashed condition
crashed = False

#using the class function of Text_Game to display all the instructions (are sprites) on the Homescreen
start1.updates()
start2.updates()
start3.updates()
start4.updates()
start5.updates()
start6.updates()
start7.updates()

#initial cordinates of the purple obstacle
h,j = 400,0

#drawing the purple obstacle on the screen
pygame.draw.circle(screen, PURPLE, (h, j), 30)

#I ended up not using a class for this, as the functionality it serves can be writen in a few lines in the Game loop

#speed of obstacle
rate_x = 20
rate_y = 12

#GAME LOOP
while not crashed:
  start = "no start"
  #loop to run as long as game runs

  #initial coordinates of the target, we will be combining this with the targets.update function to make the target teleport
  #around the screen
  e = 300
  g = 700
  for event in pygame.event.get():
    #getting python events
    if event.type==QUIT:
          pygame.quit()
          sys.exit()
          #standard code to check for crashes
    if event.type == pygame.MOUSEBUTTONDOWN:
      #checking for when left mouse button will be clicked

      #using pygame.mouse.get_pos to get pos of mouse
      mouse_x, mouse_y = pygame.mouse.get_pos()

      #distance between mouse, and initial position of player, 100,100

      #I used try: and except ValueError because of a math domain error that occured in the code.
      #I'm still not sure why this error was happening, but it was happening because the
      #number inside the square root sometimes somehow ended up being negative.
      #To fix this, I wrote a line of code, the ValueError line, to if the value inside the square root
      #is negative, make it positive
      try:
        distance = sqrt((100 - mouse_x)^2 + (100 - mouse_y)^2)
      except ValueError:
        distance = sqrt(-((100 - mouse_x)^2 + (100 - mouse_y)^2))

      if distance < 20:
        #if the mouse is clicked when the cursor is hovering over the player, this code tuns

        #screen is blacked out,
        screen.fill(BLACK)

        #player and target are drawn again using class function. The player will now also  follow the mouse
        Player.draw_player(screen)
        Target.draw_target(screen, g, e)
        pygame.display.flip()
        pygame.display.update()

        #making start = "start" now allows the next code to run
        #look at the next if statement :)
        start = "start"

  #this large part of the code, which is the majority of the game,
  #will only run when certain conditions are met, as mentioned above
  if start == "start":
    truth = True

    #miliseconf counter,
    mili_c = 100

    #second counter
    militext = 0

    #this is kind of like a game loop within a gameloop, but truth = True will be changed to truth = False when the timer
    #runs out and the game is over, allowing the code to progress, and the gameover screen to display
    while truth:
      #counter +1
      mili_c += 1

      #getting mouse pos
      m_x, m_y = pygame.mouse.get_pos()
      #print((700 - m_x)*(700-m_x) + (300 - m_y)*(300 - m_y))
      #dist_n = math.sqrt((700 - m_x)*(700-m_x) + (300 - m_y)*(300 - m_y))      scores.updates()

      #blacking out the screen, and then updating the position of player and target,  as well as updating the score.
      screen.fill(BLACK)
      scores.updates()
      Player.draw_player(screen)
      Target.draw_target(screen, g, e)

      if mili_c > 25:
          #every time mili_c rotates from 0-25, a second passes, and we have to update the timer in this if statement
          #mili_c is then reset back to zero
          mili_c = 0

          #text of timer
          mili_text = "Time: " + str(20 - militext)

          #adding a second to the second counter
          militext += 1

          #rendering  the text
          fonte = pygame.font.SysFont(None, 50)
          mili_img = fonte.render(mili_text, 1, WHITE)
      #displaying the updated time on the screen
      screen.blit(mili_img, (30, 30))

      #move the obstacle by the rate of change
      j += rate_y
      h += rate_x
      #when the obstacle gets to the side of the screen, its direction reverses. this is done
      #by these two if statements, which check if its location is outside the screen
      if j >= 600 or j <= 0:
        rate_y = rate_y*-1
      if h >= 800 or h <= 0:
        rate_x = rate_x*-1
      #position of obstacle is updated
      pygame.draw.circle(screen, PURPLE, (h, j), 30)
      pygame.event.get()
      #checking to see if obstacle and player are next to each other
      if h - m_x  < 60 and j - m_y < 60 and m_x-h < 60 and m_y-j < 60:
        #if yes, -1 to score
        scores.score -= 1
      #update display
      pygame.display.update()

      #delay in the game,  to reduce fps and lag. The timer was done with this in mind
      pygame.time.delay(10)

      #checks if player and target are next to each other
      if m_x - g  < 40 and m_y - e < 40 and g - m_x < 40 and e - m_y < 40:
        # if they are, the targets cordinated will be set at random
        g = randint(30,770)
        e = randint(30,570)

        #a sound effect is played when the player collides w the target
        #this is something we didn't learn in class, this info i found here when researching
        #https://nerdparadise.com/programming/pygame/part3
        pygame.mixer.music.load('Ding - Sound Effect (HD).mp3')
        pygame.mixer.music.play(0)

        #score is obviously increased by one when the player and target colide, again, the scoring is handled by our Scoreboard class
        scores.score += 1
        print(scores.score)

        #updates new score, displaying the new decreased score on the screen.
        scores.updates()

        #this if statements checks when time runs out
      if militext == 21:
        #loop stops
        truth = False
        #the screen is blacked out
        screen.fill(BLACK)

        #endscreen is displayed with final score using gameover sprite, Text_Game class, and updating the value of gameover.text
        gameover.text = "Your Score: "+str(scores.score)
        gameover.updates()
        scores.score = 0

        #game is OVER :) my highscore with the obstacles is 17, man do those obstacles punish you
        #since the player could be in contact with the obstacles for a couple game loops, touching the obstacles punishes your score a lot
  #draw all sprites
  #all_sprites.draw(screen)



  """I intended for the code to be playable and record highscores, but the method I tried to use created too much lag so I ended up deleting most of it
  Redefining the classes everytime is not a good method to acheive what I was trying to do
  """
  #plastic = Player(100,100, screen)
  #target = Target(700,300,BLUE,screen)
  #start1.updates()
  #start2.updates()
  #start3.updates()
  #start4.updates()
  #start5.updates()
  #start6.updates()
  #start7.updates()
  #update the display
  pygame.display.flip()

  #clear the background
  #screen.fill(BLACK)

  #update the Clock
  clock.tick(30)
  for event in pygame.event.get():
      if event.type==QUIT:
          pygame.quit()
          sys.exit()
  pygame.display.update()

  #pygame.quit()
# quit
pygame.quit()

quit()
