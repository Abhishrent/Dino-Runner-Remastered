import pygame
from os.path import join

def draw_scrolling_background(screen, bg, bg_x, speed):
    repeats = screen.get_width() // bg.get_width() + 2
    for i in range(repeats):
        screen.blit(bg, (bg_x + i * bg.get_width(), 0))
    bg_x -= speed
    if bg_x <= -bg.get_width():
        bg_x += bg.get_width()
    return bg_x

def main():
    pygame.init()

    global WIDTH, HEIGHT
    WIDTH, HEIGHT = 320, 240
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Background Only")

    # Load images
    sky = pygame.image.load(join('sprites', 'world', 'sky.png')).convert_alpha()
    bg1 = pygame.image.load(join('sprites', 'world', 'bg1.png')).convert_alpha()
    bg2 = pygame.image.load(join('sprites', 'world', 'bg2.png')).convert_alpha()
    bg3 = pygame.image.load(join('sprites', 'world', 'bg3.png')).convert_alpha()
    bg4 = pygame.image.load(join('sprites', 'world', 'bg4.png')).convert_alpha()
    bg5 = pygame.image.load(join('sprites', 'world', 'bg5.png')).convert_alpha()

    # Initialize background positions and speeds
    bg_x_sky, bg_x1, bg_x2, bg_x3, bg_x4, bg_x5 = 0, 0, 0, 0, 0, 0
    bg_speed_sky, bg_speed1, bg_speed2, bg_speed3, bg_speed4, bg_speed5 = 0, 0.5, 1, 2, 2, 2.5

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)

        screen.fill((0, 0, 0))  # Clear screen to black before drawing backgrounds

        # Draw and update sky
        screen.blit(sky, (bg_x_sky, 0))

        # Draw and update scrolling backgrounds
        bg_x1 = draw_scrolling_background(screen, bg1, bg_x1, bg_speed1)
        bg_x2 = draw_scrolling_background(screen, bg2, bg_x2, bg_speed2)
        bg_x3 = draw_scrolling_background(screen, bg3, bg_x3, bg_speed3)
        bg_x4 = draw_scrolling_background(screen, bg4, bg_x4, bg_speed4)
        bg_x5 = draw_scrolling_background(screen, bg5, bg_x5, bg_speed5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
