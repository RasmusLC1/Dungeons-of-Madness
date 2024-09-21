import sys

import pygame
import json
import math


from scripts.engine.utility.utils import load_image, load_images, Animation
from scripts.engine.assets.graphics_loader import Graphics_Loader
from scripts.engine.assets.audio_loader import Audio_Loader
from scripts.input.keyboard import Keyboard_Handler
from scripts.input.mouse import Mouse_Handler
from scripts.entities.player.player import Player
from scripts.engine.tilemap import Tilemap
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.decoration.decoration_handler import Decoration_Handler
from scripts.items.item_handler import Item_Handler
from scripts.interface.health_bar import Health_Bar
from scripts.interface.ammo_bar import Ammo_Bar
from scripts.interface.souls import Souls
from scripts.decoration.chest.Chest_handler import Chest_Handler
from scripts.entities.enemies.enemy_handler import Enemy_Handler
from scripts.engine.a_star import A_Star
from scripts.engine.lights.light_handler import Light_Handler
from scripts.inventory.item_inventory import Item_Inventory
from scripts.inventory.weapon_inventory_handler import Weapon_Inventory_Handler
from scripts.engine.ray_caster import Ray_Caster 
from scripts.entities.entity_renderer import Entity_Renderer
from scripts.engine.fonts.font import Font
from scripts.engine.fonts.symbols import Symbols
from scripts.engine.clatter import Clatter
from scripts.items.utility.text_box_handler import Text_Box_handler



import numpy as np

import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.render_scale = 4
        
        self.screen_width = 1280
        self.screen_height = 960
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((self.screen_width/self.render_scale, self.screen_height/self.render_scale))
        self.render_scroll = (0,0)
        self.clock = pygame.time.Clock()
        
        self.movement = [False, False, False, False]
        self.assets = {}
        Graphics_Loader.Run_All(self)
        Audio_Loader.Run_All(self)


        self.tilemap = Tilemap(self, tile_size=16)
        self.item_inventory = Item_Inventory(self)
        # TODO: PLACEHOLDER CODE, Implement proper class system later
        self.proffeciency = {'sword, shield, bow, arrow, axe, mace'}
        self.weapon_inventory = Weapon_Inventory_Handler(self, 'warrior', self.proffeciency)
        self.mouse = Mouse_Handler(self)
        self.ray_caster = Ray_Caster(self)
        self.a_star = A_Star()
        self.entities_render = Entity_Renderer(self)
        self.default_font = Font(self)
        self.symbols = Symbols(self)
        self.clatter = Clatter(self)
        self.text_box_handler = Text_Box_handler(self)
        Ammo_Bar.__init__(self)
        Health_Bar.__init__(self)
        self.souls_interface = Souls(self)



        self.level = 0
        self.scroll = [0, 0]

        self.load_level(self.level)

        



    def tilemap_2d(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]

    def count_lines_in_json_file(file_path):
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count

    def load_level(self, map_id):
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
         # Setup handlers
        self.light_handler = Light_Handler(self)
        
        
        self.particles = []
        self.sparks = []
        self.scroll = [0, 0]
        self.projectiles = []
        for spawner in self.tilemap.extract([('spawners', 0)]):
            print("PLAYER")
            if spawner['variant'] == 0:
                self.player = Player(self, spawner['pos'], (8, 16), 100, 5, 8, 10, 5, 5)

        self.enemy_handler = Enemy_Handler(self)
        self.trap_handler = Trap_Handler(self)
        self.decoration_handler = Decoration_Handler(self)
        self.chest_handler = Chest_Handler(self)
        self.item_handler = Item_Handler(self)
 
        
        
        self.a_star.Setup_Map(self)

        # Printing the map
        # for row in self.shadow_map:
        #     print(row)

    # Get the scroll offset
    def Camera_Scroll(self):
        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
        self.render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

    def Input_Handler(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.mouse.Mouse_Input(event, self.render_scroll)

                Keyboard_Handler.keyboard_Input(self, event, offset = self.render_scroll)

    def Update(self):
            fps = int(self.clock.get_fps())
            pygame.display.set_caption('Dungeons of Madness             FPS: ' + str(fps))
            
            self.player.Update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]), self.render_scroll)
            Particle_Handler.particle_update(self, self.render_scroll)
            self.trap_handler.Update()
            self.decoration_handler.Update()
            self.item_handler.Update(self.render_scroll)
            self.enemy_handler.Update()
            self.entities_render.Update()


            self.item_inventory.Update(self.render_scroll)
            self.weapon_inventory.Update(self.render_scroll)
            self.souls_interface.Update()
            self.ray_caster.Update(self)

            self.mouse.Mouse_Update()
            self.text_box_handler.Update()
    

    def Render(self):
        self.display.blit(self.assets['background'], (0, 0))
        
        self.ray_caster.Ray_Caster()
        self.tilemap.render_tiles(self.ray_caster.tiles, self.display, offset=self.render_scroll)

        self.trap_handler.Render(self.ray_caster.traps, self.display, self.render_scroll)

        Health_Bar.Health_Bar(self)
        Ammo_Bar.Attack_Recharge_Bar(self)
        self.souls_interface.Render(self.display)
        self.entities_render.Render(self.display, self.render_scroll)
        for particle in self.particles:
            particle.Render(self.display, self.render_scroll)
        self.item_inventory.Render(self.display)
        self.weapon_inventory.Render(self.display, self.render_scroll)
        self.text_box_handler.Render(self.display, self.render_scroll)

        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))

        
    def run(self):  
        while True:

            self.Camera_Scroll()
            
            self.Render()
            self.Update()
            self.Input_Handler()
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()