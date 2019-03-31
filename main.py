import pygame
import player1

def draw_player(screen, bg, x, y, height, width):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, height, width))
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

    pygame.init()

    init_music()

    sword_sound = pygame.mixer.Sound("swordwav.wav")
    
    screen = pygame.display.set_mode((500, 500))
    x=50
    y=50

    pHeight = 60
    pWidth = 40

    speed = 5
    swrd_dly = 0
    bg = pygame.image.load("grass.png")
    sword = pygame.image.load("sword.png")
    sword = pygame.transform.scale(sword, (50,50))
    running = True
    screen.blit(bg, [0,0])
    p_dir = 'r'
    player = pygame.Rect(x, y, pHeight, pWidth)

    #draw text
    pygame.font.init()
    myfont = pygame.font.SysFont('Garamond', 15)

    #debug coordinates
    disp_coor = False

    play_music()

    # main loop
    while running:
        pygame.time.delay(33)
        
        draw_player(screen, bg, player.x, player.y, player.height, player.width)

        if disp_coor:
            get_coor(screen, myfont, player.x, player.y)

        if swrd_dly > 0:
            swrd_dly=swrd_dly-1

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and player.x<460:
            player.x=player.x+speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)

            p_dir = 'r'
        if key[pygame.K_LEFT] and player.x>0:
            player.x=player.x-speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'l'
        if key[pygame.K_UP] and player.y>0:
            player.y=player.y-speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'u'
        if key[pygame.K_DOWN] and player.y<440:
            player.y=player.y+speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'd'
        if key[pygame.K_SPACE] and swrd_dly==0:
            pygame.mixer.Sound.play(sword_sound)
            if p_dir == 'r':
                screen.blit(sword, [player.x+50, player.y+15])
            if p_dir == 'l':
                screen.blit(pygame.transform.rotate(sword, 180), [player.x-55, player.y+20])
            if p_dir == 'u':
                screen.blit(pygame.transform.rotate(sword, 90), [player.x, player.y-55])
            if p_dir == 'd':
                screen.blit(pygame.transform.rotate(sword, 270), [player.x, player.y+65])
            swrd_dly = 15
        if key[pygame.K_BACKSPACE]:
            disp_coor = not disp_coor

main()
