from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.weapons.torch import Torch
import math

# UPDATE for throwable weapons
throwable_weapons = ['spear']

class Item_Handler():
    def __init__(self, game):
        self.game = game
        self.items = []
        self.nearby_items = []
        self.Initialise()

    def Initialise(self):
        for torch in self.game.tilemap.extract([('torch', 0)].copy()):
            self.items.append(Torch(self.game, torch['pos'], (16, 16), torch['type']))


    def Add_Item(self, item):
        self.items.append(item)


    def Remove_Item(self, item):
        self.items.remove(item)


    def find_nearby_item(self, player_pos, max_distance):
        nearby_items = []
        for item in self.items:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - item.pos[0]) ** 2 + (player_pos[1] - item.pos[1]) ** 2)
            if distance < max_distance:
                nearby_items.append(item)
        return nearby_items

    def Update(self):
        self.nearby_items = self.find_nearby_item(self.game.player.pos, 200)
        for item in self.items:
            if item.sub_type in throwable_weapons:
                try:
                    item.Throw_Weapon
                except Exception as e:
                    print(f"Item is not throwable {e}", item.sub_type)
            item.Update_Animation()
            if not item.picked_up:
                    self.items.remove(item)

    def Render(self, decorations, surf, render_scroll = (0, 0)):
        for decoration in decorations:
            decoration.Render(surf, render_scroll)