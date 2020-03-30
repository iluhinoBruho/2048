import random
import pygame
import time
import sys


delta = [0]
def show(a:list):
    for line in a:
        print(*line)

def get_free(a):
    n = len(a)
    res = []
    for i in range(n):
        for j in range(n):
            if not a[i][j]:
                res.append((i, j))
    return res

def add(field):
    global DEATH
    local_free = get_free(field)
    if not local_free:
        DEATH = True
        return
    cur = 2
    if len(local_free) >= 2:
        x = random.choice(local_free)
        #free.remove(x)
        #y = random.choice(free)
        v = random.random()
        if v >= 0.75:
            num = 4
        else:
            num = 2
        field[x[0]][x[1]] = num
        #field[y[0]][y[1]] = 4
    else:
        field[local_free[0][0]][local_free[0][1]] = 2
        

def shift_left(field):
    def shift_row(a:list):
        last = 0
        for i in range(1, len(a)):
            if a[i] == 0:
                continue
            else:
                if a[i] == a[last] and last != i:
                    a[last] <<= 1 #*=2
                    delta[0] += a[last]
                    a[i] = 0
                    #empty = last + 1
                    last = i + 1
                else:
                    tmp = a[i]
                    a[i] = 0                    
                    for j in range(i + 1):
                        if not a[j]:
                            a[j] = tmp
                            last = j
                            break
    
    
                    
    for line in field:
        shift_row(line)
    add(field)

                    
                
                
def shift_right(field):
    def shift_row(a:list):
        last = len(a) - 1
        for i in range(len(a) - 2, -1, -1):
            if a[i] == 0:
                continue
            else:
                if a[i] == a[last] and last != i:
                    a[last] <<= 1
                    delta[0] += a[last]
                    a[i] = 0
                    last = i - 1
                else:
                    tmp = a[i]
                    a[i] = 0                    
                    for j in range(len(a) - 1, i - 1, -1):
                        if not a[j]:
                            a[j] = tmp
                            last = j
                            break
    
                    
    for line in field:
        shift_row(line)
    add(field)
                  
def shift_up(field):
    def shift_row(a:list):
        last = 0
        for i in range(1, len(a)):
            if a[i] == 0:
                continue
            else:
                if a[i] == a[last]  and last != i:
                    a[last] <<= 1
                    delta[0] += a[last]
                    a[i] = 0
                    last = i + 1
                else:
                    tmp = a[i]
                    a[i] = 0                    
                    for j in range(i + 1):
                        if not a[j]:
                            a[j] = tmp
                            last = j
                            break
        return a
        
    
    for i in range(len(field)):
        column = []
        for j in range(len(field)):
            column.append(field[j][i])
        shifted = shift_row(column)
        for j in range(len(field)):
            field[j][i] = shifted[j]
    add(field)

def shift_down(field):
    def shift_row(a:list):
        last = len(a) - 1
        for i in range(len(a) - 2, -1, -1):
            if a[i] == 0:
                continue
            else:
                if a[i] == a[last]  and last != i:
                    a[last] <<= 1
                    delta[0] += a[last]
                    a[i] = 0
                    last = i - 1
                else:
                    tmp = a[i]
                    a[i] = 0                    
                    for j in range(len(a) - 1, i - 1, -1):
                        if not a[j]:
                            a[j] = tmp
                            last = j
                            break
        return a
        
    
    for i in range(len(field)):
        column = []
        for j in range(len(field)):
            column.append(field[j][i])
        shifted = shift_row(column)
        for j in range(len(field)):
            field[j][i] = shifted[j]
    add(field)

