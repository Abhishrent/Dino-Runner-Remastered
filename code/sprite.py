import pygame

class SpriteSheet():
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
    
    # A function to get the individual frame of the player from the sprite sheet
    def get_player_surf(self, frame_no, w, h, scale, color):
        player_surf = pygame.Surface((w, h), pygame.SRCALPHA).convert_alpha()
        player_surf.blit(self.sprite_sheet, (0, 0), (frame_no * w, 0, w, h))
        player_surf = pygame.transform.scale(player_surf, (int(w * scale), int(h * scale)))
        player_surf.set_colorkey(color)
        return player_surf
