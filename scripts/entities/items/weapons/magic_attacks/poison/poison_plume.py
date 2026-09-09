from scripts.entities.items.weapons.magic_attacks.poison.poison_cloud import Poison_Cloud
from scripts.engine.utility.cooldown_handler import Cooldown_Handler
import random
from scripts.engine.keys.keys import keys

class Poison_Plume():
    def __init__(self, entity):
        self.entity = entity
        self.cooldown = 0
        self.cooldown_max = 40
        self.current_cloud = 0
        self.poison_clouds = []
        self.plume_cooldown_handler = Cooldown_Handler(0.4)
        

    
    def Update_Cooldown(self, delta_time):
        return self.plume_cooldown_handler.Update_Cooldown(delta_time)      

    def Update_Clouds(self):
        for cloud in self.poison_clouds:
            cloud.Update(False)
            cloud.Update_Delete_Cooldown()
            self.Remove_Cloud(cloud)
    
    def Remove_Cloud(self, cloud):
        if not cloud.delete_countdown:
            self.entity.game.entities_render.Remove_Entity(cloud)
            self.poison_clouds.remove(cloud)



    # Return False once all clouds have been spawned
    def Update(self, delta_time, power):
        self.pos = list(self.entity.pos)
        if self.current_cloud >= power * 3:
            self.current_cloud = 0
            return False
        
        if self.Update_Cooldown(delta_time):
            self.Generate_Cloud()
            self.current_cloud += 1
        
        return True
        
    
    def Generate_Cloud(self):
        fail = 0
        tile_size = self.entity.game.tilemap.tile_size
        while fail <= 5: 
            cloud_pos = (self.entity.pos[0] + random.randint(-5 * tile_size, 5 * tile_size), self.entity.pos[1] + random.randint(-5 * tile_size, 5 * tile_size))
            if self.entity.game.tilemap.solid_check(cloud_pos):
                fail += 1
                continue
            poison_cloud = Poison_Cloud(self.entity.game, cloud_pos, 1, self.entity)
            self.entity.game.entities_render.Add_Entity(poison_cloud)
            self.poison_clouds.append(poison_cloud)
            return

