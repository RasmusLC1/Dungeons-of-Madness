from collections import deque
import pygame
import logging
from scripts.engine.keys.keys import keys
from .tile_handler import Tile_Handler
from .animation_handlers.base_animation_handler import Base_Animation_Handler
from scripts.engine.utility.rect_handler import Rect_Handler

class PhysicsEntity:
    _id_counter = 0
    _available_IDs = deque()
    _animation_handler = Base_Animation_Handler   # subclasses override this

    def __init__(self, game, type, category, pos, size, sub_category=None,
                 max_animation = 0, animation_cooldown_max = 0):
        self.game = game
        self.Set_ID()
        self.rect_handler = Rect_Handler(size[0], size[1])

        self.category = category
        if not sub_category:
            sub_category = category
        self.sub_category = sub_category
        self.type = type
        self.Set_Text_Box()


        self.pos = pygame.Vector2(pos)
        self.size = list(size)

        self.entity_image = None
        self.rendered_image = None
        self.render = True
        self.render_needs_update = True
        self.min_light_level = 40

        self._cached_dark_surface = pygame.Surface(self.size, pygame.SRCALPHA).convert_alpha()
        self._cached_light_surface = pygame.Surface(self.size, pygame.SRCALPHA).convert_alpha()

        self.saved_data = None
        self.active = 0
        self.active_opacity = 255
        self.light_level = 0



        self.touching_ground = True
        self.tile_handler = Tile_Handler(self)
        self.tile_handler.Set_Tile()

        self.animation_handler = self._animation_handler(self, max_animation, animation_cooldown_max)

        self.description = ''
        self.light_up_color = (255, 0, 0, 255)


    # --- Properties for Backward Compatibility ---
    @property
    def tile(self):
        """Allows legacy external logic to access entity.tile directly."""
        return self.tile_handler.tile

    @tile.setter
    def tile(self, new_tile):
        """Allows direct mutation alignment transfers."""
        self.tile_handler.tile = new_tile

    @property
    def max_animation(self):
        return self.animation_handler.animation_max

    @property
    def min_animation(self):
        return self.animation_handler.min_animation

    @min_animation.setter
    def min_animation(self, new_animation):
        self.animation_handler.min_animation = new_animation
    

    @property
    def animation_cooldown_max(self):
        return self.animation_handler.animation_cooldown_max
    
    @property
    def animation_cooldown(self):
        return self.animation_handler.animation_cooldown

    @property
    def animation(self):
        return self.animation_handler.animation

    @animation.setter
    def animation(self, new_animation):
        """Allows direct mutation alignment transfers."""
        self.animation_handler.animation = new_animation


    # --- Structural Identity Core ---
    def Set_ID(self):
        if PhysicsEntity._available_IDs:
            self.ID = PhysicsEntity._available_IDs.popleft()
        else:
            self.ID = PhysicsEntity._id_counter
            PhysicsEntity._id_counter += 1

    # --- Delegated Spatial API Pipelines ---
    def Remove_Tile(self):
        self.tile_handler.Remove_Tile()

    def Set_Tile(self):
        self.tile_handler.Set_Tile()

    def Set_Touching_Ground(self, state):
        self.touching_ground = state
        
    def Update_Tile(self, delta_time):
        # if self.tile:
        #     print({slot: getattr(self.tile, slot) for slot in self.tile.__slots__ if hasattr(self.tile, slot)})
        return self.tile_handler.Update_Tile(delta_time)

    def Update_Light_Level(self):
        return self.tile_handler.Update_Light_Level()

    # --- Core Transform API ---
    def Set_Position(self, position):
        try:
            self.pos = pygame.Vector2(position)
        except Exception as e:
            print(f"WRONG POSITION FORMAT: {e}", position)

    def Set_Size(self, size):
        self.size = list(size)
        self._cached_dark_surface = pygame.Surface(self.size, pygame.SRCALPHA).convert_alpha()
        self._cached_light_surface = pygame.Surface(self.size, pygame.SRCALPHA).convert_alpha()
        self.Set_Sprite()

    def rect(self):
        return self.rect_handler.rect(self.pos)

    # --- Stateful Logic Engine ---
    def Set_Active(self, duration):
        if duration == self.active:
            return
            
        self.active = duration
        self.active_opacity = max(0, min(255, duration))
        self.render_needs_update = True

    def Reduce_Active(self):
        self.Set_Active(self.active - 1)

    def Update_Active(self, state):
        self.Set_Active(state)
        self.Update_Dark_Surface()

    def Update_Animation(self, delta_time, movement=(0, 0)):
        return self.animation_handler.Update_Animation(movement, delta_time)

    def Set_Animation(self, animation):
        return self.animation_handler.Set_Frame(animation)

    def Set_Light_Level(self, value):
        # Clamps values flawlessly within color array safety channels
        self.light_level = max(self.min_light_level, min(255, value))
        self.render_needs_update = True

    # --- Interactivity & Feedback Routines ---
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        if not self.text_box:
            return None
        return self if self.text_box.Update(hitbox_1, hitbox_2) else None

    def Set_Text_Box(self):
        self.text_box = None

    def Generate_Sound(self, sound_name, volume, clatter, pos=None):
        sound_pos = pos if pos else self.pos
        self.game.sound_handler.Play_Sound(sound_name, volume)
        self.game.noise_handler.Activate(sound_pos)
        if clatter:
            self.game.clatter.Generate_Clatter(sound_pos, clatter)

    # --- Visual Graphics Pipeline ---
    def Update_Dark_Surface(self):
        if not self.render_needs_update or not self.entity_image:
            return False
            
        alpha_value = max(0, min(255, self.active))
        if alpha_value == 0:
            return False
            
        try:
            self.rendered_image = self.entity_image.copy()
            self.rendered_image.set_alpha(alpha_value)
            self._cached_dark_surface.fill((self.light_level, self.light_level, self.light_level, 255))
            self.rendered_image.blit(self._cached_dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.render_needs_update = False
            return True
        except Exception as e:
            print("Error in Updating dark surface entity: ", e, self.light_level, alpha_value, self.type)
            return False

    def Lightup(self, entity_image):
        if not entity_image:
            return
        self._cached_light_surface.fill(self.light_up_color)
        entity_image.blit(self._cached_light_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # --- Life Cycle Data Persistence ---
    def Save_Data(self):
        self.saved_data = {
            'ID': self.ID,
            'category': self.category,
            keys.type: self.type,
            keys.pos: [self.pos[0], self.pos[1]],
            'size': self.size,
            'active': self.active,
            'light_level': self.light_level,
            'render': self.render
        }
        self.saved_data.update(self.animation_handler.Save_Data())
        return self.saved_data

    def Load_Data(self, data):
        self.ID = data['ID']
        self.category = data['category']
        self.type = data[keys.type]
        self.pos = pygame.Vector2(data[keys.pos])
        self.size = data['size']
        self.active = data['active']
        self.light_level = data['light_level']
        self.render = data['render']
        self.animation_handler.Load_Data(data)
        
        self.tile_handler.Set_Tile()
        if self.ID >= PhysicsEntity._id_counter:
            PhysicsEntity._id_counter = self.ID + 1

    def Delete(self):
        self.tile_handler.Remove_Tile()
        if hasattr(self, "ID") and self.ID not in PhysicsEntity._available_IDs:
            PhysicsEntity._available_IDs.append(self.ID)

    # --- Subclass Extension Hooks ---
    def Update(self, delta_time, movement=(0, 0)):
        if not self.animation_cooldown_max:
            return False
        return self.Update_Animation(delta_time, movement)


    def Damage_Taken(self, damage): pass
    def Set_Effect(self, effect, duration, permanent=False): pass

    def Set_Description(self): pass
    
    def Set_Sprite(self, key=None):
        return self.animation_handler.Set_Sprite(key if key is not None else self.type)

    def Set_Entity_Image(self):
        self.animation_handler.Set_Entity_Image()
    
    def Render(self, surf, offset=(0, 0)):
        if not self.Update_Light_Level():
            return

        self.Update_Dark_Surface()

        if not self.rendered_image:
            if not self.entity_image:
                self.Set_Sprite()

            if self.entity_image:
                self.render_needs_update = True
                self.Update_Dark_Surface()

            if not self.rendered_image:
                logging.warning("No image to render for %s (id=%s)", self.type, self.ID)
                return

        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    
