import math
import pygame
from scripts.engine.utility.rect_handler import Rect_Handler

# Basic raycasting attributes
DEFAULT_ACTIVITY = 700
NUM_LINES = 100 
SPREAD_ANGLE = 360  
ANGLE_INCREMENT = SPREAD_ANGLE / (NUM_LINES - 1) if NUM_LINES > 1 else 0
TILE_SIZE = 32
INACTIVE_DISTANCE = 800 * 800 

class Ray_Caster():
    def __init__(self, game):
        self.game = game
        self.tiles = []
        self.saved_data = None
        self.rect_handler = Rect_Handler(10, 10)

        # Pre-calculate ray vectors to save math during runtime
        self.ray_vectors = []
        self._generate_ray_vectors()

    # Pre-calculates unit vectors for the rays.
    def _generate_ray_vectors(self):
        self.ray_vectors = []
        start_rad = math.radians(-SPREAD_ANGLE / 2)
        inc_rad = math.radians(ANGLE_INCREMENT)
        
        for j in range(NUM_LINES):
            angle = start_rad + (j * inc_rad)
            self.ray_vectors.append((math.cos(angle), math.sin(angle)))

    def Save_Data(self):
        self.saved_data = {}
        tilemap = self.game.tilemap
        for tile in self.tiles:
            tile_key = tilemap.Convert_Tile_Pos_To_Key(tile.pos)
            self.saved_data[tile_key] = tile.pos

    def Load_Data(self, data):
        for pos_data in data.values():
            tile_key = tuple(pos_data) 
            tile = self.game.tilemap.Get_Tile(tile_key)
            if tile:
                self.tiles.append(tile)
            else:
                print(f"RAYCASTER TILE NOT FOUND AT {tile_key}")

    def Update(self, delta_time):
        self.Check_Tile_Active()
        self.Update_Entities(delta_time)

    def Update_Entities(self, delta_time):
        for tile in self.tiles:
            tile.Set_Entity_Active(delta_time)

    # Optimized filtering using list comprehension
    def Check_Tile_Active(self):
        p_pos = self.game.player.pos
        # Rebuild list only with active tiles that are within distance
        self.tiles = [tile for tile in self.tiles if self._process_tile_activity(tile, p_pos)]

    # Helper to handle individual tile logic during filter
    def _process_tile_activity(self, tile, player_pos):
        if tile.active:
            tile.active -= 1
        
        dx = player_pos[0] - tile.scaled_pos[0]
        dy = player_pos[1] - tile.scaled_pos[1]
        
        if (dx * dx + dy * dy) > INACTIVE_DISTANCE:
            tile.active = 0
            return False
        return True

    def Remove_Tile(self, tile):
        if tile in self.tiles:
            tile.active = 0
            self.tiles.remove(tile)

    def Check_Tile(self, tile_pos):
        tilemap = self.game.tilemap
        tile = tilemap.Current_Tile(tile_pos)
        
        if not tile:
            return False
        
        # If tile is already active, we just refresh it and skip the heavy Add_Tile logic
        if tile.active:
            tile.Set_Active(DEFAULT_ACTIVITY)
        else:
            self.Add_Tile(tilemap, tile)
        
        return tile.translucent

    def Add_Tile(self, tilemap, tile):
        tile.Set_Active(DEFAULT_ACTIVITY)
        self.tiles.append(tile)
        tilemap.Add_Tile_To_Minimap(tile)

    def Clear_Entity_From_Tiles(self, entity_ID):
        for tile in self.tiles:
            tile.Remove_Entity(entity_ID)
 
    def Ray_Caster(self):
        player_tile_pos = self.game.player.tile.pos
        px, py = player_tile_pos
        
        # Localize functions/variables to speed up lookups inside the loop
        check_func = self.Check_Tile
        max_steps = round(8 * self.game.render_scale)
        vectors = self.ray_vectors
        
        # Check origin tile
        check_func(player_tile_pos)
        
        # Cast rays
        for dx, dy in vectors:
            for i in range(1, max_steps):
                # Step along the vector
                if not check_func((px + dx * i, py + dy * i)):
                    break

    def rect(self, pos):
        return self.rect_handler.rect(pos)