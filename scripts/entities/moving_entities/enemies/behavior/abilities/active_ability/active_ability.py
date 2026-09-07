from scripts.entities.moving_entities.enemies.behavior.abilities.ability import Ability
from scripts.engine.utility.cooldown_handler import Cooldown_Handler
from scripts.engine.keys.keys import keys
import time
COOLDOWN_TIME = 50
# Increases speed when enemy spots the player
class Active_Ability(Ability):
    def __init__(self, game, entity, name, can_attack_while_triggered=False):
        super().__init__(game, entity, name, can_attack_while_triggered, is_passive=False)
        self.ability_cooldown_handler = Cooldown_Handler(COOLDOWN_TIME)
        self.trigger_cooldown_handler = Cooldown_Handler(1)
        self.last_cooldown_update = time.time()

    def _Reset_Attack(self):
        self.ability_cooldown_handler.Set_Cooldown(COOLDOWN_TIME)

    def Update_Cooldown(self):
        current_time = time.time()
        elapsed = current_time - self.last_cooldown_update
        self.last_cooldown_update = current_time
        return self.ability_cooldown_handler.Tick(elapsed)

    # Prevents constant trigger checks
    def Check_Trigger_Cooldown(self, delta_time):
        return self.trigger_cooldown_handler.Update_Cooldown(delta_time)