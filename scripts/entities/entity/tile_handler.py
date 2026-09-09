import pygame
from scripts.engine.utility.cooldown_handler import Cooldown_Handler

MIN_LIGHT_LEVEL = 40
LIGHT_ALPHA_SCALE = 30
TILE_COOLDOWN_MAX = 0.1

class Tile_Handler:
    def __init__(self, entity):
        self.entity = entity
        self.game = entity.game
        self.tile = None
        self.tile_cooldown_handler = Cooldown_Handler(TILE_COOLDOWN_MAX)

    def Set_Tile(self):
        self.Remove_Tile()
        
        tile_size = self.game.tilemap.tile_size
        feet_x = self.entity.rect().midtop[0]
        feet_y = self.entity.rect().midtop[1]

        tile_x = int(feet_x // tile_size)
        tile_y = int(feet_y // tile_size)
        
        new_tile = self.game.tilemap.Current_Tile((tile_x, tile_y))
        if not new_tile:
            return False
            
        self.tile = new_tile
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self.entity)
        
        if hasattr(self.tile, 'Add_Entity'):
            self.tile.Add_Entity(self.entity)
        return True

    def Remove_Tile(self):
        if not self.tile:
            return
        self.tile.Remove_Entity(self.entity.ID)
        self.tile = None

    def Update_Light_Level(self):
        if not self.tile:
            return True

        new_light_level = min(255, self.tile.light_level * LIGHT_ALPHA_SCALE)

        if self.entity.light_level < new_light_level:
            self.entity.Set_Light_Level(self.entity.light_level + 5)
            self.entity.render_needs_update = True
        elif self.entity.light_level > new_light_level:
            self.entity.Set_Light_Level(self.entity.light_level - 5)
            self.entity.render_needs_update = True
        
        return self.entity.light_level > self.entity.min_light_level

    def Update_Tile(self, delta_time):
        if not self.tile_cooldown_handler.Update_Cooldown(delta_time):
            return False

        if not self._Check_If_Tile():
            return False    

        t_size = self.game.tilemap.tile_size
        nx, ny = int(self.entity.pos[0]) // t_size, int(self.entity.pos[1]) // t_size

        if (nx, ny) == self.tile.pos:
            return False

        return self._Add_New_Tile(nx, ny)
    
    def _Add_New_Tile(self, nx, ny):
        new_tile = self.game.tilemap.Current_Tile((nx, ny))
        
        if new_tile and new_tile != self.tile:
            self.Remove_Tile()
            self.tile = new_tile
            self.game.tilemap.Add_Entity_To_Tile(self.tile, self.entity)
            if hasattr(self.tile, 'Add_Entity'):
                self.tile.Add_Entity(self.entity)
            return True
        
        return False
    
    def _Check_If_Tile(self):
        if self.tile:
            return True
        
        print(f"ERROR TILE NOT FOUND: {self.entity.type} at {self.entity.pos}")
        new_tile = self.game.tilemap.Get_Random_Tile_With_Path_To_Player()
        if not new_tile:
            self.entity.Delete()
            return False
        
        self.tile = new_tile
        self.entity.pos = pygame.Vector2(self.tile.scaled_pos)
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self.entity)
        if hasattr(self.tile, 'Add_Entity'):
            self.tile.Add_Entity(self.entity)
        return True