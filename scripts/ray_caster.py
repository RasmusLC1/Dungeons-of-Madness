import math
import pygame

class Ray_Caster():
    def __init__(self, game):
        self.tiles = []
        self.enemies = []
        self.traps = []
        self.chests = []
        self.game = game
        self.default_activity = 700

    def Update(self, game):
        # Handle tile activity degradation
        for tile in self.tiles:
            if tile['active']:
                tile['active'] -= 1
            # Find distance from player and if it's greater than 300, delete it
            distance = math.sqrt((game.player.pos[0] - tile['pos'][0] * 16) ** 2 + (game.player.pos[1] - tile['pos'][1] * 16) ** 2)
            if abs(distance) > 300:
                tile['active'] = 0
                self.tiles.remove(tile)

        for enemy in self.enemies:
            if enemy.active:
                enemy.Reduce_Active()
            else:
                self.enemies.remove(enemy)
            distance = math.sqrt((game.player.pos[0] - enemy.pos[0]) ** 2 + (game.player.pos[1] - enemy.pos[0]) ** 2)
            if abs(distance) > 300:
                enemy.Set_Active(0)
                self.enemies.remove(enemy)


        for chest in self.chests:
            if chest.active:
                chest.Reduce_Active()
            else:
                self.chests.remove(chest)
            distance = math.sqrt((game.player.pos[0] - chest.pos[0]) ** 2 + (game.player.pos[1] - chest.pos[0]) ** 2)
            if abs(distance) > 300:
                chest.Set_Active(0)
                self.chests.remove(chest)
            

                

    def Ray_Caster(self):
        # Basic raycasting attributes
        num_lines = 20 # Define the number of lines and the spread angle (in degrees)
        spread_angle = 120  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1) # Calculate the angle increment between each line
        # Calculate the starting angle
        base_angle = math.atan2(self.game.player.direction_y_holder, self.game.player.direction_x_holder)
        start_angle = base_angle - math.radians(spread_angle / 2)
        
        # Check the tile the player is standing on
        tile = self.game.tilemap.Current_Tile((self.game.player.pos[0], self.game.player.pos[1]))
        if tile and not tile['active']:
            tile['active'] = self.default_activity
            self.tiles.append(tile)
        else:
            tile['active'] = self.default_activity


        # Find nearby Enemies
        self.game.player.nearby_enemies.clear()
        self.game.player.Nearby_Enemies(200)
        nearby_chests = self.game.chest_handler.find_nearby_chests(self.game.player.pos, 200)


        # Look for tiles that hit the rays
        for j in range(num_lines):
            for i in range(1, 13):
                angle = start_angle + j * math.radians(angle_increment)
                pos_x = self.game.player.pos[0] + math.cos(angle) * 16 * i
                pos_y = self.game.player.pos[1] + math.sin(angle) * 16 * i
                tile = self.game.tilemap.Current_Tile((pos_x, pos_y))
                if tile:
                    if not tile['active']:
                        tile['active'] = self.default_activity
                        self.tiles.append(tile)
                    else:
                        tile['active'] = self.default_activity

                    if tile['type'] == 'BottomWall' or tile['type'] == 'TopWall' or tile['type'] == 'RightWall' or tile['type'] == 'LeftWall':
                            break

                for enemy in self.game.player.nearby_enemies:
                    # Check if enemy is already in the enemy list
                    if self.rect((pos_x, pos_y)).colliderect(enemy.rect()):
                        if not enemy.active:
                            enemy.Set_Active(255)
                            self.enemies.append(enemy)
                        else:
                            enemy.Set_Active(255)

                for chest in nearby_chests:
                    if self.rect((pos_x, pos_y)).colliderect(chest.rect()):
                        if not chest.active:
                            chest.Set_Active(255)
                            self.chests.append(chest)
                        else:
                            chest.Set_Active(255)

                        
                # pygame.draw.line(surf, (255, 255, 255), (self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1]), (pos_x, pos_y), 1)
        
        # print(self.game.player.nearby_enemies)

    def rect(self, pos):
        return pygame.Rect(pos[0], pos[1], 10, 10)