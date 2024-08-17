import pygame
from sprite import SpriteSheet
from os.path import join
import random
import time

# Global variables
screen = None
sprite_obj = None
game_paused = False
game_started = False
game_over = False
scroll = 0
frame_count = 0
last_cactus_spawn = None
cactus_spawn_delay = 2000
cacti = []
bg_x1 = 0
bg_speed1 = 0.5
bg_x2 = 0
bg_speed2 = 1
bg_x3 = 0
bg_speed3 = 2
bg_x4 = 0
bg_speed4 = 2
bg_x5 = 0
bg_speed5 = 2.5
floor_pos = 0
floor_speed = 2
floor_y = None
score = 0
jump = False
jump_velocity = 0
player_pos_y = None
player_rect = None
gravity = 0.5
base_delay = 100
delay_decrease_per_point = 0.6
min_delay = 10
black = (0, 0, 0)
font_name = None
text_color = (255, 255, 255)
animation_list = []
animation_steps = [4, 6, 4, 3, 7]
action = 0
last_update = None
animation_delay = 50
frame = 0
step_counter = 0

def draw_text(text, font, color, x, y):
    global screen
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def draw_floor(screen, floor_tile, floor_pos, floor_speed, screen_width, screen_height):
    for x in range(int(floor_pos), screen_width, floor_tile.get_width()):
        screen.blit(floor_tile, (x, screen_height - floor_tile.get_height()))
    floor_pos -= floor_speed
    if floor_pos <= -floor_tile.get_width():
        floor_pos = 0
    return floor_pos

def draw_scrolling_background(screen, bg, bg_x, speed):
    repeats = screen.get_width() // bg.get_width() + 2
    for i in range(repeats):
        screen.blit(bg, (bg_x + i * bg.get_width(), 0))
    bg_x -= speed
    if bg_x <= -bg.get_width():
        bg_x += bg.get_width()
    return bg_x

def update_scrolling_speed(score):
    base_speeds = [0.5, 1, 2, 2, 2.5]
    scaling_factor = 0.05
    speeds = [base_speed + score * scaling_factor for base_speed in base_speeds]
    return [int(speed) for speed in speeds]  # Ensure speeds are integers

def pause_game():
    global game_paused
    game_paused = True
    while game_paused:
        draw_text("Game Paused \nPress ENTER to continue", font_name, text_color, WIDTH // 2 - 60, HEIGHT // 2 - 10)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_paused = False

class Cactus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = cactus  # Use the cactus image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))  # Create a rect for collision detection

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self, speed):
        self.x -= speed
        self.rect.x = self.x  # Update rect position

def spawn_cactus():
    global last_cactus_spawn, cactus_spawn_delay
    current_time = pygame.time.get_ticks()
    if current_time - last_cactus_spawn >= cactus_spawn_delay:
        last_cactus_spawn = current_time
        x_pos = WIDTH + random.randint(0, 50)  # Randomize starting position within the screen width
        y_pos = floor_y - cactus.get_height() + 12 # Position cactus on the floor
        cacti.append(Cactus(x_pos, y_pos))
        cactus_spawn_delay = max(1000, cactus_spawn_delay - 10)  # Decrease delay, min 1000ms

def update_cacti(speed):
    for cactus in cacti[:]:
        cactus.update(speed)
        if cactus.x < -cactus.image.get_width():
            cacti.remove(cactus)

def draw_cacti():
    for cactus in cacti:
        cactus.draw(screen)

def check_collision(player_rect, cacti):
    for cactus in cacti:
        if player_rect.colliderect(cactus.rect):
            return True
    return False

def reset_game():
    global game_started, game_over, score, cacti, player_pos_y, jump, jump_velocity
    game_started = False
    game_over = False
    score = 0
    cacti.clear()
    player_pos_y = floor_y - 24
    jump = False
    jump_velocity = 0

