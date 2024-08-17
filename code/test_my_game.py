import pytest
import pygame
from unittest.mock import MagicMock, patch
from project import draw_floor, update_scrolling_speed, reset_game, spawn_cactus, cacti, cactus_spawn_delay, last_cactus_spawn

@pytest.fixture
def setup_pygame():
    pygame.init()
    screen = pygame.Surface((320, 240))  
    return screen

def test_draw_floor(setup_pygame):
    screen = setup_pygame
    floor_tile = pygame.Surface((34, 16))  
    floor_tile.fill((255, 0, 0))  
    floor_pos = 0
    floor_speed = 2
    screen_width = 320
    screen_height = 240
    new_floor_pos = draw_floor(screen, floor_tile, floor_pos, floor_speed, screen_width, screen_height)
    expected_floor_pos = floor_pos - floor_speed
    if expected_floor_pos <= -floor_tile.get_width():
        expected_floor_pos = 0
    
    assert new_floor_pos == expected_floor_pos

def test_update_scrolling_speed():
    score = 10
    base_speeds = [0.5, 1, 2, 2, 2.5]
    scaling_factor = 0.05
    expected_speeds = [int(base_speed + score * scaling_factor) for base_speed in base_speeds]
    speeds = update_scrolling_speed(score)
    assert speeds == expected_speeds

def test_spawn_cactus():
    global cacti, last_cactus_spawn, cactus_spawn_delay
    cacti = []
    last_cactus_spawn = pygame.time.get_ticks() - cactus_spawn_delay
    cactus_spawn_delay = 1000  
    assert len(cacti) == 1
    cactus = cacti[0]
    assert cactus.x > 320 
    assert cactus.y == floor_y - 12  
if __name__ == "__main__":
    pytest.main()
