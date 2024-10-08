from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.level_generation.noise_map import Noise_Map
from scripts.engine.tilemap import Tilemap
from scripts.engine.a_star import A_Star
import random
import os

import math
# TODO:  shrines, entrance and exit, keys 

class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.player_spawn = (0, 0)
        self.cellular_automata = Cellular_Automata()
        self.tilemap = Tilemap(self, tile_size=16)
        self.a_star = A_Star()
        self.traps = ['spike_trap', 'spike_poison_trap', 'Pit_trap', 'Pit_trap', 'Pit_trap']
        self.noise_map = Noise_Map()
        self.torches = []




    def Generate_Map(self):
        self.Delete_Map_File('data/maps/0.json')
        self.tilemap.Clear_Tilemap()
        self.cellular_automata.Create_Map()

        floor = 0
        lava = 2
        
        self.Spawn_Lakes(20, floor, lava)

        
        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

        self.Player_Spawn()
        self.a_star.Set_Map('custom')
        
        if not self.Spawn_Loot_Room(4):
            self.Generate_Map()
            return

        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

        self.a_star.Set_Map('custom')

        # Call itself recursively and generate a new map if it fails to spawn enemies
        if not self.Enemy_Spawner():
            self.Generate_Map()
            return
        
        

        
        self.Spawn_Loot(2)

        self.Level_Structure()

        

        self.tilemap.save('data/maps/0.json')

    def Spawn_Lakes(self, iterations, value_1, value_2):
        for i in range(iterations):

            density = random.randint(30, 40)
            size_x = random.randint(3, 5)
            size_y = random.randint(3, 5)
            start_x = random.randint(2, self.cellular_automata.size_x - size_x)
            start_y = random.randint(2, self.cellular_automata.size_y - size_y)
            lake_map = [[0 for _ in range(size_y)] for _ in range(size_x)]

            self.noise_map.Generate_Map(density, lake_map, value_1, value_2, size_x, size_y)
            self.cellular_automata.Refine_Level(value_1, value_2, size_x, size_y, 1, lake_map)
            i = 0
            j = 0
            for y in range(start_y, start_y + size_y):
                i = 0
                for x in range(start_x, start_x + size_x):
                    if x >= self.cellular_automata.size_x- 2 or y >= self.cellular_automata.size_y - 2:
                        break

                    self.cellular_automata.map[x][y] = lake_map[i][j]
                    i += 1
                j += 1

    def Level_Structure(self):
        for j in range(self.cellular_automata.size_y):
            for i in range(self.cellular_automata.size_x):
                if self.cellular_automata.map[i][j] == 1: # Wall 
                    if not self.Wall_Checker(i, j):
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


                elif self.cellular_automata.map[i][j] == 0: # Floor
                    self.Floor_Checker(i, j)
                elif self.cellular_automata.map[i][j] == 2:
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Lava_env', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif self.cellular_automata.map[i][j] == 3:
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'DoorClosed', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


    # Spawns torches based on density, it then checks distance to nearest torch to prevent overlap
    # Higher density = More torches
    def Torch_Spawner(self, i, j, density):
        spawn_torch = random.randint(0, density)
        if spawn_torch == 1:
            for torch in self.torches:
                distance = math.sqrt((i - torch[0]) ** 2 + (j - torch[1]) ** 2)
                if distance < 8:
                    return
            self.torches.append((i, j))
            self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [i * 16, j * 16]})

    def Floor_Checker(self, i, j):
        value = random.randint(0, 100)
        if value < 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': self.traps[value], 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
        else:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Floor', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            self.Torch_Spawner(i, j, 20)


    def Spawn_Loot_Room(self, rooms):

        success = 0
        fail = 0

        while success <= rooms:
            size_x = random.randint(4, 6)
            size_y = random.randint(4, 6)
            start_x = random.randint(5, self.cellular_automata.size_x - size_x)
            start_y = random.randint(5, self.cellular_automata.size_y - size_y)

            # Ensure that the room is far enough away from the player
            distance = math.sqrt((self.player_spawn[0] - start_x) ** 2 + (self.player_spawn[1] - start_y) ** 2)
            if distance < 20:
                continue

            # Flatten the loot room and make it floors
            for y in range(start_y, start_y + size_y):
                for x in range(start_x, start_x + size_x):
                    if y == start_y:
                        self.cellular_automata.map[x][y] = 1
                    elif y == start_y + size_y - 1:
                        self.cellular_automata.map[x][y] = 1
                    elif x == start_x:
                        self.cellular_automata.map[x][y] = 1
                    elif x == start_x + size_x - 1:
                        self.cellular_automata.map[x][y] = 1
                    else:
                        self.cellular_automata.map[x][y] = 0
            
            # Close the walls
            # self.cellular_automata.Close_Borders(start_x, start_y, start_x + size_x, start_y + size_y)
            path = []

            # Check if left side connects to player
            y_door = start_y + size_y // 2
            self.a_star.a_star_search(path, [start_x - 1, y_door], [self.player_spawn[0], self.player_spawn[1]], 'test')
            if not path:
                fail += 1
                if fail >= 10:
                    return False
                continue

            chest_count = 0
            for y in range(start_y + 1, start_y + size_y - 1):
                for x in range(start_x + 1, start_x + size_x -1):
                    spawn_loot = random.randint(1, 3)
                    if spawn_loot == 1:
                        chest_count += 1
                        self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (x * 16, y * 16)})
            
            # Spawn a chest in case nothing else spawns as a backup
            if not chest_count:
                self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (start_x + size_x // 2 * 16, start_y + size_y // 2 * 16)})


            print("TESTTEST", [start_x - 1, y_door], [self.player_spawn[0], self.player_spawn[1]])
            self.cellular_automata.map[start_x][y_door] = 3
            success += 1

        return True
 

        

    def Wall_Checker(self, i, j):

        # Handle Edge cases first to prevent crashes
        if i <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'LeftWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        elif i >= self.cellular_automata.size_x - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'RightWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'TopWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j >= self.cellular_automata.size_y - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        wall_found = False

        if self.cellular_automata.map[i + 1][j] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'LeftWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True

        elif self.cellular_automata.map[i - 1][j] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'RightWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True


        if self.cellular_automata.map[i][j - 1] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'TopWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True

        elif self.cellular_automata.map[i][j + 1] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True
            
        return wall_found
        

    
    def Player_Spawn(self):
        self.player_spawn = (20, 20)
        for y in range(self.player_spawn[1] - 5, self.player_spawn[1] + 5):
            for x in range(self.player_spawn[0] - 5, self.player_spawn[0] + 5):
                self.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y), 'active': 0, 'light': 0}
        
        self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (self.player_spawn[0] * 16, self.player_spawn[1] * 16)})

        self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [self.player_spawn[0] * 16, self.player_spawn[1] * 16]})
    
    def Enemy_Spawner(self):
        spawners = 0
        fails = 0
        path = []
        while spawners < 10:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == 1:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 1, 'pos': (spawner_x * 16, spawner_y * 16)})
                spawners += 1
            else:
                fails += 1

            if fails > 20:
                return False
        
        return True

    def Spawn_Loot(self, level):
        loot_amount = random.randint(10 + level, 20 + level)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == 1:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (spawner_x * 16, spawner_y * 16)})
                loot += 1


    def Delete_Map_File(self, file_path):

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
            


