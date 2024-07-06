from datetime import datetime
import logging
import os
import time

from datetime import datetime

import pygame

exe_path = os.path.dirname(os.path.realpath(__file__))

# Format the current date and time as YYYYMMDDHHMISS
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

log_filename = f'{exe_path}/game_{timestamp}.log'

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename=log_filename, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Toddler Typing")
clock = pygame.time.Clock()
running = True
dt = 0

last_escape_press_time = 0
double_press_threshold = 0.25

# my_font = pygame.font.SysFont('Arial', 600, True)
my_font = pygame.font.SysFont('Arial', 1200, True)

key_data = {
    # Alphabet
    pygame.K_a: {"text": 'A', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/A.ogg")},
    pygame.K_b: {"text": 'B', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/B.ogg")},
    pygame.K_c: {"text": 'C', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/C.ogg")},
    pygame.K_d: {"text": 'D', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/D.ogg")},
    pygame.K_e: {"text": 'E', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/E.ogg")},
    pygame.K_f: {"text": 'F', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/F.ogg")},
    pygame.K_g: {"text": 'G', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/G.ogg")},
    pygame.K_h: {"text": 'H', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/H.ogg")},
    pygame.K_i: {"text": 'I', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/I.ogg")},
    pygame.K_j: {"text": 'J', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/J.ogg")},
    pygame.K_k: {"text": 'K', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/K.ogg")},
    pygame.K_l: {"text": 'L', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/L.ogg")},
    pygame.K_m: {"text": 'M', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/M.ogg")},
    pygame.K_n: {"text": 'N', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/N.ogg")},
    pygame.K_o: {"text": 'O', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/O.ogg")},
    pygame.K_p: {"text": 'P', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/P.ogg")},
    pygame.K_q: {"text": 'Q', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/Q.ogg")},
    pygame.K_r: {"text": 'R', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/R.ogg")},
    pygame.K_s: {"text": 'S', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/S.ogg")},
    pygame.K_t: {"text": 'T', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/T.ogg")},
    pygame.K_u: {"text": 'U', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/U.ogg")},
    pygame.K_v: {"text": 'V', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/V.ogg")},
    pygame.K_w: {"text": 'W', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/W.ogg")},
    pygame.K_x: {"text": 'X', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/X.ogg")},
    pygame.K_y: {"text": 'Y', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/Y.ogg")},
    pygame.K_z: {"text": 'Z', "sound": pygame.mixer.Sound(f"{exe_path}/assets/letters/Z.ogg")},
    # Numbers
    pygame.K_0: {"text": '0', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/0.ogg")},
    pygame.K_1: {"text": '1', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/1.ogg")},
    pygame.K_2: {"text": '2', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/2.ogg")},
    pygame.K_3: {"text": '3', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/3.ogg")},
    pygame.K_4: {"text": '4', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/4.ogg")},
    pygame.K_5: {"text": '5', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/5.ogg")},
    pygame.K_6: {"text": '6', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/6.ogg")},
    pygame.K_7: {"text": '7', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/7.ogg")},
    pygame.K_8: {"text": '8', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/8.ogg")},
    pygame.K_9: {"text": '9', "sound": pygame.mixer.Sound(f"{exe_path}/assets/numbers/9.ogg")},
    # Misc
    pygame.K_UP: {"text": '↑', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/UP.ogg")},
    pygame.K_DOWN: {"text": '↓', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/DOWN.ogg")},
    pygame.K_LEFT: {"text": '←', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/LEFT.ogg")},
    pygame.K_RIGHT: {"text": '→', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/RIGHT.ogg")},
    pygame.K_RETURN: {"text": '←', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/LEFT.ogg")},
    pygame.K_BACKSPACE: {"text": '←', "sound": pygame.mixer.Sound(f"{exe_path}/assets/misc/LEFT.ogg")},
    # pygame.K_SLASH: {"text": '/', "sound": pygame.mixer.Sound(f"{path}/assets/misc/SLASH.ogg")},
    # pygame.K_BACKSLASH: {"text": '\\', "sound": pygame.mixer.Sound(f"{path}/assets/misc/BACKSLASH.ogg")},
    # pygame.K_LCTRL: {"text": 'CTRL', "sound": pygame.mixer.Sound(f"{path}/assets/misc/CTRL.ogg")},
    # pygame.K_RCTRL: {"text": 'CTRL', "sound": pygame.mixer.Sound(f"{path}/assets/misc/CTRL.ogg")},
    # pygame.K_LALT: {"text": 'ALT', "sound": pygame.mixer.Sound(f"{path}/assets/misc/ALT.ogg")},
    # pygame.K_RALT: {"text": 'ALT', "sound": pygame.mixer.Sound(f"{path}/assets/misc/ALT.ogg")},
}

while running:
    keys = pygame.key.get_pressed()

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            logging.debug(f"Key pressed: {event.key} {event.unicode}")
            if event.key in key_data:
                if key_data[event.key]["sound"]:
                    pygame.mixer.Sound.play(key_data[event.key]["sound"])
            elif event.key == pygame.K_DELETE:
                current_time = time.time()

                if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                    if (current_time - last_escape_press_time) < double_press_threshold:
                        # Double press detected with Ctrl held down
                        running = False

                last_escape_press_time = current_time

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("pink")

    for key, char in key_data.items():
        if keys[key]:
            text_surface = my_font.render(char['text'], False, 'black')
            break
    else:
        # Render empty if no relevant key is pressed
        text_surface = my_font.render('', False, 'black')

    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_surface, text_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
