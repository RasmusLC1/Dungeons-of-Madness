from scripts.entities.items.weapons.weapon_handler import Weapon_Handler
from scripts.entities.items.runes.rune_handler import Rune_Handler
from scripts.entities.items.loot.loot_handler import Loot_Handler
from scripts.engine.utility.cooldown_handler import Cooldown_Handler
import pygame
from scripts.engine.keys.keys import keys


class Item_Handler():
    def __init__(self, game):
        self.game = game
        self.items = []
        self.nearby_items = []
        self.nearby_item_cooldown_handler = Cooldown_Handler(0.5)
        self.saved_data = {}
        self.weapon_handler = Weapon_Handler(self.game, self)
        self.loot_handler = Loot_Handler(self.game, self)
        self.rune_handler = Rune_Handler(self.game, self)


    def Save_Item_Data(self):
        for item in self.items:
            item.Save_Data()
            self.saved_data[item.ID] = item.saved_data


    def Load_Data(self, data):
        for ID, item_data in data.items():
            if not item_data:
                continue

            self.Load_Item_From_Data(item_data)

    def Load_Item_From_Data(self, item_data):
        try:
            type = item_data[keys.type]
            pos = item_data[keys.pos]
            amount = item_data['amount']
            item = None
            if item_data['sub_category'] == keys.weapon:
                item = self.weapon_handler.Weapon_Spawner(type, pos[0], pos[1], data=item_data)
            elif item_data['sub_category'] == keys.loot:
                loot_type = item_data[keys.loot_type]
                item = self.loot_handler.Spawn_Loot_Type(loot_type, pos, item_data)
            elif item_data['sub_category'] == keys.rune:
                item = self.rune_handler.Load_Data(item_data)
            else:
                return None
            
            return item
        except Exception as e:
            print("DATA WRONG ITEM HANDLER", item_data, e)


    def Clear_Items(self):
        self.items.clear()
        self.nearby_items.clear()
        self.saved_data.clear()
        self.rune_handler.Clear_Runes()


    def Initialise(self):
        for gold in self.game.tilemap.extract([(keys.gold, 0)].copy()):
            gold = self.loot_handler.Spawn_Loot_Type(keys.valuable, gold[keys.pos], type = keys.gold)
            if gold:
                self.Add_Item(gold)

        self.rune_handler.Initialise_Runes()
        
# RUNE LOGIC
    def Spawn_Rune(self, pos, type = None, rarity_value = None):
        return self.rune_handler.Loot_Spawner(pos, type, rarity_value)
    
    def Remove_Rune_From_Active_Runes(self, rune):
        return self.rune_handler.Remove_Rune_From_Active_Runes(rune)
    
    def Get_Active_Runes(self):
        return self.rune_handler.Get_Active_Runes()
    
    def Replace_Rune_In_Inventory(self, rune_to_replace, new_rune):
        return self.rune_handler.Replace_Rune_In_Inventory(rune_to_replace, new_rune)
    
    def Check_For_Damage_Rune(self):
        return self.rune_handler.Check_If_Player_Has_Damage_Runes()
    
