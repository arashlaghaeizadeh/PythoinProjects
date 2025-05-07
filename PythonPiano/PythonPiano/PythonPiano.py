import pygame									                                                    	#Step 1
import piano_lists as pl							                                                    #Step 1
from pygame import mixer                                                                                #Step 1

pygame.init()                                                                                           #Step 1
pygame.mixer.set_num_channels(50)                                                                       #Step 1

font = pygame.font.Font("assets/Terserah.ttf", 48)                                                      #Step 1
medium_font = pygame.font.Font("assets/Terserah.ttf", 28)                                               #Step 1
small_font = pygame.font.Font("assets/Terserah.ttf", 16)                                                #Step 1
real_small_font = pygame.font.Font("assets/Terserah.ttf", 10)                                           #Step 1
fps = 60                                                                                                #Step 1
timer = pygame.time.Clock()                                                                             #Step 1
WIDTH = 52 * 35                                                                                         #Step 1
HIGHT = 400                                                                                             #Step 1
screen = pygame.display.set_mode([WIDTH,HIGHT])                                                         #Step 1
pygame.display.set_caption("My Python Piano")                                                           #Step 1
active_whites = []                                                                                      #Step 2
active_blacks = []                                                                                      #Step 2

def draw_piano(whites, blacks):                                                                         #Step 2
    white_rects = []                                                                                    #Step 2
    for i in range(52):                                                                                 #Step 2
        rect = pygame.draw.rect(screen, 'white', [i * 35, HIGHT - 300, 35, 300], 0, 2)                  #Step 2
        white_rects.append(rect)                                                                        #Step 2
        pygame.draw.rect(screen, 'black', [i * 35, HIGHT - 300, 35, 300], 2, 2)                         #Step 2
        key_label = small_font.render(pl.white_notes[i], True, 'black')                                 #Step 2
        screen.blit(key_label, (i * 35 + 3, HIGHT - 20))                                                #Step 2
    skip_count = 0                                                                                      #Step 2
    last_skip = 2                                                                                       #Step 2
    skip_track = 2                                                                                      #Step 2
    black_rects = []                                                                                    #Step 2
    for i in range(36):                                                                                 #Step 2
        rect = pygame.draw.rect(screen, 'black', [23 + (i * 35) + (skip_count * 35), HIGHT - 300        #Step 2
                                                  , 24 , 200], 0, 2)                                    #Step 2
        for q in range(len(blacks)):                                                                    #Step 2
            if blacks[q][0] == i:                                                                       #Step 2
                if blacks[q][1] > 0:                                                                    #Step 2
                    pygame.draw.rect(screen, 'green', [23 + (i * 35) * (skip_count * 35), HIGHT - 300   #Step 2
                                                       , 24 , 200], 2, 2)                               #Step 2
                    blacks[q][1] -= 1                                                                   #Step 2

        key_label = real_small_font.render(pl.black_labels[i], True, 'white')                           #Step 2
        screen.blit(key_label, (25 + (i * 35) + (skip_count * 35) , HIGHT - 120))                       #Step 2
        black_rects.append(rect)                                                                        #Step 2
        skip_track += 1                                                                                 #Step 2
        if last_skip == 2 and skip_track == 3:                                                          #Step 2
            last_skip = 3                                                                               #Step 2
            skip_track = 0                                                                              #Step 2
            skip_count += 1                                                                             #Step 2
        elif last_skip == 3 and skip_track == 2:                                                        #Step 2
            last_skip = 2                                                                               #Step 2
            skip_track = 0                                                                              #Step 2
            skip_count += 1                                                                             #Step 2

        for i in range(len(whites)):                                                                    #Step 2    
                if whites[i][1] > 0:                                                                    #Step 2
                    j = whites[i][0]                                                                    #Step 2
                    pygame.draw.rect(screen, 'green',  [j * 35, HIGHT - 100, 35 , 100], 2, 2)           #Step 2
                    whites[i][1] -= 1                                                                   #Step 2
    return white_rects, black_rects, whites, blacks                                                     #Step 2
run = True                                                                                              #Step 1 
while run:                                                                                              #Step 1
    timer.tick(fps)                                                                                     #Step 1
    screen.fill('gray')                                                                                 #Step 1
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)     #Step 2


    for event in pygame.event.get():                                                                    #Step 1
        if event.type == pygame.QUIT:                                                                   #Step 1
            run = False                                                                                 #Step 1

        pygame.display.flip()                                                                           #Step 1
pygame.quit()                                                                                           #Step 1