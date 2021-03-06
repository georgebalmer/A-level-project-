import pygame
import math
import random
# -- Global Constants





# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)


traffic_x_list = [200,400,600]

map = [[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]

### Drawing function
font_name = pygame.font.match_font('arial')
def draw_text(Surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    Surface.blit(text_surface, text_rect)

# Class definitions

#### Game class
class Game (pygame.sprite.Sprite):
    # Instantiation method
    def __init__(self):
        super().__init__()
        self.GameDone = False
        self.all_sprites_group = pygame.sprite.Group()

        #vairable for speed of player

        self.player_speed = 3
        
        #setting variables for scoreboard
        self.coins = 100
        self.bullets = 10
        self.score = 0

        # Create map
        self.roadedge_list = pygame.sprite.Group()
        # Create walls on the screen (each tile is 20 x 20 so alter coords)
        for y in range(38):
            for x in range (45):
                if map[y][x] == 1:
                    my_roadedge = Roadedge(WHITE, 20, 20, x*20, y *20)
                    self.roadedge_list.add(my_roadedge)
                    self.all_sprites_group.add(my_roadedge)
        # Create road marks
        #road mark creation
        self.roadmarks = pygame.sprite.Group()
        roadmark_y_coord = 0
        roadmark_x_coord = 350
        counter = 0
        for y in range(2):
            for x in range(20):
                roadmark = Road_mark(WHITE,5,20,roadmark_x_coord,roadmark_y_coord,1)
                self.all_sprites_group.add(roadmark)
                self.roadmarks.add(roadmark)
                roadmark_y_coord += 30
                counter += 1
            roadmark_y_coord = 0
            roadmark_x_coord += 200

        # Create player
        self.player = Player(RED,100,100,0,0)
        self.all_sprites_group.add (self.player)

        #create traffic
        #list for random spawn x co-ord
        
        self.traffic_list = pygame.sprite.Group()
        traffic_counter=0
        traffic_speedcount=4

        for y in range(3):
            traffic = Traffic(YELLOW,100,100,random.choice(traffic_x_list),random.randint(40,700)*-1,traffic_speedcount)
            self.all_sprites_group.add(traffic)
            self.traffic_list.add(traffic)
            traffic_speedcount = 4

        #create coins
        self.coin_list = pygame.sprite.Group()
        self.coiny = 0
        for y in range(3):
            coin = Coin(GREEN, 50, 50, random.choice(traffic_x_list), self.coiny, 4)
            self.all_sprites_group.add(coin)
            self.coin_list.add(coin)
            self.coiny += 50

    def check_colls(self):
        ## Check traffic collision
        traffic_hit_list = pygame.sprite.spritecollide(self.player, self.traffic_list, False)
        for hit in traffic_hit_list:
            self.GameDone = True
        lowy = 1000
        for x in self.traffic_list:
            if x.rect.y < lowy:
                lowy = x.rect.y

        ## check coin collision
        coins=0
        coin_hit_list = pygame.sprite.spritecollide(self.player, self.coin_list, True)
        for hit in coin_hit_list:
            coin = Coin(GREEN, 50, 50, random.choice(traffic_x_list), random.randint(40,700)*-1, 4)
            self.all_sprites_group.add(coin)
            self.coin_list.add(coin)
            self.coins += 1

        

        ## check bullet collisions
        bullet_hit_list = pygame.sprite.groupcollide(bullets_list, self.traffic_list, True, True)

    def update_game(self):
        self.score += 0


    
            
            

### end of game class

### Bullet class

class Bullet(pygame.sprite.Sprite):
         
    def __init__(self,x_ref,y_ref,speedy):

        super().__init__()

        self.image = pygame.Surface([10,10])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()

        #sets position
        self.rect.y = y_ref
        self.rect.x = x_ref

        self.bullet_speedy = speedy

    def update(self):
        self.rect.y -= self.bullet_speedy
        
             




### Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self,color,width,height,x_ref,y_ref,speedy):
        #constructor
        super().__init__()

        #creates sprites
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        #sets position of road mark
        self.rect.x = x_ref
        self.rect.y = y_ref

        self.coin_speedy = speedy
    def update(self):

        self.rect.y = self.rect.y + self.coin_speedy
        if self.rect.y > 600:
           self.rect.y = random.randint(40,700)*-1
           self.rect.x = random.choice(traffic_x_list)
        
           

    def coin_speedy(self, val):
        self.coin_speedy = speedy

#### end of Coin class
        


#### Player class
class Player(pygame.sprite.Sprite):

    # Instantiation method
    def __init__(self, color, width, height, speedy, speedx):

         super().__init__()

         self.x = width
         self.y = height
         self.colour = color


         self.image = pygame.Surface([width,height])
         self.image.fill(color)
         self.image = pygame.image.load("player2.png")

         self.rect = self.image.get_rect()
         self.rect.x = 400
         self.rect.y = 400

         self.player_speedy = speedy
         self.player_speedx = speedx
         
    # update method to change object of this class each time through the loop
    def update(self):
        self.rect.y = self.rect.y + self.player_speedy
        self.rect.x = self.rect.x + self.player_speedx

        #player_old_x = 0
        #player_old_y = 0

    # Sets the speed of the player horizontally
    def player_set_speedx(self, val):
        self.player_speedx = val
    # End procedure

    # Sets the speed of the player vertically
    def player_set_speedy(self,val):
        self.player_speedy = val
    #End procedure
#### End of Player class


######tile road edge class
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

#### end of road edge class

#### Road Mark class

class Road_mark(pygame.sprite.Sprite):
        
    #instantiation
    def __init__(self,color,width,height,x_ref,y_ref,speedy):

        #constructor
        super().__init__()

        #creates sprites
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        #sets position of road mark
        self.rect.x = x_ref
        self.rect.y = y_ref

        #set speed
        self.roadmark_speedy = speedy
        #end procedure


    def update(self):
         
        self.rect.y = self.rect.y + self.roadmark_speedy
        if self.rect.y > 600:
            self.rect.y=0
            g.score += 1
            
            
    def roadmark_set_speedy(self,val):
        speedy = val
        self.roadmark_speedy = speedy

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

    def update(self):
        #traffic_speedcount
        #traffic_counter
        self.rect.y = self.rect.y + self.traffic_speedy
        if self.rect.y > 600:
            self.rect.y = random.randint(40,700)*-1
            self.rect.x = random.choice([200,400,600])

        ## makes sure there are enough traffic sprites on the screen
        if len(g.traffic_list) < 3:
            traffic = Traffic(YELLOW,100,100,random.choice(traffic_x_list),random.randint(40,700)*-1,4)
            g.all_sprites_group.add(traffic)
            g.traffic_list.add(traffic)

    
    def traffic_set_speedy(self,val):
        speedy = val
        self.traffic_speedy = speedy

    def traffic_nuke(self):
        self.rect.y -= 1000



# -- Initialise PyGame
pygame.init()


# -- Blank Screen
size = (900,600)

screen = pygame.display.set_mode(size)

GameDone = False
clock = pygame.time.Clock()
g = Game()
bullets_list=pygame.sprite.Group()

while not g.GameDone:
            
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameDone = True
        # end event type

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                g.player.player_set_speedx(-1*g.player_speed)

            elif event.key == pygame.K_RIGHT:
                g.player.player_set_speedx(g.player_speed)

            elif event.key == pygame.K_UP:
                g.player.player_set_speedy(-1*g.player_speed)    

            elif event.key == pygame.K_DOWN:
                g.player.player_set_speedy(g.player_speed)    

            elif event.key == pygame.K_ESCAPE:
                GameDone = True

            elif event.key == pygame.K_1:
                if g.coins > 4:
                    g.coins -= 5
                    g.bullets += 10

            elif event.key == pygame.K_2:
                if g.coins > 9:
                    g.coins -= 10
                    g.player_speed = g.player_speed *1.2

            elif event.key == pygame.K_3:
                if g.coins > 19:
                    for x in g.traffic_list:
                        traffic_list.traffic_nuke()
                        

            elif event.key == pygame.K_SPACE:
                if g.bullets>0:
                    bullet = Bullet(g.player.rect.x+25,g.player.rect.y,10)
                    bullets_list.add(bullet)
                    g.all_sprites_group.add(bullet)
                    g.bullets -= 1
                else:
                    draw_text(screen, str("no bullets remaining"), 20, 450,10)
                

        # end event type

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                g.player.player_set_speedx(0)

            elif event.key == pygame.K_RIGHT:
                g.player.player_set_speedx(0)

            elif event.key == pygame.K_UP:
                g.player.player_set_speedy(0)
     
            elif event.key == pygame.K_DOWN:
                g.player.player_set_speedy(0)
                            
        # end event type

    # end event for loop


    # -- Game logic goes after this comment
    g.all_sprites_group.update()
    g.update_game()
    g.check_colls()
    
    
    # Runs the update function for all sprites

    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    g.all_sprites_group.draw(screen)
    draw_text(screen,  str("score: " + str(g.score)), 20, 795, 10)
    draw_text(screen, str("Quit [ESC]"), 18, 30, 20)
    draw_text(screen,  str("coins: £" + str(g.coins)), 20, 795, 30)
    draw_text(screen,  str("bullets: " + str(g.bullets)), 20, 795, 50)
    draw_text(screen,  str("Shop:"), 20, 5, 70)
    draw_text(screen,  str("[1] 10 bullets - £5"), 17, 5, 100)
    draw_text(screen,  str("[2] +20% speed - £10"), 17, 5, 120)
    draw_text(screen,  str("[3] nuke - £20"), 17, 5, 140)
    
    

    ## Put text on screen


    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # -- The clock ticks over
    clock.tick(60)
            
          
#End While
 