def death(screen, score):
    #some output
    k = 4/8 * 1.3
    pygame.draw.rect(screen, (12, 12, 12), (int(50), int(100), int(350 * 1.3) + 10, int(300 * 1.3)))
    
    font = pygame.font.SysFont("comicsansms", int(137 * k))
    text = font.render("WAISTED", True, (240, 0, 0))
    screen.blit(text, (int(60), int(120)))    
    
    font = pygame.font.SysFont("comicsansms", int(73 * k))
    text = font.render("Your score: {}".format(score), True, (230, 230, 230))
    screen.blit(text, (int(90 + 30 * (1 - k)), int(160 + 150 * k))) 
    
    font = pygame.font.SysFont("comicsansms", int(30 * k))
    text = font.render("Press Space to restart or press any key to exit".format(score), True, (218, 165, 32))
    screen.blit(text, (int(66 + 30 * (1 - k)), int(350 + 150 * k))) 
    pygame.display.update()
    
    
    
    #time.sleep(10)
    global DEATH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                DEATH = False
                RUN()
            else:
                pygame.quit()
                sys.exit()
                
    

#No win in this game
#def win():
#    exit()
def start_menu(screen):
    W, H = 565, 685
    #pygame.init()
    #screen = pygame.display.set_mode((W, H))
    #pygame.display.set_caption("2048")
    #pygame.display.update()
    
    k = 4/8 * 1.3 
    pygame.draw.rect(screen, (0, 0, 128), (int(50), int(100), int(350 * 1.3), int(300 * 1.3)))
    
    font = pygame.font.SysFont("comicsansms", int(30 * k))
    text = font.render("PRESS 0 TO SART STANDART (4x4) GAME", True, (230, 230, 230))
    screen.blit(text, (int(80), int(120)))    
    
    font = pygame.font.SysFont("comicsansms", int(30 * k))
    text = font.render("PRESS DIGIT N TO START (NxN) GAME", True, (230, 230, 230))
    screen.blit(text, (int(90 + 30 * (1 - k)), int(100 + 150 * k)))
    
    font = pygame.font.SysFont("comicsansms", int(30 * k))
    text = font.render("PRESS F5 TO START RANDOM GAME", True, (230, 230, 230))
    screen.blit(text, (int(90 + 30 * (1 - k)), int(130 + 150 * k)))
    
    pygame.display.update()
    
    num, _Random = 4, False
    while True:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    _Random = True
                    return num, _Random
                if event.key == pygame.K_0:
                    return num, _Random
                if event.key == pygame.K_1:
                    num = 1
                    return num, _Random
                if event.key == pygame.K_2:
                    num = 2
                    return num, _Random
                if event.key == pygame.K_3:
                    num = 3
                    return num, _Random
                if event.key == pygame.K_4:
                    num = 4
                    return num, _Random
                if event.key == pygame.K_5:
                    num = 5
                    return num, _Random
                if event.key == pygame.K_6:
                    num = 6
                    return num, _Random
                if event.key == pygame.K_7:
                    num = 7
                    return num, _Random                
                if event.key == pygame.K_8:
                    num = 8
                    return num, _Random
                if event.key == pygame.K_9:
                    num = 9
                    return num, _Random
    

