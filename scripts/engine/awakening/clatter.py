from scripts.engine.awakening.awakening import Awakening
from scripts.engine.utility.cooldown_handler import Cooldown_Handler
from scripts.engine.keys.keys import keys

SILENCE_MULTIPLIER = 100
CLATTER_COOLDOWN = 0.5

class Clatter():
    def __init__(self, game) -> None:
        self.game = game
        self.awakening = Awakening(game)
        self.clatter_position = None
        self.clatter_cooldown_handler = Cooldown_Handler()

    def Update(self, delta_time):
        self.awakening.Update()
        self.clatter_cooldown_handler.Tick(delta_time)

    def Generate_Clatter(self, center, clatter_range):
        if self.clatter_cooldown_handler.value > 0:
            return

        self.clatter_position = center
        self.Set_Clatter_Cooldown()

        clatter_range = self.Calculate_Silence_Modifier(clatter_range)
        self.awakening.Trigger_Awakening()

        nearby_enemies = [
            enemy for enemy in self.game.enemy_handler.Find_Nearby_Enemies(self.game.player, clatter_range)
            if enemy and not enemy.locked_on_target
        ]

        for enemy in nearby_enemies:
            self.game.enemy_handler.Add_To_Pathfinding_Queue(enemy, center)

        self.game.enemy_handler.clatter_subscription.Broadcast_Clatter(center)

    def Check_Clatter_Cooldown(self):
        return self.clatter_cooldown_handler.value > 0

    def Set_Clatter_Cooldown(self):
        self.clatter_cooldown_handler.Set_Cooldown(CLATTER_COOLDOWN)

    def Increase_Awakening(self):
        self.awakening.Set_Awakening_Level(self.awakening.awakening_level + 1)

    def Get_Awakening_Level(self):
        return self.awakening.awakening_level

    def Calculate_Silence_Modifier(self, clatter_range):
        if self.game.player.active_ability == keys.silence:
            silence_effect = self.game.player.Get_Effect(keys.silence)
            clatter_range = max(1, clatter_range - silence_effect.effect_strength * SILENCE_MULTIPLIER)

        return clatter_range
        

    def Reset_Awakening_Level(self):
        self.awakening.awakening_cooldown = 0
        self.awakening.Set_Awakening_Level(0)