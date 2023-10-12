import pygame 
#import time
from pygame.locals import * 


def draw_block():
    surface.fill((110,110,5))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__== "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))
    surface.fill((44, 145, 36))
    
    
    #time.sleep(3)  #-> to see output for a specific time
    # Loading an image 
    block = pygame.image.load("C:\Users\Admin\Desktop\New Folder\snake_game\block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x,block_y))
    #event loop is fundamental in any ui program this is done by while loop 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    pass

            elif event.type == QUIT :
                running = False
