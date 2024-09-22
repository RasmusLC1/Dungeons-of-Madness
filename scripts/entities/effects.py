import math
import random
import pygame


class Status_Effect_Handler:
    def __init__(self, entity):
        self.entity = entity

        self.is_on_fire = 0
        self.fire_cooldown = 0
        self.fire_animation = 0
        self.fire_animation_max = 7
        self.fire_animation_cooldown = 0
        self.fire_animation_cooldown_max = 20

        self.poisoned = 0
        self.poisoned_cooldown = 0
        self.poison_animation = 0
        self.poison_animation_max = 2
        self.poison_animation_cooldown = 0
        self.poison_animation_cooldown_max = 30

        self.is_on_ice = 0
        self.frozen = 0 
        self.frozen_cooldown = 0
        self.frozen_animation = 0
        self.frozen_animation_max = 2
        self.frozen_animation_cooldown = 0
        self.frozen_animation_cooldown_max = 30

        self.wet = 0 
        self.wet_cooldown = 0
        self.wet_animation = 0
        self.wet_animation_max = 2
        self.wet_animation_cooldown = 0
        self.wet_animation_cooldown_max = 30

        self.regen = 0 
        self.regen_max = 10 
        self.regen_cooldown = 0
        self.regen_animation = 0
        self.regen_animation_max = 5
        self.regen_animation_cooldown = 0
        self.regen_animation_cooldown_max = 30

        self.speed = 0 
        self.speed_max = 10 
        self.speed_cooldown = 0

        self.strength = 0 
        self.strength_max = 10 
        self.strength_cooldown = 0

        self.invisibility = 0 
        self.invisibility_max = 10 
        self.invisibility_cooldown = 0


        self.snared = 0


    def Set_Effect(self, effect, duration):
        if effect == 'Snare':
            return self.Set_Snare(duration)
        elif effect == 'Poison':
            return self.Set_Poisoned(duration)
        elif effect == 'Freeze':
            return self.Set_Frozen(duration)
        elif effect == 'Fire':
            return self.Set_On_Fire(duration)
        elif effect == 'Wet':
            return self.Set_Wet(duration)
        elif effect == 'Dry':
            return self.Set_Dry(duration)
        elif effect == 'Slow_Down':
            return self.Slow_Down(duration)
        elif effect == 'healing':
            return self.Healing(duration)
        elif effect == 'regen':
            return self.Set_Regen(duration)
        elif effect == 'speed':
            return self.Set_Speed(duration)
        elif effect == 'strength':
            return self.Set_Strength(duration)
        elif effect == 'invisibility':
            return self.Set_Invisibility(duration)
        else:
            return False
        
    def Update_Status_Effects(self):
        
        self.OnFire()
        self.Regen()
        self.Snare()
        self.Poisoned()
        self.Frozen()
        self.Wet()
        self.Speed()
        self.Strength()
        self.Invisibility()

    def Render_Effects(self, game, surf, offset=(0, 0)):
        # Render status effects
        #Fire
        self.Render_Effect(game, surf, self.is_on_fire, self.fire_animation, 'fire', offset)
        # Posion
        self.Render_Effect(game, surf, self.poisoned, self.poison_animation, 'poison', offset)
        # Frozen
        self.Render_Effect(game, surf, self.frozen, self.frozen_animation, 'frozen', offset)
        # Wet
        self.Render_Effect(game, surf, self.wet, self.wet_animation, 'wet', offset)
        # Regen
        self.Render_Effect(game, surf, self.regen, self.regen_animation, 'regen', offset)


     #set poison effect
    def Set_Poisoned(self, poison_time):
        self.poisoned =  max(random.randint(2, poison_time), self.poisoned)
        return True

    def Poisoned(self):
        if not self.poisoned:
            return
        if self.poisoned_cooldown:
            self.poisoned_cooldown -= 1

        if not self.poisoned_cooldown:
            self.entity.Damage_Taken(self.poisoned)
            self.poisoned_cooldown = random.randint(50, 70)
            self.poisoned -= 1
        self.Slow_Down(self.poisoned)
        self.Effect_Animation('poison_animation_cooldown', 'poison_animation', self.poison_animation_max, self.poison_animation_cooldown_max)
    

    #set frozen effect
    def Set_Frozen(self, freeze_time):
        if self.is_on_fire:
            return
        
        if self.wet:
            freeze_time *= 2
            self.wet = 0
        self.frozen = max(3, freeze_time)
        return True
    
    def Frozen(self):
        if self.frozen <= 1:
            self.frozen = 0
            return
        elif self.frozen_cooldown:
            self.frozen_cooldown -= 1

        if not self.frozen_cooldown:
            self.frozen_cooldown = random.randint(160, 200)
            self.frozen -= 1
        self.Slow_Down(self.frozen)
        self.Effect_Animation('frozen_animation_cooldown', 'frozen_animation', self.frozen_animation_max, self.frozen_animation_cooldown_max)
    
    def Remove_Frozen(self):
        self.frozen = 0

    # Set wet effect
    def Set_Wet(self, wet_time):
        if self.is_on_fire:
            self.is_on_fire = 0
        if self.frozen:
            self.frozen -= 1
        self.wet = max(2, wet_time)
        return True

    def Wet(self):
        if self.wet <= 1:
            self.wet = 0
            return
        elif self.wet_cooldown:
            self.wet_cooldown -= 1

        if not self.wet_cooldown:
            self.wet_cooldown = random.randint(160, 200)
            self.wet -= 1
        self.Effect_Animation('wet_animation_cooldown', 'wet_animation', self.wet_animation_max, self.wet_animation_cooldown_max)

    
    def Set_Dry(self, drying):
        self.wet = max(0, self.wet - drying)
        return True


    #set Fire effect
    def Set_On_Fire(self, fire_time):
        if self.wet:
            return False
        if self.frozen:
            self.Remove_Frozen()
        self.is_on_fire = max(random.randint(fire_time, fire_time * 2), self.is_on_fire)
        return True
    
    def OnFire(self):
        if self.fire_cooldown:
            self.fire_cooldown -= 1
        elif self.is_on_fire:
                damage = random.randint(1, 3)
                self.entity.Damage_Taken(damage)
                self.is_on_fire -= 1
                self.fire_cooldown = random.randint(30, 50)
        self.Effect_Animation('fire_animation_cooldown', 'fire_animation', self.fire_animation_max, self.fire_animation_cooldown_max)
    
   
    
    # Set Speed effect, doesn't work when frozen
    def Set_Speed(self, speed_time):
        if self.frozen:
            return False
        if self.speed >= self.speed_max:
            return False
        self.speed = min(speed_time + self.speed, 10)
        return True
    
    def Speed(self):
        if not self.speed or self.frozen:
            return
        
        self.entity.max_speed = min(14, self.entity.max_speed * 2)

        if self.speed_cooldown:
            self.speed_cooldown -= 1
        else:
            self.speed -= 1
            self.speed_cooldown = random.randint(40, 60)
    
    # Set Strength effect, doesn't work when poisoned
    def Set_Strength(self, strength_time):
        
        if self.poisoned:
            return False
        if self.strength >= self.strength_max:
            return False
        self.strength = min(strength_time + self.strength, 10)
        return True
    
    def Strength(self):
        if not self.strength or self.poisoned:
            return
      
        self.entity.strength = min(20, self.entity.strength * 2)

        if self.strength_cooldown:
            self.strength_cooldown -= 1
        else:
            self.strength -= 1
            self.strength_cooldown = random.randint(40, 60)

    # Set Strength effect, doesn't work when poisoned
    def Set_Invisibility(self, invisibility_time):

        if self.invisibility >= self.invisibility_max:
            return False
        self.invisibility = min(invisibility_time + self.invisibility, 10)
        return True
    
    def Invisibility(self):
        if not self.invisibility:
            return
        
        self.entity.active = max(0, min(255, 110 - self.invisibility * 10))

        if self.invisibility_cooldown:
            self.invisibility_cooldown -= 1
        else:
            self.invisibility -= 1
            self.invisibility_cooldown = random.randint(40, 60)
    


    #set snare effect
    def Set_Snare(self, snare_time):
        self.snared = snare_time
        return True

    def Snare(self):
        if self.snared:
            self.snared -= 1
            self.frame_movement = (0, 0)

    # Return true if healing was successfull
    def Healing(self, healing):
        if self.entity.health >= self.entity.max_health:
            return False     
        self.entity.health = min(self.entity.max_health, self.entity.health + healing)
        return True
    
     # Set Regen effect, doesn't work when poisoned
    def Set_Regen(self, regen_time):
        if self.poisoned:
            return False
        if self.regen >= self.regen_max:
            return False
        self.regen = min(regen_time + self.regen, 10)
        return True

    def Regen(self):
        if not self.regen or self.poisoned:
            return
        if self.regen_cooldown:
            self.regen_cooldown -= 1
            return
          
        self.Healing(random.randint(3, 5))
        self.regen -= 1
        self.regen_cooldown = random.randint(40, 60)
        self.Effect_Animation('regen_animation_cooldown', 'regen_animation', self.regen_animation_max, self.regen_animation_cooldown_max)


    # Slow the entity down by increasing friction
    def Slow_Down(self, effect):
        if not effect:
            return
        try:
            self.entity.max_speed = max(0.1, self.entity.max_speed / effect)
        except ZeroDivisionError as e:
            print(self.entity.max_speed, effect)
            print(f"SLOWDOWN: {e}")


    # General effect animation update, takes string input for attributes
    def Effect_Animation(self, animation_cooldown_attribute, animation_attribute, animation_max, cooldown_max):
        # Asign the attributes to temp values
        try:
            animation_cooldown = getattr(self, animation_cooldown_attribute)
            animation = getattr(self, animation_attribute)
        except Exception as e:
                print(f"Wrong effect animation input{e}", animation_cooldown_attribute, animation_attribute)

        if animation_cooldown:
            animation_cooldown -= 1
        else:
            animation_cooldown = cooldown_max
            if animation >= animation_max:
                animation = 0
            else:
                animation += 1
        
        try:
            # Overwrite the attributes with the temp values
            setattr(self, animation_cooldown_attribute, animation_cooldown)
            setattr(self, animation_attribute, animation)
        except Exception as e:
                print(f"Wrong effect animation output{e}", animation_cooldown, animation)
    
    # Render effect animations
    # TODO: Implement better animations
    def Render_Effect(self, game, surf, condition, animation, effect, offset=(0, 0)):
        if condition:
            try:
                fire_image = game.assets[effect][animation].convert_alpha()
                # Set the opacity to 70%
                fire_image.set_alpha(179)
                surf.blit(pygame.transform.flip(fire_image, self.entity.flip[0], False), (self.entity.pos[0] - offset[0] + self.entity.anim_offset[0], self.entity.pos[1] - offset[1] - 5))
            except Exception as e:
                    print(f"Wrong Render effect input{e}", condition, animation, effect)