DEATH = False
def RUN(NUMBER= 4, RANDOM= False):
    W, H = 565, 685
    
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("2048")
    pygame.display.update()    
    
    k = 4/8 * 1.3 #for local customization
    pygame.draw.rect(screen, (0, 0, 128), (int(50), int(100), int(350 * 1.3), int(300 * 1.3)))
    
    font = pygame.font.SysFont("comicsansms", int(60 * k))
    text = font.render("PRESS ANY KEY TO", True, (230, 230, 230))
    screen.blit(text, (int(80), int(120)))    
    
    font = pygame.font.SysFont("comicsansms", int(150 * k))
    text = font.render("START", True, (230, 230, 230))
    screen.blit(text, (int(90 + 30 * (1 - k)), int(120 + 150 * k))) 
    pygame.display.update()
    
    got = False
    while True:       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:   
                NUMBER, RANDOM = start_menu(screen)
                got = 1
        if got:
            break
            
    pygame.display.update()
    
    if RANDOM:
        NUMBER = random.randint(5, 16)

    blocks = NUMBER
    
    #kef = {4:1, 6:0.67, 8:0.5}
    #k = kef[NUMBER] 
    k = 4/NUMBER * 1.3
    
    block_size = int(100 * k)
    margine = int(7 * k)
    W = blocks * (block_size + margine) + margine
    H = W + 120
    
    #reinitilizing screen not to have small black edges
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("2048")
    pygame.display.update()       
    
    title_rect = pygame.Rect(0, 0, W, 100)
    back_rect = pygame.Rect(0, 100, W, H)

    
    k = 4/8 * 1.3 #for local customization
    pygame.draw.rect(screen, (0, 0, 128), (int(50), int(100), int(350 * 1.3), int(300 * 1.3)))
    
    font = pygame.font.SysFont("comicsansms", int(40 * k))
    text = font.render("PRESS ANY KEY TO CONTINUE", True, (230, 230, 230))
    screen.blit(text, (int(80), int(120)))    
    pygame.display.update()
    
    k = 4/NUMBER * 1.3
    

    field = [[0] * blocks for _ in range(blocks)]
    free = []    
    
    
    
    
    
    
    
    CLR = {2:(238, 232, 170), 4:(255, 222, 173), 8:(244, 164, 96), 16:(205, 133, 63), 32:(210, 105, 30), 64:(255, 0, 0), 128:(128, 0, 0), 256:(255, 0, 255), 512:(128, 0, 128), 1024:(0, 0, 255), 2048:(0, 0, 128)}
    ADD = {2:28, 4:28, 8:28, 16:14, 32:10, 64:10 ,128:3, 256:3,}
    SIZE = {1:72, 2:72, 3:56, 4:36, 5:25, 6:10}
    
    if RANDOM:
        CLR = {}
    
    
    for el in ADD:
        ADD[el] = int(ADD[el] * k)
    for el in SIZE:
        SIZE[el] = int(SIZE[el] * k)
        
    started = 0
    add(field)
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                started = 1
                if event.key == pygame.K_LEFT:
                    shift_left(field)
                elif event.key == pygame.K_RIGHT:
                    shift_right(field)
                elif event.key == pygame.K_DOWN:
                    shift_down(field)
                elif event.key == pygame.K_UP:
                    shift_up(field)             
                pygame.draw.rect(screen, (255, 255, 255), title_rect)
                pygame.draw.rect(screen, (169, 169, 169), back_rect) #(47, 79, 79),
                for row in range(blocks):
                    for col in range(blocks):
                        w = col * (block_size + margine) + margine
                        h = row * (block_size + margine) + margine + 110
                        if field[row][col] == 0:
                            colour = (211, 211, 211)
                            pygame.draw.rect(screen, colour, (w, h, block_size, block_size))
                        else:
                            num = field[row][col]
                            if num in CLR:
                                colour = CLR[num]
                            else:
                                colour = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
                                CLR[num] = colour
                                
                            num = str(num)
                            pygame.draw.rect(screen, colour, (w, h, block_size, block_size))
                            font = pygame.font.SysFont("comicsansms", SIZE[len(num)])
                            if int(num) <= 32:
                                num_colour = (139, 69, 19)
                            else:
                                num_colour = (230, 230, 230)
                                
                            if RANDOM:    
                                num_colour = (248, 248, 248)
                                
                            text = font.render(num, True, num_colour)
                            if int(num) in ADD:
                                shift = ADD[int(num)]
                            else:
                                shift = 1
                                
                            screen.blit(text, (w + shift, h))
                            
                   
        if started:
            score += delta[0]
            delta[0] = 0
            font = pygame.font.SysFont("comicsansms", int(45))
            text = "Score:  {}".format(score)
            text = font.render(text, True, (255, 140, 0))
            screen.blit(text, (7, 10)) 

        pygame.display.update()
        #for line in field:
            #if 2048 in line:
                #win()
        
        if DEATH:
            death(screen, score)
            
            
        



if __name__ == "__main__":
    RUN()