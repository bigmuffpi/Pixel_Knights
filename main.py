import pygame
import player1

pygame.init()

def draw_player(screen, bg, x, y):
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 60))
    pygame.display.update()
    screen.blit(bg, [0, 0])
def main():
    screen = pygame.display.set_mode((500, 500))
    x=50
    y=50
    speed = 5
    bg = pygame.image.load("grass.png")
    sword = pygame.image.load("sword.png")
    sword = pygame.transform.scale(sword, (50,50))
    running = True
    screen.blit(bg, [0,0])
    p_dir = 'r'
    # main loop
    while running:
        pygame.time.delay(25)
        draw_player(screen, bg, x, y)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] and x<460:
            x=x+speed
            #screen.blit(bg, [0, 0])
            pygame.draw.rect(screen, (0, 0, 0), (x,y, 40, 60))
            p_dir = 'r'
        if key[pygame.K_LEFT] and x>0:
            x=x-speed
            screen.blit(bg, [0, 0])
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 60))
            p_dir = 'l'
        if key[pygame.K_UP] and y>0:
            y=y-speed
            #screen.blit(bg, [0, 0])
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 60))
            p_dir = 'u'
        if key[pygame.K_DOWN] and y<440:
            y=y+speed
            #screen.blit(bg, [0, 0])
            p_dir = 'd'
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 60))
        if key[pygame.K_SPACE]:
            #screen.blit(bg, [0, 0])

            if p_dir == 'r':
                screen.blit(sword, [x+50, y+15])
            if p_dir == 'l':
                screen.blit(pygame.transform.rotate(sword, 180), [x-55, y+20])
            if p_dir == 'u':
                screen.blit(pygame.transform.rotate(sword, 90), [x, y-55])
            if p_dir == 'd':
                screen.blit(pygame.transform.rotate(sword, 270), [x, y+65])


main()