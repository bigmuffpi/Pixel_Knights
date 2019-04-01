import pygame
import player1

def draw_player(screen, bg, x, y, height, width):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    pygame.display.update()
    screen.blit(bg, [0, 0])

def get_coor(screen, myfont, x, y):
    coord = str(x) + "/"+ str(y)
    textsurface = myfont.render(coord, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))

def init_music():
    pygame.mixer.music.load("bgmusic.wav")
    pygame.mixer.music.set_volume(.5)

def play_music():
    pygame.mixer.music.play(-1)

def main():

    #init pygame, sounds/music, images
    pygame.init()
    init_music()
    play_music()
    sword_sound = pygame.mixer.Sound("swordwav.wav")
    screen = pygame.display.set_mode((500, 500))
    bg = pygame.image.load("grass.png")
    screen.blit(bg, [0,0])
    sword = pygame.image.load("sword.png")
    sword = pygame.transform.scale(sword, (50, 50))

    #player properties
    x=50
    y=50
    pHeight = 60
    pWidth = 40
    speed = 5
    p_dir = 'r'

    #initialize player
    protag = player1.Player(screen, [0,0,0], x, y, pHeight, pWidth, speed, p_dir)
    swrd_dly = 0

    #debug info to display player coordinates
    pygame.font.init()
    myfont = pygame.font.SysFont('Garamond', 15)
    disp_coor = False

    running = True

    # main loop
    while running:
        pygame.time.delay(33)

        #redraws the player every cycle
        draw_player(protag.window_, bg, protag.xPos_, protag.yPos_, protag.height_, protag.width_)

        #need to add cooldown so debug isnt spammed
        if disp_coor:
            get_coor(screen, myfont, protag.xPos_, protag.yPos_)

        #makes sure sword isnt spammed
        if swrd_dly > 0:
            swrd_dly=swrd_dly-1

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        key = pygame.key.get_pressed()

        #movement block
        if key[pygame.K_RIGHT] and protag.xPos_<460:
            protag.xPos_=protag.xPos_+protag.speed_
            protag.dir_ = 'r'
        if key[pygame.K_LEFT] and protag.xPos_>0:
            protag.xPos_=protag.xPos_-protag.speed_
            protag.dir_ = 'l'
        if key[pygame.K_UP] and protag.yPos_>0:
            protag.yPos_=protag.yPos_-protag.speed_
            protag.dir_ = 'u'
        if key[pygame.K_DOWN] and protag.yPos_<440:
            protag.yPos_=protag.yPos_+protag.speed_
            protag.dir_ = 'd'

         #checking for attack
        if key[pygame.K_SPACE] and swrd_dly==0:
            pygame.mixer.Sound.play(sword_sound)

            #makes sure sword corresponds to player's direction
            if protag.dir_ == 'r':
                screen.blit(sword, [protag.xPos_+50, protag.yPos_+15])
            if protag.dir_ == 'l':
                screen.blit(pygame.transform.rotate(sword, 180), [protag.xPos_-55, protag.yPos_+20])
            if protag.dir_ == 'u':
                screen.blit(pygame.transform.rotate(sword, 90), [protag.xPos_, protag.yPos_-55])
            if protag.dir_ == 'd':
                screen.blit(pygame.transform.rotate(sword, 270), [protag.xPos_, protag.yPos_+65])

            #adds some delay so sword isnt spammed
            swrd_dly = 15

        #init debug coordinates
        if key[pygame.K_BACKSPACE]:
            disp_coor = not disp_coor

main()
