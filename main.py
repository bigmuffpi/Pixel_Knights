import pygame
import player1

pygame.init()

def draw_player(screen, bg, x, y, height, width):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, height, width))
    pygame.display.update()
    screen.blit(bg, [0, 0])
def main():
    screen = pygame.display.set_mode((500, 500))
    x=50
    y=50

    pHeight = 60
    pWidth = 40

    speed = 5
    bg = pygame.image.load("grass.png")
    sword = pygame.image.load("sword.png")
    sword = pygame.transform.scale(sword, (50,50))
    running = True
    screen.blit(bg, [0,0])
    p_dir = 'r'
    player = pygame.Rect(x, y, pHeight, pWidth)

    #draw text
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 15)

    # main loop
    while running:
        pygame.time.delay(25)
        coord = str(player.x) + "/"+ str(player.y)
        textsurface = myfont.render(coord, False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
        draw_player(screen, bg, player.x, player.y, player.height, player.width)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and x<460:
            player.x=player.x+speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)

            p_dir = 'r'
        if key[pygame.K_LEFT] and x>0:
            player.x=player.x-speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'l'
        if key[pygame.K_UP] and y>0:
            player.y=player.y-speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'u'
        if key[pygame.K_DOWN] and y<440:
            player.y=player.y+speed
            #draw_player(screen, bg, player.x, player.y, player.height, player.width)
            p_dir = 'd'
        if key[pygame.K_SPACE]:
            if p_dir == 'r':
                screen.blit(sword, [player.x+50, player.y+15])
            if p_dir == 'l':
                screen.blit(pygame.transform.rotate(sword, 180), [player.x-55, player.y+20])
            if p_dir == 'u':
                screen.blit(pygame.transform.rotate(sword, 90), [player.x, player.y-55])
            if p_dir == 'd':
                screen.blit(pygame.transform.rotate(sword, 270), [player.x, player.y+65])



main()