
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
CLICK_RADIUS = 50

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

# Fonts
font = pygame.font.Font(None, 36)

# Click count
click_count = 0

# Sound volume
sound_volume = 100

# Fullscreen
fullscreen = False

# Cheats
cheat_code = ""
cheat_active = False

# Main Menu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_button_rect.collidepoint(x, y):
                    game()
                elif options_button_rect.collidepoint(x, y):
                    options_menu()
                elif exit_button_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        start_button_rect = pygame.draw.rect(screen, (0, 255, 0), (300, 200, 200, 50))
        options_button_rect = pygame.draw.rect(screen, (0, 0, 255), (300, 300, 200, 50))
        exit_button_rect = pygame.draw.rect(screen, (255, 0, 0), (300, 400, 200, 50))

        start_text = font.render("Start Game", True, (0, 0, 0))
        options_text = font.render("Options", True, (0, 0, 0))
        exit_text = font.render("Exit", True, (0, 0, 0))

        screen.blit(start_text, (330, 210))
        screen.blit(options_text, (330, 310))
        screen.blit(exit_text, (330, 410))

        pygame.display.flip()

# Game Loop
def game():
    global click_count
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x < CLICK_RADIUS and y < CLICK_RADIUS:
                    if cheat_active and cheat_code == "BULKME":
                        click_count += 20
                    else:
                        click_count += 1

        screen.fill(WHITE)

        click_text = font.render("Clicks: " + str(click_count), True, (0, 0, 0))
        screen.blit(click_text, (10, 10))

        pygame.display.flip()

# Options Menu
def options_menu():
    global sound_volume, fullscreen, cheat_active, cheat_code
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if volume_up_button_rect.collidepoint(x, y):
                    sound_volume = min(sound_volume + 10, 100)
                elif volume_down_button_rect.collidepoint(x, y):
                    sound_volume = max(sound_volume - 10, 0)
                elif fullscreen_toggle_rect.collidepoint(x, y):
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
                elif cheat_toggle_rect.collidepoint(x, y):
                    cheat_active = not cheat_active
                elif quit_button_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()
                elif back_button_rect.collidepoint(x, y):
                    main_menu()

        screen.fill(WHITE)
        volume_up_button_rect = pygame.draw.rect(screen, (0, 255, 0), (300, 200, 200, 50))
        volume_down_button_rect = pygame.draw.rect(screen, (255, 0, 0), (300, 300, 200, 50))
        fullscreen_toggle_rect = pygame.draw.rect(screen, (0, 0, 255), (300, 400, 200, 50))
        cheat_toggle_rect = pygame.draw.rect(screen, (255, 255, 0), (300, 500, 200, 50))
        quit_button_rect = pygame.draw.rect(screen, (255, 0, 0), (300, 600, 200, 50))
        back_button_rect = pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 50))

        volume_up_text = font.render("Volume Up", True, (0, 0, 0))
        volume_down_text = font.render("Volume Down", True, (0, 0, 0))
        fullscreen_text = font.render("Fullscreen: " + str(fullscreen), True, (0, 0, 0))
        cheat_toggle_text = font.render("Cheats: " + str(cheat_active), True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))
        back_text = font.render("Back", True, (0, 0, 0))

        cheat_code_input = font.render("Cheat Code: " + cheat_code, True, (0, 0, 0))

        screen.blit(volume_up_text, (330, 210))
        screen.blit(volume_down_text, (330, 310))
        screen.blit(fullscreen_text, (330, 410))
        screen.blit(cheat_toggle_text, (330, 510))
        screen.blit(quit_text, (330, 610))
        screen.blit(back_text, (10, 10))
        screen.blit(cheat_code_input, (330, 550))

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()