def game_overf():
    global game_over
    game_over = True
    while game_over:
        screen.fill(black)
        draw_text("GAME OVER", font_name, text_color, WIDTH // 2 - 20, HEIGHT // 2 - 10)
        draw_text("Press ENTER to restart", font_name, text_color, WIDTH // 2 - 60, HEIGHT // 2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_game()
                    return

def main():
    global screen, sprite_obj, game_paused, game_started, game_over, scroll, frame_count, last_cactus_spawn, cactus_spawn_delay, cacti
    global bg_x1, bg_speed1, bg_x2, bg_speed2, bg_x3, bg_speed3, bg_x4, bg_speed4, bg_x5, bg_speed5
    global floor_pos, floor_speed, floor_y, score, jump, jump_velocity, player_pos_y, player_rect, gravity
    global base_delay, delay_decrease_per_point, min_delay, black, font_name, text_color
    global animation_list, animation_steps, action, last_update, animation_delay, frame, step_counter

    pygame.init()

    #------------------------------------------------------------VARIABLES---------------------------------------------------
    global WIDTH, HEIGHT  # Declare global variables
    WIDTH, HEIGHT = 320, 240
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Runner")

    global sprite_obj
    sprite_sheet = pygame.image.load(join('sprites', 'player', 'doux.png'))
    sprite_obj = SpriteSheet(sprite_sheet)

    global sky, bg1, bg2, bg3, bg4, bg5, cactus, small_cactus, floor, floor_tile
    sky = pygame.image.load(join('sprites', 'world', 'sky.png')).convert_alpha()
    bg1 = pygame.image.load(join('sprites', 'world', 'bg1.png')).convert_alpha()
    bg2 = pygame.image.load(join('sprites', 'world', 'bg2.png')).convert_alpha()
    bg3 = pygame.image.load(join('sprites', 'world', 'bg3.png')).convert_alpha()
    bg4 = pygame.image.load(join('sprites', 'world', 'bg4.png')).convert_alpha()
    bg5 = pygame.image.load(join('sprites', 'world', 'bg5.png')).convert_alpha()
    cactus = pygame.image.load(join('sprites', 'world', 'cactus.png')).convert_alpha()
    small_cactus = pygame.image.load(join('sprites', 'world', 'cactus_small.png')).convert_alpha()
    floor = pygame.image.load(join('sprites', 'world', 'floor.png')).convert_alpha()
    floor_tile = floor.subsurface(pygame.Rect(38, 0, 34, 16))

    global floor_y, player_pos_y, player_rect, last_cactus_spawn, cactus_spawn_delay, cacti
    floor_y = HEIGHT - 16
    player_pos_y = floor_y - 24
    player_rect = pygame.Rect(10, player_pos_y, 24, 24)
    last_cactus_spawn = pygame.time.get_ticks()

    global font_name, text_color, animation_list, animation_steps, action, last_update, animation_delay, frame, step_counter
    font_name = pygame.font.SysFont("consolas", 10)
    text_color = (255, 255, 255)

    animation_list = []
    animation_steps = [4, 6, 4, 3, 7]
    action = 0
    last_update = pygame.time.get_ticks()
    animation_delay = 50
    frame = 0
    step_counter = 0

    for animation in animation_steps:
        temp_list = []
        for _ in range(animation):
            temp_list.append(sprite_obj.get_player_surf(step_counter, 24, 24, 1.5, black))
            step_counter += 1
        animation_list.append(temp_list)

    # Game loop
    running = True
    while running:
        pygame.time.Clock().tick(60)

        if game_started:
            animation_delay = max(base_delay - score * delay_decrease_per_point, min_delay)

        if game_started:
            speeds = update_scrolling_speed(score)
            bg_speed1, bg_speed2, bg_speed3, bg_speed4, bg_speed5 = speeds
            floor_speed = bg_speed5

            spawn_cactus()
            update_cacti(floor_speed)

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_delay:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list[action]):
                frame = 0

        screen.blit(sky, (0, 0))
        screen.blit(bg1, (bg_x1, 0))
        screen.blit(bg2, (bg_x2, 0))
        screen.blit(bg3, (bg_x3, 0))
        screen.blit(bg4, (bg_x4, 0))
        screen.blit(bg5, (bg_x5, 0))

        if game_started and not game_over:
            bg_x1 = draw_scrolling_background(screen, bg1, bg_x1, bg_speed1)
            bg_x2 = draw_scrolling_background(screen, bg2, bg_x2, bg_speed2)
            bg_x3 = draw_scrolling_background(screen, bg3, bg_x3, bg_speed3)
            bg_x4 = draw_scrolling_background(screen, bg4, bg_x4, bg_speed4)
            bg_x5 = draw_scrolling_background(screen, bg5, bg_x5, bg_speed5)
            floor_pos = draw_floor(screen, floor_tile, floor_pos, floor_speed, WIDTH, HEIGHT)

        if game_started and not game_paused and not game_over:
            frame_count += 1
            if frame_count >= 60:
                score += 1
                frame_count = 0

        if game_started:
            draw_text("Score: " + str(score), font_name, text_color, 10, 10)

        if not game_started:
            screen.fill(black)
            draw_text("Press any key to start", font_name, text_color, WIDTH // 2 - 60, HEIGHT // 2 - 10)
            action = 0  

        screen.blit(animation_list[action][frame], (10, player_pos_y))
        player_rect.y = player_pos_y

        if game_started and not game_over:
            draw_cacti()

        if game_started and not game_over and check_collision(player_rect, cacti):    
            time.sleep(2)
            game_overf()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_over:
                    game_overf()
                else:
                    game_started = True
                    if event.key == pygame.K_ESCAPE:
                        pause_game()
                    if event.key == pygame.K_SPACE and not jump:
                        action = 2
                        jump = True
                        jump_velocity = -10
                        frame = 0
                    if event.key == pygame.K_DOWN:
                        action = 4
                        frame = 0
            else:
                action = 1
                frame = 0

        if jump:
            player_pos_y += jump_velocity
            jump_velocity += gravity
            if player_pos_y >= floor_y - 24:
                player_pos_y = floor_y - 24
                jump = False
                jump_velocity = 0
                action = 1

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
