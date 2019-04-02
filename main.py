'''
THINGS TO DO

use variables instead of hardcoded numbers, e.g. window size, colors, etc.

fix height and width being backwards

get stuff into functions and classes

merge player1 and enemy classes?


'''


import pygame
import player1
import enemy

def draw_objects(obj_list, screen, bg):
    for i in range(0, len(obj_list)):
        pygame.draw.rect(screen, (0, 0, 0), (obj_list[i].xPos_, obj_list[i].yPos_, obj_list[i].width_, obj_list[i].height_))
    pygame.display.update()
    screen.blit(bg, [0, 0])

def draw_player(screen, bg, x, y, height, width):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    pygame.display.update()
    screen.blit(bg, [0, 0])

def enemy_path(x, speed, dir):
    if dir:
        newX = x-speed
    else:
        newX = x+speed
    return newX

def get_coor(screen, myfont, x, y):
    coord = str(x) + "/"+ str(y)
    textsurface = myfont.render(coord, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))

def init_music():
    pygame.mixer.music.load("bgmusic.wav")
    pygame.mixer.music.set_volume(.5)

def play_music():
    pygame.mixer.music.play(-1)

def draw_x(screen):

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    for i in range(0, 500, 5):
        pygame.draw.line(screen, (255, 0,0), [0, x2], [500, y2])
        x2 = x2+5
        y2 = y2+5

def draw_y(screen):

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for i in range(0, 500, 5):
        pygame.draw.line(screen, (255,0,0), [x1, 0], [y1, 500])
        x1 = x1+5
        y1 = y1+5

def main():

    # init pygame, sounds/music, images
    pygame.init()
    init_music()
    play_music()
    sword_sound = pygame.mixer.Sound("swordwav.wav")
    screen = pygame.display.set_mode((500, 500))
    bg = pygame.image.load("grass.png")
    screen.blit(bg, [0,0])
    sword = pygame.image.load("sword.png")
    sword = pygame.transform.scale(sword, (50, 50))
    enemy_sprite = pygame.image.load("enemy.jpg")
    enemy_sprite = pygame.transform.scale(enemy_sprite, (50,250))

    # player properties
    x=50
    y=50
    pHeight = 60
    pWidth = 40
    speed = 5
    p_dir = 'r'

    # initialize player
    protag = player1.Player(screen, [0,0,0], x, y, pHeight, pWidth, speed, p_dir)
    swrd_dly = 0
    swrd_out = False
    p_rect = pygame.Rect(protag.xPos_, protag.yPos_, protag.width_, protag.height_)

    # adding enemy
    antag = enemy.Enemy(screen, [255,0,0], 410, 250, 250, 50, speed, p_dir)
    a_rect = pygame.Rect(antag.xPos_, antag.yPos_, antag.width_, antag.height_)
    a_dir = True

    # debug info to display player coordinates
    pygame.font.init()
    myfont = pygame.font.SysFont('Garamond', 15)
    debug_en = False

    # obj_list = [protag, antag]
    # test for enemy image, no need to draw rect
    obj_list = [protag]
    running = True

    # main loop
    while running:
        pygame.time.delay(33)

        # time for slow test
        # pygame.time.delay(100)

        # draw list of objects rather than each object individually
        draw_objects(obj_list, screen, bg)

        # check if debug enabled to display stats
        if debug_en:
            # draw grid, 5x5 pixels
            draw_x(screen)
            draw_y(screen)

            # display player coordinates
            get_coor(screen, myfont, protag.xPos_, protag.yPos_)

        # makes sure sword isnt spammed
        if swrd_dly > 0:
            swrd_dly=swrd_dly-1

        # move teh enemy
        antag.yPos_ = enemy_path(antag.yPos_, antag.speed_, a_dir)
        screen.blit(enemy_sprite, [antag.xPos_, antag.yPos_])

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        key = pygame.key.get_pressed()

        #check collision
        if p_rect.colliderect(a_rect):
            print("we lost")

        # movement block
        if key[pygame.K_RIGHT] and protag.xPos_<460:
            protag.xPos_=protag.xPos_+protag.speed_
            if not key[pygame.K_SPACE]:     # we dont want a turn when attack is being held
                protag.dir_ = 'r'
        if key[pygame.K_LEFT] and protag.xPos_>0:
            protag.xPos_=protag.xPos_-protag.speed_
            if not key[pygame.K_SPACE]:
                protag.dir_ = 'l'
        if key[pygame.K_UP] and protag.yPos_>0:
            protag.yPos_=protag.yPos_-protag.speed_
            if not key[pygame.K_SPACE]:
                protag.dir_ = 'u'
        if key[pygame.K_DOWN] and protag.yPos_<440:
            protag.yPos_=protag.yPos_+protag.speed_
            if not key[pygame.K_SPACE]:
                protag.dir_ = 'd'

        # checking for attack and controlling cooldown
        if not key[pygame.K_SPACE] and swrd_out == True:
            swrd_dly = 15
            swrd_out = False


        if key[pygame.K_SPACE] and swrd_dly==0:
            # play sword sound
            if swrd_out == False:
                pygame.mixer.Sound.play(sword_sound)

            # makes sure sword corresponds to player's direction
            if protag.dir_ == 'r':
                screen.blit(sword, [protag.xPos_+50, protag.yPos_+15])
            if protag.dir_ == 'l':
                screen.blit(pygame.transform.rotate(sword, 180), [protag.xPos_-55, protag.yPos_+20])
            if protag.dir_ == 'u':
                screen.blit(pygame.transform.rotate(sword, 90), [protag.xPos_, protag.yPos_-55])
            if protag.dir_ == 'd':
                screen.blit(pygame.transform.rotate(sword, 270), [protag.xPos_, protag.yPos_+65])

            # adds some delay so sword isnt spammed
            swrd_out = True


        # update player
        p_rect.x = protag.xPos_
        p_rect.y = protag.yPos_

        # check enemy direction and flip if ncessary
        a_rect.y = antag.yPos_

        if a_rect.y == 90:
            a_dir = False
        if a_rect.y == 410:
            a_dir = True

        # init debug
        if key[pygame.K_BACKSPACE]:
            debug_en = not debug_en

main()
