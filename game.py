# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Toddler Typing")
clock = pygame.time.Clock()
running = True
dt = 0

a_sound = pygame.mixer.Sound("A.wav")
b_sound = pygame.mixer.Sound("B.wav")

my_font = pygame.font.SysFont('Arial', 600, True)

player_pos = pygame.Vector2((screen.get_width() / 2) - 200, (screen.get_height() / 2) - 300)

paused = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pygame.mixer.Sound.play(a_sound)
            elif event.key == pygame.K_b:
                pygame.mixer.Sound.play(b_sound)
            elif event.key == pygame.K_p:
                paused = not paused
                print(paused)
            elif event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    text_surface = my_font.render('', False, (0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        text_surface = my_font.render('A', False, (0, 0, 0))
    elif keys[pygame.K_b]:
        text_surface = my_font.render('B', False, (0, 0, 0))
    elif keys[pygame.K_c]:
        text_surface = my_font.render('C', False, (0, 0, 0))
    elif keys[pygame.K_d]:
        text_surface = my_font.render('D', False, (0, 0, 0))
    elif keys[pygame.K_e]:
        text_surface = my_font.render('E', False, (0, 0, 0))
    elif keys[pygame.K_f]:
        text_surface = my_font.render('F', False, (0, 0, 0))
    elif keys[pygame.K_g]:
        text_surface = my_font.render('G', False, (0, 0, 0))
    elif keys[pygame.K_h]:
        text_surface = my_font.render('H', False, (0, 0, 0))
    elif keys[pygame.K_i]:
        text_surface = my_font.render('I', False, (0, 0, 0))
    elif keys[pygame.K_j]:
        text_surface = my_font.render('J', False, (0, 0, 0))
    elif keys[pygame.K_k]:
        text_surface = my_font.render('K', False, (0, 0, 0))
    elif keys[pygame.K_l]:
        text_surface = my_font.render('L', False, (0, 0, 0))
    elif keys[pygame.K_m]:
        text_surface = my_font.render('M', False, (0, 0, 0))
    elif keys[pygame.K_n]:
        text_surface = my_font.render('N', False, (0, 0, 0))
    elif keys[pygame.K_o]:
        text_surface = my_font.render('O', False, (0, 0, 0))
    elif keys[pygame.K_p]:
        text_surface = my_font.render('P', False, (0, 0, 0))
    elif keys[pygame.K_q]:
        text_surface = my_font.render('Q', False, (0, 0, 0))
    elif keys[pygame.K_r]:
        text_surface = my_font.render('R', False, (0, 0, 0))
    elif keys[pygame.K_s]:
        text_surface = my_font.render('S', False, (0, 0, 0))
    elif keys[pygame.K_t]:
        text_surface = my_font.render('T', False, (0, 0, 0))
    elif keys[pygame.K_u]:
        text_surface = my_font.render('U', False, (0, 0, 0))
    elif keys[pygame.K_v]:
        text_surface = my_font.render('V', False, (0, 0, 0))
    elif keys[pygame.K_w]:
        text_surface = my_font.render('W', False, (0, 0, 0))
    elif keys[pygame.K_x]:
        text_surface = my_font.render('X', False, (0, 0, 0))
    elif keys[pygame.K_y]:
        text_surface = my_font.render('Y', False, (0, 0, 0))
    elif keys[pygame.K_z]:
        text_surface = my_font.render('Z', False, (0, 0, 0))
    elif keys[pygame.K_0]:
        text_surface = my_font.render('0', False, (0, 0, 0))
    elif keys[pygame.K_1]:
        text_surface = my_font.render('1', False, (0, 0, 0))
    elif keys[pygame.K_2]:
        text_surface = my_font.render('2', False, (0, 0, 0))
    elif keys[pygame.K_3]:
        text_surface = my_font.render('3', False, (0, 0, 0))
    elif keys[pygame.K_4]:
        text_surface = my_font.render('4', False, (0, 0, 0))
    elif keys[pygame.K_5]:
        text_surface = my_font.render('5', False, (0, 0, 0))
    elif keys[pygame.K_6]:
        text_surface = my_font.render('6', False, (0, 0, 0))
    elif keys[pygame.K_7]:
        text_surface = my_font.render('7', False, (0, 0, 0))
    elif keys[pygame.K_8]:
        text_surface = my_font.render('8', False, (0, 0, 0))
    elif keys[pygame.K_9]:
        text_surface = my_font.render('9', False, (0, 0, 0))

    screen.blit(text_surface, player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()