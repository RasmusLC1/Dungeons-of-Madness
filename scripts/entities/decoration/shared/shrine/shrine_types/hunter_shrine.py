from scripts.entities.decoration.shared.shrine.shrine import Shrine
from scripts.entities.decoration.shared.shrine.shrine_reward_pools import GOOD_REWARDS
from scripts.engine.keys.keys import keys
from scripts.entities.decoration.shared.shared_registry import Register_Decoration
from scripts.entities.decoration.shared.shrine.shrine_registry import Register_Shrine
import random

Register_Shrine(keys.hunter_shrine)
@Register_Decoration(keys.hunter_shrine)
class Hunter_Shrine(Shrine):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.hunter_shrine, pos, (64, 64), max_animation=1)
        self.description = "Return the\ntreasure for\nreward"
        self.treasures = []

    def Open(self, generate_clatter=False):
        if self.empty:
            return False
        self.empty = True
        self.Set_Animation(1)
        self.Set_Sprite()
        self.Spawn_Treasure()
        self.Activate_Shrine()
        return True

    def Spawn_Treasure(self):
        self.game.sound_handler.Play_Sound(keys.hunter_shrine_activation, 0.4)
        fail = 0
        for i in range(3):
            tile = self.game.tilemap.Get_Random_Tile_With_Path_To_Player()
            if not tile:
                print("TILE NOT FOUND, HUNTER SHRINE")
                fail += 1
                if fail > 10:
                    return
                continue
            treasure = self.game.item_handler.Spawn_Item_By_Type(keys.valuable, tile.scaled_pos, type=keys.hunter_treasure)
            if not treasure:
                print("Treasure not spawned, HUNTER SHRINE")
                return
            self.treasures.append(treasure)

    def Spawn_Reward(self, item):
        if self.animation != 1 or item.type != keys.hunter_treasure:
            return False

        self.Activate_Shrine()
        self.animation_handler.Set_Static_Animation(2)
        self.game.item_handler.Remove_Item(item, True)
        reward, amount = random.choice(list(GOOD_REWARDS.items()))
        self.game.player.Set_Effect(reward, amount, True)
        self.game.sound_handler.Play_Sound(keys.collapse, 0.4)
        self.game.clatter.Generate_Clatter(self.pos, 1000)

        for treasure in list(self.treasures):
            self.treasures.remove(treasure)
            self.game.item_handler.Remove_Item(treasure, True)
        return True