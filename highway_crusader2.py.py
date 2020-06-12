import pygame
import math
import random
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,25)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()


# -- Blank Screen
size = (900,600)

screen = pygame.display.set_mode(size)





map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]






# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

 # -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# -- classes
#Road_mark class
class Road_mark(pygame.sprite.Sprite)
    def __init__(self,color,width,height)

#traffic class
class Traffic(pygame.sprite.Sprite):

    #instantiation
    def __init__(self,color,width,height,x_ref,y_ref,speedy):

        #constructor
        super().__init__()

        #creates sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the traffic attributes
        self.rect.x = x_ref
        self.rect.y = y_ref

        self.traffic_speedy = speedy

    def traffic_set_speedy(self,val):
        speedy = val
        self.traffic_speedy = speedy





#tile road edge class
class Roadedge(pygame.sprite.Sprite):

    #instatiation
    def __init__(self,color, width, height, x_ref, y_ref):

        #sprite constructor
        super().__init__()

        #creates sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the road edge attributes
        self.rect.x = x_ref
        self.rect.y = y_ref


    def road_widen(self, value)
        for y in range(39):

    def road_narrow(self, value)

    def Left__right_bend(self)

    def Right_left_bend(self)


# player class
class Player(pygame.sprite.Sprite):

    # Instatnitaion method
    def __init__(self, color, width, height, speedy, speedx):



         super().__init__()

         self.x = width
         self.y = height
         self.colour = color


         self.image = pygame.Surface([width,height])
         self.image.fill(color)

         self.rect = self.image.get_rect()
         self.rect.x = 400
         self.rect.y = 400

         self.player_speedy = speedy
         self.player_speedx = speedx
    # update method to change object of this class each time through the loop
    def update(self):
        self.rect.y = self.rect.y + self.player_speedy
        self.rect.x = self.rect.x + self.player_speedx


        player_old_x=0
        player_old_y=0

    def player_set_speedx(self, val):
        self.player_speedx = val
    # End procedure

    def player_set_speedy(self,val):
        self.player_speedy = val
    #End procedure

#Police car class
class Police_car(pygame.sprite.Sprite):

    #instatiation
        def __init__(self, width, height, x_ref, y_ref, speedx, speedy):

            #sprite constructor
            super().__init__()
        #end procedure

        def update(self):
            self.rect.y = self.rect.y + self.speedy
            self.rect.x = self.rect.x + self.speedx
        #end procedure

        def police_car_set_speedy(self,val):
            self.speedy = val
        #end procedure

        def police_car_set_speedx(self,val):
            self.speedx = val
        #end procedure


all_sprites_group = pygame.sprite.Group()

# -- object creation
#player creation
player = Player(RED,20,20,0,0)
all_sprites_group.add (player)

#traffic creaation
traffic_list = pygame.sprite.Group()
traffic_counter=0
speedcount=1
for y in range(5):
    traffic = Traffic(YELLOW,10,10,random.randint(320,550),random.randint(40,200)*-1,speedcount)
    all_sprites_group.add(traffic)
    traffic_counter += 1
    speedcount = 4


#roadedge creataion
roadedge_list = pygame.sprite.Group()



# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(38):
    for x in range (45):
        if map[y][x] == 1:
            my_roadedge = Roadedge(WHITE, 20, 20, x*20, y *20)
            roadedge_list.add(my_roadedge)
            all_sprites_group.add(my_roadedge)

#code for collision group
player_hit_list=pygame.sprite.Group()

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                done = True


          if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        player.player_set_speedx(-3)

                elif event.key == pygame.K_RIGHT:
                        player.player_set_speedx(3)
          #end if

          if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.player_set_speedy(-3)

                elif event.key == pygame.K_DOWN:
                    player.player_set_speedy(3)
          #end if
          if event.type == pygame.KEYUP:
                     player.player_set_speedy(0)
                     player.player_set_speedx(0)
          #end if



          #End If
     #Next event
    # -- Game logic goes after this comment
    player_old_x = player.rect.x
    player_old_y = player.rect.y

    player_hit_list = pygame.sprite.spritecollide(player, roadedge_list, False)

    for foo in player_hit_list:
        player.player_set_speedx(0)
        player.player_set_speedy(0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y


    traffic_hit_list = pygame.sprite.spritecollide(player, traffic_list, False)
    for foo in traffic_hit_list:
        traffic_list.traffic_set_speedy(0)
        player.player_set_speedx(0)
        player.player_set_speedy(0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y

    # Runs the update function for all sprites
    all_sprites_group.update()



    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    all_sprites_group.draw (screen)


    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
