from scripts.entities.decoration.decoration import Decoration
from scripts.engine.keys.keys import keys
from .crystal_caverns_registry import Register_Decoration
import pygame

DEFAULT_TRIGGER_RADIUS = 100  # Pixels padded around each side of the node

@Register_Decoration(keys.amplifying_node)
class Crystalisation_Shrine(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.crystalisation_shrine, pos, (32, 32),
                         max_animation=4, animation_cooldown_max=1.5)
        self.description = "Resonant energies\nAmplifies Runes"
        self.trigger_radius = DEFAULT_TRIGGER_RADIUS
        self.player_in_range = False
        self.effect_strength = 3

    def Update(self, delta_time):
        self.Check_Player_Distance()
        return super().Update(delta_time)

    def Check_Player_Distance(self):
        player = self.game.player
        in_range_now = player.rect().colliderect(self.rect())

        if in_range_now == self.player_in_range:
            return  # No state change — nothing to do

        self.player_in_range = in_range_now
        if in_range_now:
            player.Set_Effect(keys.power, self.effect_strength, True)
        else:
            player.Remove_Effect(keys.power, self.effect_strength)
        return
    

    def rect(self):
        return pygame.Rect(
            self.pos[0] - self.trigger_radius,
            self.pos[1] - self.trigger_radius,
            self.size[0] + (self.trigger_radius * 2),
            self.size[1] + (self.trigger_radius * 2)
        )