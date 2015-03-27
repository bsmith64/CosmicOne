import pygame
import random

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# # # # # # # # # - - CLASSES - - # # # # # # # # #

class Block(pygame.sprite.Sprite):

        def __init__(self,color):
                # Init the parent class
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('astroid-1.png')
                self.rect = self.image.get_rect()



                #self.image = pygame.Surface((50,50)).convert()
                #self.image.fill(pygame.Color("white"))
                #self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('starshipOne.png')
                self.rect = self.image.get_rect()
                

                #self.image = pygame.Surface((50,50)).convert()
                #self.image.fill(pygame.Color("green"))
                #self.rect = self.image.get_rect()


class Bullet(pygame.sprite.Sprite):

        def __init__(self):
                pygame.sprite.Sprite.__init__(self)

                self.image = pygame.Surface([4,10])
                self.image.fill(green)

                self.rect = self.image.get_rect()

        def update(self):
                self.rect.y -= 30



pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])



all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
astroid_trash = pygame.sprite.Group()



"""for i in range(20):

        block = Block(black)

        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(350)

        block_list.add(block)
        all_sprites_list.add(block)"""


# LOGIC THAT GENERATES FIRST ASTROID - - - - - - - - - -

"""block = Block(black)

block.rect.x = random.randrange(screen_width * 0.8)
block.rect.y = random.randrange(screen_height * 0.8)

all_sprites_list.add(block)
block_list.add(block)"""


# Create the player - - - - - - - - - -
player = Player()
all_sprites_list.add(player)



# Game paramaters - - - - - - - - - - -
clock = pygame.time.Clock()

x_change = 300
y_change = 400

player.rect.x = x_change
player.rect.y = y_change


# # # # # # # # # # - - MAIN GAME LOOP - - # # # # # # # # #

def gameLoop():

        score = 0
        x_change = 0
        y_change = 0
        movement = 11

        astroid_speed = 10

        # GENERATED THE ASTROIDS - - - - - - - - - - -
        block = Block(black)

        block.rect.x = random.randrange(screen_width * 0.8)
        block.rect.y = -200
        
        all_sprites_list.add(block)
        block_list.add(block)

        # THE LOOP - - - - - - - - - -
        done = False
        while not done:


                

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                                pygame.quit()
                                quit()
                        
                        # MOVEMENT - - - - - - - - - - -
                        if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_LEFT:
                                        x_change -= movement
                                if event.key == pygame.K_RIGHT:
                                        x_change += movement
                                if event.key == pygame.K_UP:
                                        y_change -= movement
                                if event.key == pygame.K_DOWN:
                                        y_change += movement
                        
                        # CONTINUAL MOVEMENT - - - - - - - - - - -
                        if event.type == pygame.KEYUP:

                                if event.key == pygame.K_LEFT:
                                        x_change = 0
                                if event.key == pygame.K_RIGHT:
                                        x_change = 0
                                if event.key == pygame.K_UP:
                                        y_change = 0
                                if event.key == pygame.K_DOWN:
                                        y_change = 0

                        
                        # BULLET FIRE - - - - - - - - - - -
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_s:

                                        bullet = Bullet()

                                        bullet.rect.x = player.rect.x + 38
                                        bullet.rect.y = player.rect.y

                                        all_sprites_list.add(bullet)
                                        bullet_list.add(bullet)


                                

                player.rect.x += x_change
                player.rect.y += y_change
                all_sprites_list.update()



                for bullet in bullet_list:

                        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

                        for block in block_hit_list:
                                bullet_list.remove(bullet)
                                all_sprites_list.remove(bullet)
                                score += 1
                                block_list.remove(block)
                                astroid_trash.add(block)
                                print (astroid_trash)
                                print (score)

                        

                        if block.rect.y > 600:
                                print (block.rect.y)
                                block_list.remove(block)
                                all_sprites_list.remove(block)
                                astroid_trash.add(block)

                        if len(astroid_trash) == 1 :
                                block.rect.x = random.randrange(screen_width * 0.8)
                                block.rect.y = -200



                                print (block.rect.x)
                                print (block.rect.y)

                                all_sprites_list.add(block)
                                block_list.add(block)
                                astroid_trash.remove(block)
               

                        if bullet.rect.y < -10:
                                bullet_list.remove(bullet)
                                all_sprites_list.remove(bullet)

                


                block.rect.y += astroid_speed


                


                # GAME BOUNDARIES - - - - - - - - -

                if player.rect.x < 0 or player.rect.x > screen_width - 79:
                        done = True
                        
                if player.rect.y < 0 or player.rect.y > screen_height - 70:
                        done = True
                        





                screen.fill(black)
                all_sprites_list.draw(screen)

                pygame.display.update()

                clock.tick(30)

gameLoop()
pygame.quit()
quit()