# WEAPON LOGIC
    def Spawn_Weapon(self, pos, type = None):
        weapon = None
        if type:
            weapon = self.weapon_handler.Weapon_Spawner(type, pos[0], pos[1])
        else:
            weapon = self.weapon_handler.Spawn_Random_Weapon(pos)

        return weapon
    
    def Spawn_Arrow_For_Trap(self, pos):
        return self.weapon_handler.Spawn_Arrow_For_Trap(pos)

    def Add_Item(self, item):
        if item in self.items:
            return
        self.items.append(item)

    
    def Find_Item(self, ID):
        for item in self.items:
            if item.ID == ID:
                return item
        
        return None
    
    def Get_Gems_For_Weapon(self, value):
        return self.loot_handler.Get_Gems_For_Weapon(value)

    def Remove_Item(self, item, delete_item = False):
        if not item in self.items:
            return
        
        self.items.remove(item)
        self.game.entities_render.Remove_Entity(item)
        self.game.tilemap.Remove_Entity_From_Tile(item.tile, item.ID)
        if delete_item:
            item.Delete()


    def Find_Nearby_Item(self, entity_pos, max_distance):
        nearby_items = []
        if max_distance <= 5:
            nearby_items = self.game.tilemap.Search_Nearby_Tiles(max_distance, entity_pos, keys.item)
        else:
            nearby_items = self.Search_For_Nearby_Items(entity_pos, max_distance)
        
        return nearby_items

    def Search_For_Nearby_Items(self, entity_pos, max_distance):
        nearby_items = []
        max_distance_squared = max_distance * max_distance
        for item in self.items:
            # Calculate the Euclidean distance
            dx = entity_pos[0] - item.pos[0]
            dy = entity_pos[1] - item.pos[1]
            distance = dx*dx + dy*dy
            if distance < max_distance_squared:
                nearby_items.append(item)

        return nearby_items

    def Update(self, delta_time):
        self.Check_Keyboard_Input()
        if self.nearby_item_cooldown_handler.Update_Cooldown(delta_time):
            self.nearby_items.clear()
            self.nearby_items = self.Find_Nearby_Item(self.game.player.pos, 3)

        picked_up_items = []
        for item in self.items:
            item.Update_Delete_Cooldown(delta_time)

            if item.picked_up:
                picked_up_items.append(item)
                continue

            self.Throw_Projectile(item, delta_time)

        for item in picked_up_items:
            self.items.remove(item)

        self.rune_handler.Update(delta_time)

    
    # Shoot projectiles
    def Throw_Projectile(self, item, delta_time):
        if not item.is_projectile:
            return
        if not item.special_attack:
            
            if not item.entity:
                return
            if item.shoot_speed and item.entity.category == keys.enemy and not item.delete_countdown:
                item.Set_Delete_Countdown(0.2)
                return
        try:
            if not item in self.items:
                return
            item.Shoot(delta_time)
        except Exception as e:
            print(f"Item is not throwable {e}", item.type, item.entity, item.tile, vars(item))

    def Check_Keyboard_Input(self):
        if self.game.keyboard_handler.is_key_pressed(pygame.K_e):
            if not self.Pick_Up_Items(2):
                return
            else:
                self.game.keyboard_handler.Set_E_Key(False)
    
    def Pick_Up_Items(self, distance) -> bool:
        nearby_items = self.Find_Nearby_Item(self.game.player.pos, distance)
        # Remove items that have been picked up already, prevents inventory problems
        for item in nearby_items:
            if item.picked_up:
                nearby_items.remove(item)
        if not nearby_items:
            return None
        player_pos = self.game.player.pos
        nearby_items.sort(key=lambda decoration: (player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
        return nearby_items[0].Pick_Up()
        
    
    def Pick_Up_All_Nearby_Items(self, distance) -> bool:
        nearby_items = self.Find_Nearby_Item(self.game.player.pos, distance)
        if not nearby_items:
            return False

        for item in nearby_items:
            if item.type == 'torch':
                continue
            item.Pick_Up()
        return True

    def Reset_Nearby_Items_Cooldown(self):
        self.nearby_item_cooldown_handler.Set_Cooldown(0.001)

    def Update_Nearby_Items_Cooldown(self, delta_time):
        if self.nearby_item_cooldown:
            self.nearby_item_cooldown = max(0, self.nearby_item_cooldown - delta_time)
            return False
        self.nearby_item_cooldown = 0.5
        return True


    def Find_Items_In_Inventory(self, index):
        for item in self.items:
            if not item.inventory_index:
                return
            if item.inventory_index == index:
                return item
            
    # Returns a list of all item_types that can be spawned
    def Check_If_Loot_Is_Affordable(self, item_types, rarity_value):
        return self.loot_handler.Check_If_Loot_Is_Affordable(item_types, rarity_value)
    
    def Spawn_Item_By_Type(self, category, pos, type = None, rarity_value = 0):
        self.loot_handler.Spawn_Loot_Type(category, pos, type = type, rarity_value = rarity_value)