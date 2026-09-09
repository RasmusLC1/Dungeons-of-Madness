from scripts.entities.moving_entities.moving_entity import Moving_Entity
from scripts.entities.moving_entities.player.player_effects import Player_Status_Effect_Handler
from scripts.entities.moving_entities.player.player_weapon import Player_Weapon_Handler
from scripts.entities.moving_entities.player.player_movement import Player_Movement
from scripts.entities.moving_entities.player.player_animation_handler import Player_Animation_Handler
from scripts.engine.keys.keys import keys
from scripts.entities.items.weapons.projectiles.bombs.bomb_launcher import Bomb_Launcher

import random
import pygame


class Player(Moving_Entity):

    _animation_handler = Player_Animation_Handler
    _effect_handler = Player_Status_Effect_Handler

    def __init__(self, game, pos, size, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, keys.player, keys.player, pos, size, health, strength, max_speed, agility, intelligence, stamina, keys.player)
 
        self.bow_cooldown = 0
        self.souls = 500
        self.souls_to_remove = 0
        self.nearby_chests = []
        self.view_direction = (0,0)

        self.light_cooldown = 0
        self.default_light_level = 6
        
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.default_light_level, self.tile)
        self.game.light_handler.Initialise_Light_Level(self.tile)
        self.player_particle_cooldown = 0
        self.last_shrine_visited = None # used for teleporting and other shrine logic
        self.luck = 10 # player luck, can be upgraded from 0 -> 10
        self.rune_power = 0
        self.arcane_conduit = 0

        self.weapon_handler = Player_Weapon_Handler(self.game, self)
        self.movement_handler = Player_Movement(self.game, self)


        self.bomb_launcher = Bomb_Launcher(game)

    def Save_Data(self):
        super().Save_Data()
        self.saved_data[keys.souls] = self.souls
        self.saved_data['max_speed'] = self.max_speed
        self.saved_data['last_shrine_visited'] = self.last_shrine_visited 


    def Load_Data(self, data):

        super().Load_Data(data)
        self.souls = data[keys.souls]
        self.max_speed = data['max_speed']
        self.last_shrine_visited = data['last_shrine_visited']

    

    def Update(self, tilemap, delta_time, movement=(0, 0), offset=(0, 0)):
        # Resets luck and rune power
        self.Update_Luck(-self.luck)
        self.Update_Rune_Power(-self.rune_power)
        super().Update(tilemap, delta_time, movement=movement)

        self.Mouse_Handler()
        self.movement_handler.Update()

        
        self.Update_Light()
        self.Caclulate_View_Direction()

        self.weapon_handler.Update(delta_time, offset)

        self.Update_Souls_To_Remove()
        self.Spawn_Particles(delta_time)
        self.tile.distance_to_player


    def Caclulate_View_Direction(self):
        self.view_direction = pygame.math.Vector2(self.target[0] - self.pos[0], self.target[1] - self.pos[1])
        if self.view_direction.length() > 0:
            self.view_direction.normalize_ip()

    def Set_Souls(self, souls):
        self.souls = souls

    def Increase_Souls(self, added_soul):
        arcane_hunger_strength = self.Get_Effect_Strength(keys.arcane_hunger)
        if arcane_hunger_strength:
            added_soul += arcane_hunger_strength
        self.souls += added_soul

    def Decrease_Souls(self, subtract_soul):
        if self.souls_to_remove + subtract_soul > self.souls:
            return False
        self.souls_to_remove += subtract_soul
        return True
    
    

    # Subtract the souls that are to be removed from total souls to get a correct souls count
    def Get_Total_Available_Souls(self):
        return self.souls - self.souls_to_remove
    
    # Returns acane conduit effect
    def Get_Acane_Conduit(self):
        return self.arcane_conduit
    
    def Set_Arcane_Conduit(self, amount):
        self.arcane_conduit = amount

    def Update_Souls_To_Remove(self):
        if not self.souls_to_remove:
            return
        
        self.souls_to_remove = max(0, self.souls_to_remove - 1)
        self.souls = max(0, self.souls - 1)
        self.game.particle_handler.Activate_Particles(1, keys.soul_particle, self.rect().center, time = random.uniform(1.5, 2))


    def Entity_Collision_Detection(self):
        if self.movement_handler.dashing > 40:
            return None
        return super().Entity_Collision_Detection()
    
    def Remove_Active_Weapon(self):
        self.weapon_handler.Remove_Active_Weapon()

    def Set_Health(self, health):
        self.health = health


    def Trigger_Attack_Animation(self):
        self.animation_handler.Trigger_Attack_Animation()

    
    def Set_Active_Weapon(self, weapon):  
        self.weapon_handler.Set_Active_Weapon(weapon)
    
    def Set_Light_State(self, state):
        self.light_source.active = state


    def Update_Light_Source(self, light_level):
        self.light_source.Update_Light_Level(light_level)

    # Function to update the light around player
    def Update_Light(self):
        # Check if player has moved to new tile
        if self.light_source.tile == self.tile:
            return

        if not self.light_source.active:
            # If lights were off trigger new light
            self.light_source.active = True
            self.game.light_handler.Move_Light(self.pos, self.light_source, self.tile)
            self.Set_Light_State(True)
        else:
            # Standard movement update
            self.game.light_handler.Move_Light(self.pos, self.light_source, self.tile)
        
        
    def Mouse_Handler(self):
        self.Set_Target(self.game.mouse.player_mouse)


    def Find_Nearby_Chests(self, range):
        self.nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.pos, range)


    def Enable_Inventory_Effect(self, effect_name, effect_power):
        self.effects.Set_Effect(effect_name, effect_power, True)

    def Disable_Inventory_Effect(self, effect_name, effect_power):
        self.effects.Remove_Effect(effect_name, effect_power)

    # Interface function to call the actual inventory function
    def Pay_Gold(self, amount):
        return self.game.inventory.item_inventory.Pay_Gold(amount)

    # Set luck, called by luck effect, minimum value of 1
    def Update_Luck(self, amount):
        self.luck = max(0, self.luck + amount)

    def Update_Rune_Power(self, amount):
        self.rune_power = max(0, self.rune_power + amount)
        
    def Check_If_Dead(self):
        # Check if the player can be revived
        if self.health <= 0:
            if self.game.inventory.item_inventory.Revive():
                return False
        if not super().Check_If_Dead():
            return False
        
        self.game.clatter.Reset_Awakening_Level()
        self.game.state_machine.Set_State('game_over')

        return True
    
    def Charge(self, render_scroll):
        self.movement_handler.Dash(render_scroll)

    def Set_Last_Shrine(self, shrine):
        self.last_shrine_visited = shrine

    def Set_Attack_Speed(self, attack_time):
        self.animation_handler.Set_Attack_Speed(attack_time)

    # Spawn player particles at random intervals
    def Spawn_Particles(self, delta_time):
        if not self.player_particle_cooldown:
            self.player_particle_cooldown = random.uniform(0.3, 0.5)
            self.game.particle_handler.Activate_Particles(random.randint(1, 3), keys.player_particle, self.rect().center)

            return
        self.player_particle_cooldown -= delta_time
        return

    def Get_Animation(self):
        return self.animation_handler.Get_Action()
    
    def Set_Animation_Idle(self):
        # Reset the animation lock to overwrite current animation
        self.animation_handler.Set_Animation_Lock(False)
        return self.animation_handler.Set_Animation(keys.idle)
    
    def Get_Weapon(self):
        return self.weapon_handler.Get_Active_Weapon()

    # Render player
    def Render(self, surf, offset=(0, 0)):
        if abs(self.movement_handler.dashing) >= 50:
            return
        
        action = self.animation_handler.Get_Action()
        if 'roll'  in action or 'backstep' in action:
            super().Render(surf, offset)
            return

        if 'up' in action:
            self.weapon_handler.Render_Weapons(surf, offset)
            super().Render(surf, offset)
            return
        else:
            super().Render(surf, offset)
            self.weapon_handler.Render_Weapons(surf, offset)
            return
   