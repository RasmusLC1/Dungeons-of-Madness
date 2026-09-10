import pygame
from scripts.engine.utility.utils import load_image, load_images, Animation, get_tiles_from_sheet
from scripts.engine.keys.keys import keys


class Graphics_Loader:
    def Run_All(self):
        Graphics_Loader.Asset_Background_List(self)
        Graphics_Loader.Asset_Crypt_Tile_List(self)
        Graphics_Loader.Asset_Crystal_Cavern_Tile_List(self)
        Graphics_Loader.Asset_Trap_List(self)
        Graphics_Loader.Asset_Effect_List(self)
        Graphics_Loader.Asset_Magic_Attack_List(self)
        Graphics_Loader.Enemy_Assets(self)
        Graphics_Loader.Asset_Player_List(self)
        Graphics_Loader.Asset_Interative_Objects_List(self)
        Graphics_Loader.Glowing_Crystals_List(self)
        Graphics_Loader.Crystal_Cavern_Decorations(self)
        Graphics_Loader.Asset_Environment_List(self)
        Graphics_Loader.Asset_Potion_List(self)
        Graphics_Loader.Asset_Decoration_List(self)
        Graphics_Loader.Asset_Weapons_List(self)
        Graphics_Loader.Asset_magic_staffs_List(self)
        Graphics_Loader.Asset_Weapons_Effects(self)
        Graphics_Loader.Asset_Inventory(self)
        Graphics_Loader.Asset_Font(self)
        Graphics_Loader.Asset_Loot(self)
        Graphics_Loader.Asset_Keys(self)
        Graphics_Loader.Asset_Gems(self)
        Graphics_Loader.Asset_Ingots(self)
        Graphics_Loader.Asset_Bombs(self)
        Graphics_Loader.Asset_Rune(self)
        Graphics_Loader.Asset_Menu(self)
        
        Graphics_Loader.Asset_UI(self)
        Graphics_Loader.Asset_Particles_List(self)
        Graphics_Loader.Asset_Tooltips(self)


    def Enemy_Assets(self):
        Graphics_Loader.Add_Skeletons(self)
        Graphics_Loader.Asset_Fire_Spirit_List(self)
        Graphics_Loader.Asset_Ice_Spirit_List(self)
        Graphics_Loader.Asset_Earth_Elemental_List(self)
        Graphics_Loader.Asset_Electric_Elemental_List(self)
        Graphics_Loader.Asset_Poison_Elemental_List(self)
        Graphics_Loader.Asset_Void_Spawn_List(self)
        Graphics_Loader.Wight_King_List(self)
        Graphics_Loader.Asset_Spider_List(self)
        Graphics_Loader.Asset_Ghoul_List(self)
        Graphics_Loader.Asset_Enemy_Symbols_List(self)
        Graphics_Loader.Asset_vampire_List(self)
        Graphics_Loader.Asset_minotaur_List(self)
        Graphics_Loader.Asset_medusa_List(self)
        Graphics_Loader.Asset_Clicker_List(self)
    
    def Asset_Background_List(self):
        background_assets = {'background': load_image('background.png'),}
        self.assets.update(background_assets)
    
    def Add_Skeletons(self):
        Graphics_Loader.Asset_Skeleton_Warrior_List(self)
        Graphics_Loader.Asset_Skeleton_Guardian_List(self)
        Graphics_Loader.Asset_Skeleton_Banner_Bearer_List(self)
        Graphics_Loader.Asset_Skeleton_Ranger_List(self)
        Graphics_Loader.Asset_Skeleton_Bell_Toller_List(self)
        Graphics_Loader.Asset_Skeleton_Cleric_List(self)
        Graphics_Loader.Asset_Skeleton_Undertaker_List(self)
        Graphics_Loader.Asset_Skeleton_Warlock_List(self)
        
        Graphics_Loader.Add_Placeholder_Idle_Animations(self)


    def Add_Placeholder_Idle_Animations(self):
        new_assets = {}
        for key, value in self.assets.items():
            # Only create idle animations for skeletons with running animations
            if 'skeleton' in key and 'running' in key:
                idle_key = key.replace('running', 'idle')
                new_assets[idle_key] = value  # copy same frames
        self.assets.update(new_assets)


    def Asset_Crypt_Tile_List(self):
        tiles_assets = {
            keys.crypt_floor : get_tiles_from_sheet('tile_set/crypt/floor.png', 5, 1, 0, 0, 32, 32),
            keys.crypt_wall_top : get_tiles_from_sheet('tile_set/crypt/wall_top.png', 3, 0, 0, 0, 32, 32),
            keys.crypt_wall_left : get_tiles_from_sheet('tile_set/crypt/wall_left.png', 0, 3, 0, 0, 32, 32),
            keys.crypt_wall_right : get_tiles_from_sheet('tile_set/crypt/wall_right.png', 0, 3, 0, 0, 32, 32),
            keys.crypt_wall_middle : get_tiles_from_sheet('tile_set/crypt/wall_middle.png', 0, 3, 0, 0, 32, 32),
            keys.crypt_wall_bottom : get_tiles_from_sheet('tile_set/crypt/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            keys.crypt_wall_bottom_corner : get_tiles_from_sheet('tile_set/crypt/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Crystal_Cavern_Tile_List(self):
        tiles_assets = {
            keys.crystal_cavern_floor : get_tiles_from_sheet('tile_set/crystal_cavern/floor.png', 5, 1, 0, 0, 32, 32),
            keys.crystal_cavern_wall_top : get_tiles_from_sheet('tile_set/crystal_cavern/wall_top.png', 3, 0, 0, 0, 32, 32),
            keys.crystal_cavern_wall_left : get_tiles_from_sheet('tile_set/crystal_cavern/wall_left.png', 0, 3, 0, 0, 32, 32),
            keys.crystal_cavern_wall_right : get_tiles_from_sheet('tile_set/crystal_cavern/wall_right.png', 0, 3, 0, 0, 32, 32),
            keys.crystal_cavern_wall_middle : get_tiles_from_sheet('tile_set/crystal_cavern/wall_middle.png', 0, 3, 0, 0, 32, 32),
            keys.crystal_cavern_wall_bottom : get_tiles_from_sheet('tile_set/crystal_cavern/wall_bottom.png', 3, 0, 0, 0, 32, 32),
            keys.crystal_cavern_wall_bottom_corner : get_tiles_from_sheet('tile_set/crystal_cavern/wall_bottom_corner.png', 2, 0, 0, 0, 32, 32),
        }
        self.assets.update(tiles_assets)

    def Asset_Trap_List(self):
        trap_assets = {
            keys.spike_trap : get_tiles_from_sheet('decoration/traps/spike_trap.png', 6, 0, 0, 0, 32, 32),
            keys.spike_poison_trap : get_tiles_from_sheet('decoration/traps/Spike_Trap_poison.png', 13, 0, 0, 0, 32, 32),
            keys.pit_trap : get_tiles_from_sheet('decoration/traps/Pit_Trap_Spikes.png', 1, 0, 0, 0, 32, 32),
            keys.fire_trap : get_tiles_from_sheet('decoration/traps/Fire_Trap.png', 13, 0, 0, 0, 32, 20),
            keys.spider_web : get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_web.png', 3, 0, 0, 0, 32, 32),
            keys.poison_plume : get_tiles_from_sheet('decoration/traps/poison_plume.png', 7, 0, 0, 0, 32, 32),
            keys.rubble : get_tiles_from_sheet('decoration/traps/rubble.png', 3, 0, 0, 0, 32, 32),
            keys.pressure_plate : get_tiles_from_sheet('decoration/traps/pressure_plate.png', 0, 0, 0, 0, 32, 32),
            keys.arrow_trap : get_tiles_from_sheet('decoration/traps/arrow_trap.png', 0, 0, 0, 0, 32, 32),
            keys.soul_trap : get_tiles_from_sheet('decoration/traps/soul_trap.png', 1, 0, 0, 0, 32, 32),
        }

        self.assets.update(trap_assets)

    def Asset_Particles_List(self):
        effect_assets = {
            keys.dash_particle : get_tiles_from_sheet('particles/general/dash.png', 5, 0, 0, 0, 5, 5),
            keys.fire_particle : get_tiles_from_sheet('particles/general/fire.png', 5, 0, 0, 0, 3, 3),
            keys.electric_particle : get_tiles_from_sheet('particles/general/spark.png', 5, 0, 0, 0, 3, 3),
            keys.blood_particle : get_tiles_from_sheet('particles/general/blood.png', 5, 0, 0, 0, 3, 3),
            keys.bone_particle : get_tiles_from_sheet('particles/general/bone.png', 5, 0, 0, 0, 3, 3),
            keys.electric_particle : get_tiles_from_sheet('particles/general/electric.png', 5, 0, 0, 0, 3, 3),
            keys.frost_particle : get_tiles_from_sheet('particles/general/frost.png', 5, 0, 0, 0, 3, 3),
            keys.gold_particle : get_tiles_from_sheet('particles/general/gold.png', 5, 0, 0, 0, 3, 3),
            keys.poison_particle : get_tiles_from_sheet('particles/general/poison.png', 5, 0, 0, 0, 3, 3),
            keys.vampire_particle : get_tiles_from_sheet('particles/general/vampire.png', 5, 0, 0, 0, 3, 3),
            keys.soul_particle : get_tiles_from_sheet('particles/general/soul.png', 5, 0, 0, 0, 3, 3),
            keys.player_particle : get_tiles_from_sheet('particles/general/player.png', 5, 0, 0, 0, 3, 3),
            keys.loot_particle : get_tiles_from_sheet('particles/general/loot.png', 5, 0, 0, 0, 3, 3),
            keys.strength_particle : get_tiles_from_sheet('particles/general/strength.png', 5, 0, 0, 0, 3, 3),
        }
        self.assets.update(effect_assets)

    def Asset_Effect_List(self):
        effect_assets = {
            keys.fire : get_tiles_from_sheet('particles/effects/fire/orange/loops/burning_loop_1.png', 7, 0, 0, 0, 32, 32),
            keys.poison : get_tiles_from_sheet('particles/effects/poison.png', 2, 0, 0, 0, 32, 32),
            keys.frozen : get_tiles_from_sheet('particles/effects/frozen.png', 2, 0, 0, 0, 32, 32),
            keys.wet : get_tiles_from_sheet('particles/effects/wet.png', 2, 0, 0, 0, 32, 32),
            keys.regen : get_tiles_from_sheet('particles/effects/regen.png', 2, 1, 0, 0, 32, 32),
            keys.electric : get_tiles_from_sheet('particles/effects/electric.png', 5, 0, 0, 0, 32, 32),
            keys.invulnerable : get_tiles_from_sheet('particles/effects/invincible.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(effect_assets)
    
    def Asset_Magic_Attack_List(self):
        particle_assets = {
       keys.fire_particle_attack : get_tiles_from_sheet('items/weapons/magic_attacks/fire/fire_particle.png', 3, 0, 0, 0, 4, 4),
       keys.fire_ball : get_tiles_from_sheet('items/weapons/magic_attacks/fire/fire_ball.png', 0, 0, 0, 0, 16, 16),
       keys.fire_explosion : get_tiles_from_sheet('items/weapons/magic_attacks/fire/fire_explosion.png', 7, 0, 0, 0, 32, 32),

       keys.ice_particle_attack : get_tiles_from_sheet('items/weapons/magic_attacks/ice/ice_particle.png', 3, 0, 0, 0, 4, 4),
       keys.ice_ball : get_tiles_from_sheet('items/weapons/magic_attacks/ice/ice_ball.png', 0, 0, 0, 0, 16, 16),
       keys.ice_explosion : get_tiles_from_sheet('items/weapons/magic_attacks/ice/ice_explosion.png', 5, 0, 0, 0, 32, 32),
       keys.ice_storm : get_tiles_from_sheet('items/weapons/magic_attacks/ice/ice_storm.png', 9, 0, 0, 0, 32, 32),

       keys.poison_particle_attack : get_tiles_from_sheet('items/weapons/magic_attacks/poison/poison_particle.png', 3, 0, 0, 0, 4, 4),
       keys.poison_ball : get_tiles_from_sheet('items/weapons/magic_attacks/poison/poison_ball.png', 0, 0, 0, 0, 16, 16),
       keys.poison_explosion : get_tiles_from_sheet('items/weapons/magic_attacks/poison/poison_explosion.png', 5, 0, 0, 0, 32, 32),
       keys.poison_cloud : get_tiles_from_sheet('items/weapons/magic_attacks/poison/poison_cloud.png', 3, 0, 0, 0, 32, 32),


       keys.electric_particle_attack : get_tiles_from_sheet('items/weapons/magic_attacks/electric/electric_particle.png', 3, 0, 0, 0, 16, 16),
       keys.electric_ball : get_tiles_from_sheet('items/weapons/magic_attacks/electric/electric_ball.png', 0, 0, 0, 0, 16, 16),
       keys.electric_explosion : get_tiles_from_sheet('items/weapons/magic_attacks/electric/electric_explosion.png', 5, 0, 0, 0, 32, 32),

        keys.soul_reap : get_tiles_from_sheet('items/weapons/magic_attacks/vampiric/soul_reap.png', 0, 0, 0, 0, 32, 32),
        keys.vampiric_ball : get_tiles_from_sheet('items/weapons/magic_attacks/vampiric/vampiric_ball.png', 0, 0, 0, 0, 16, 16),
        keys.soul_pit : get_tiles_from_sheet('items/weapons/magic_attacks/vampiric/soul_pit.png', 6, 0, 0, 0, 32, 32),
        
        }
        self.assets.update(particle_assets)


    def Asset_Player_List(self):
        entities_assets = {

            keys.player_idle : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_idle.png', 3, 0, 0, 0, 32, 32),
            keys.player_idle_up : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_idle.png', 3, 0, 0, 0, 32, 32),
            keys.player_standing_still_down : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_idle.png', 3, 0, 0, 0, 32, 32),
            keys.player_standing_still_up : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_idle.png', 3, 0, 0, 0, 32, 32),
            keys.player_running_down : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_running.png', 5, 0, 0, 0, 32, 32),
            keys.player_running_up : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_running_behind.png', 5, 0, 0, 0, 32, 32),
            keys.player_rolling : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_rolling.png', 4, 0, 0, 0, 32, 32),
            keys.player_backstep : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_rolling.png', 4, 0, 0, 0, 32, 32),
            keys.player_stab : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_attack_stab.png', 4, 0, 0, 0, 48, 48),
            keys.player_cut : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_attack_slash.png', 4, 0, 0, 0, 48, 48),
            keys.player_two_hand : get_tiles_from_sheet('entities/enemies/mythical/kobold/kobold_red/kobold_attack_two_hand.png', 4, 0, 0, 0, 48, 48),


        }
        
        self.assets.update(entities_assets)


    def Asset_Kobold_List(self):
        entities_assets = {

            keys.player_idle : get_tiles_from_sheet('entities/player/idle.png', 4, 0, 0, 0, 32, 32),
            keys.player_idle_up : get_tiles_from_sheet('entities/player/idle_up.png', 4, 0, 0, 0, 32, 32),
            keys.player_standing_still_down : get_tiles_from_sheet('entities/player/standing_still_down.png', 4, 0, 0, 0, 32, 32),
            keys.player_standing_still_up : get_tiles_from_sheet('entities/player/standing_still_up.png', 4, 0, 0, 0, 32, 32),
            keys.player_running_down : get_tiles_from_sheet('entities/player/running_down.png', 5, 0, 0, 0, 32, 32),
            keys.player_running_up : get_tiles_from_sheet('entities/player/running_up.png', 5, 0, 0, 0, 32, 32),
            keys.player_attack : get_tiles_from_sheet('entities/player/player_attack.png', 4, 0, 0, 0, 32, 32),


        }
        
        self.assets.update(entities_assets)


    def Asset_Skeleton_Warrior_List(self):
        entities_assets = {
            keys.skeleton_warrior_1_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_1_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_1_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_warrior_2_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_2.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_2_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_2_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_warrior_3_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_3.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_warrior_3_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warrior/skeleton_warrior_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Guardian_List(self):
        entities_assets = {
            keys.skeleton_guardian_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_guardian/skeleton_guardian.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_guardian_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_guardian/skeleton_guardian_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Banner_Bearer_List(self):
        entities_assets = {
            keys.skeleton_banner_bearer_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_banner_bearer/skeleton_banner_bearer.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_banner_bearer_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_banner_bearer/skeleton_banner_bearer_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Ranger_List(self):
        entities_assets = {
            keys.skeleton_ranger_1_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_1.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_1_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_1_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_ranger_2_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_2.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_2_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_2_attack.png', 6, 0, 0, 0, 32, 32),

            keys.skeleton_ranger_3_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_3.png', 5, 0, 0, 0, 32, 32),
            keys.skeleton_ranger_3_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_ranger/skeleton_ranger_3_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)


    def Asset_Skeleton_Warlock_List(self):
        entities_assets = {
            keys.skeleton_warlock_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warlock/skeleton_warlock.png', 3, 0, 0, 0, 32, 32),
            keys.skeleton_warlock_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_warlock/skeleton_warlock_attack.png', 4, 0, 0, 0, 32, 32),

        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Cleric_List(self):
        entities_assets = {
            keys.skeleton_cleric_1_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_cleric/skeleton_cleric_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_cleric_1_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_cleric/skeleton_cleric_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Bell_Toller_List(self):
        entities_assets = {
            keys.skeleton_bell_toller_1_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_bell/skeleton_bell_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_bell_toller_1_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_bell/skeleton_bell_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Skeleton_Undertaker_List(self):
        entities_assets = {
            keys.skeleton_undertaker_1_running: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_undertaker/skeleton_undertaker_1.png', 6, 0, 0, 0, 32, 32),
            keys.skeleton_undertaker_1_attack: get_tiles_from_sheet('entities/enemies/skeleton/skeleton_undertaker/skeleton_undertaker_attack_1.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Wight_King_List(self):
        entities_assets = {
            keys.wight_king_idle: get_tiles_from_sheet('entities/enemies/skeleton/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),
            keys.wight_king_running: get_tiles_from_sheet('entities/enemies/skeleton/wight_king/wight_king.png', 4, 0, 0, 0, 40, 40),
            keys.wight_king_attack: get_tiles_from_sheet('entities/enemies/skeleton/wight_king/wight_king_attack.png', 6, 0, 0, 0, 40, 40),
        }
        self.assets.update(entities_assets)


    def Asset_Fire_Spirit_List(self):
        entities_assets = {
            keys.fire_spirit_idle: get_tiles_from_sheet('entities/enemies/elementals/fire_spirit/fire_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            keys.fire_spirit_running: get_tiles_from_sheet('entities/enemies/elementals/fire_spirit/fire_spirit_moving.png', 3, 0, 0, 0, 32, 32),
            keys.fire_spirit_attack: get_tiles_from_sheet('entities/enemies/elementals/fire_spirit/fire_spirit_attacking.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Ice_Spirit_List(self):
        entities_assets = {
            keys.ice_spirit: get_tiles_from_sheet('entities/enemies/elementals/ice_spirit/ice_spirit_idle.png', 3, 0, 0, 0, 32, 32),
            keys.ice_spirit_attack: get_tiles_from_sheet('entities/enemies/elementals/ice_spirit/ice_spirit_moving.png', 3, 0, 0, 0, 32, 32),
            keys.ice_spirit_running: get_tiles_from_sheet('entities/enemies/elementals/ice_spirit/ice_spirit_attacking.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Earth_Elemental_List(self):
        entities_assets = {
            keys.earth_elemental: get_tiles_from_sheet('entities/enemies/elementals/earth_elemental/earth_elemental_idle.png', 3, 0, 0, 0, 48, 48),
            keys.earth_elemental_running: get_tiles_from_sheet('entities/enemies/elementals/earth_elemental/earth_elemental_running.png', 3, 0, 0, 0, 48, 48),
            keys.earth_elemental_attack: get_tiles_from_sheet('entities/enemies/elementals/earth_elemental/earth_elemental_attack.png', 3, 0, 0, 0, 48, 48),
        }
        self.assets.update(entities_assets)

    def Asset_medusa_List(self):
        entities_assets = {
            keys.medusa: get_tiles_from_sheet('entities/enemies/mythical/medusa/IDLE.png', 5, 0, 0, 0, 150, 150),
            keys.medusa_running: get_tiles_from_sheet('entities/enemies/mythical/medusa/MOVE.png', 3, 0, 0, 0, 150, 150),
            keys.medusa_attack_direct: get_tiles_from_sheet('entities/enemies/mythical/medusa/ATTACK1.png', 5, 0, 0, 0, 150, 150),
            keys.medusa_attack_ranged: get_tiles_from_sheet('entities/enemies/mythical/medusa/ATTACK2.png', 5, 0, 0, 0, 150, 150),
        }
        self.assets.update(entities_assets)

    def Asset_Clicker_List(self):
        entities_assets = {
            keys.clicker_running: get_tiles_from_sheet('entities/enemies/dwellers/clicker/clicker.png', 4, 0, 0, 0, 32, 32),
            keys.clicker_attack: get_tiles_from_sheet('entities/enemies/dwellers/clicker/clicker_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_minotaur_List(self):
        entities_assets = {
            keys.minotaur: get_tiles_from_sheet('entities/enemies/mythical/minotaur/minotaur_idle.png', 3, 0, 0, 0, 64, 64),
            keys.minotaur_running: get_tiles_from_sheet('entities/enemies/mythical/minotaur/minotaur_running.png', 3, 0, 0, 0, 64, 64),
            keys.minotaur_attack: get_tiles_from_sheet('entities/enemies/mythical/minotaur/minotaur_attacking.png', 5, 0, 0, 0, 64, 64),
        }
        self.assets.update(entities_assets)

    def Asset_Electric_Elemental_List(self):
        entities_assets = {
            keys.electric_elemental: get_tiles_from_sheet('entities/enemies/elementals/electric_elemental/electric_elemental_idle.png', 3, 0, 0, 0, 32, 32),
            keys.electric_elemental_running: get_tiles_from_sheet('entities/enemies/elementals/electric_elemental/electric_elemental_running.png', 3, 0, 0, 0, 32, 32),
            keys.electric_elemental_attack: get_tiles_from_sheet('entities/enemies/elementals/electric_elemental/electric_elemental_attack.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Poison_Elemental_List(self):
        entities_assets = {
            keys.poison_elemental: get_tiles_from_sheet('entities/enemies/elementals/poison_elemental/poison_elemental_idle.png', 3, 0, 0, 0, 32, 32),
            keys.poison_elemental_running: get_tiles_from_sheet('entities/enemies/elementals/poison_elemental/poison_elemental_running.png', 3, 0, 0, 0, 32, 32),
            keys.poison_elemental_attack: get_tiles_from_sheet('entities/enemies/elementals/poison_elemental/poison_elemental_attack.png', 3, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)
    

    def Asset_vampire_List(self):
        entities_assets = {
            keys.vampire_running: get_tiles_from_sheet('entities/enemies/dwellers/vampire/vampire.png', 3, 0, 0, 0, 32, 32),
            keys.vampire_attack: get_tiles_from_sheet('entities/enemies/dwellers/vampire/vampire_attack.png', 6, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Void_Spawn_List(self):
        entities_assets = {
            keys.wraith_idle: get_tiles_from_sheet('entities/enemies/void_spawn/wraith/wraith.png', 4, 0, 0, 0, 32, 32),
            keys.wraith_running: get_tiles_from_sheet('entities/enemies/void_spawn/wraith/wraith.png', 4, 0, 0, 0, 32, 32),
            keys.wraith_attack: get_tiles_from_sheet('entities/enemies/void_spawn/wraith/wraith_attack.png', 5, 0, 0, 0, 32, 32),

            keys.phantom_idle: get_tiles_from_sheet('entities/enemies/void_spawn/phantom/phantom.png', 4, 0, 0, 0, 32, 32),
            keys.phantom_running: get_tiles_from_sheet('entities/enemies/void_spawn/phantom/phantom.png', 4, 0, 0, 0, 32, 32),
            keys.phantom_attack: get_tiles_from_sheet('entities/enemies/void_spawn/phantom/phantom_attack.png', 5, 0, 0, 0, 32, 32),

            keys.shade_idle: get_tiles_from_sheet('entities/enemies/void_spawn/shade/shade.png', 4, 0, 0, 0, 32, 32),
            keys.shade_running: get_tiles_from_sheet('entities/enemies/void_spawn/shade/shade.png', 4, 0, 0, 0, 32, 32),
            keys.shade_attack: get_tiles_from_sheet('entities/enemies/void_spawn/shade/shade_attack.png', 5, 0, 0, 0, 32, 32),

            keys.rift_stalker_idle: get_tiles_from_sheet('entities/enemies/void_spawn/rift_stalker/rift_stalker.png', 4, 0, 0, 0, 32, 32),
            keys.rift_stalker_running: get_tiles_from_sheet('entities/enemies/void_spawn/rift_stalker/rift_stalker.png', 4, 0, 0, 0, 32, 32),
            keys.rift_stalker_attack: get_tiles_from_sheet('entities/enemies/void_spawn/rift_stalker/rift_stalker_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Ghoul_List(self):
        entities_assets = {
            keys.ghoul_running: get_tiles_from_sheet('entities/enemies/dwellers/ghoul/ghoul.png', 4, 0, 0, 0, 32, 32),
            keys.ghoul_attack: get_tiles_from_sheet('entities/enemies/dwellers/ghoul/ghoul_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Spider_List(self):
        entities_assets = {
            keys.spider_idle: get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_idle.png', 4, 0, 0, 0, 32, 32),
            keys.spider_running: get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_running.png', 4, 0, 0, 0, 32, 32),
            keys.friendly_spider_idle: get_tiles_from_sheet('entities/enemies/dwellers/spider/friendly_spider_idle.png', 4, 0, 0, 0, 32, 32),
            keys.friendly_spider_running: get_tiles_from_sheet('entities/enemies/dwellers/spider/friendly_spider_running.png', 4, 0, 0, 0, 32, 32),
            keys.spider_attack: get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_attacking.png', 3, 0, 0, 0, 32, 32),
            keys.spider_jumping: get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_jumping.png', 8, 0, 0, 0, 32, 32),
            keys.spider_on_back: get_tiles_from_sheet('entities/enemies/dwellers/spider/spider_on_back.png', 8, 0, 0, 0, 32, 32),
        }
        self.assets.update(entities_assets)

    def Asset_Enemy_Symbols_List(self):
        symbols_assets = {
            keys.exclamation_mark: get_tiles_from_sheet('entities/enemies/symbols/exclamation.png', 0, 0, 0, 0, 16, 16),
            keys.health_bar: get_tiles_from_sheet('entities/enemies/symbols/health_bar.png', 9, 0, 0, 0, 32, 16),
            keys.crystal_scale_bar: get_tiles_from_sheet('entities/enemies/symbols/crystal_scale_bar.png', 9, 0, 0, 0, 32, 16),
        }
        self.assets.update(symbols_assets)

    def Asset_magic_staffs_List(self):
        Weapons_assets = {
            keys.fire_staff: get_tiles_from_sheet('items/weapons/staff/fire_staff.png', 0, 0, 0, 0, 32, 32),
            keys.fire_staff_attack_cut: get_tiles_from_sheet('items/weapons/staff/fire_staff_attack.png', 5, 0, 0, 0, 32, 32),

            keys.frozen_staff: get_tiles_from_sheet('items/weapons/staff/frozen_staff.png', 0, 0, 0, 0, 32, 32),
            keys.frozen_staff_attack_cut: get_tiles_from_sheet('items/weapons/staff/frozen_staff_attack.png', 5, 0, 0, 0, 32, 32),

            keys.poison_staff: get_tiles_from_sheet('items/weapons/staff/poison_staff.png', 0, 0, 0, 0, 32, 32),
            keys.poison_staff_attack_cut: get_tiles_from_sheet('items/weapons/staff/poison_staff_attack.png', 5, 0, 0, 0, 32, 32),

            keys.vampiric_staff: get_tiles_from_sheet('items/weapons/staff/vampiric_staff.png', 0, 0, 0, 0, 32, 32),
            keys.vampiric_staff_attack_cut: get_tiles_from_sheet('items/weapons/staff/vampiric_staff_attack.png', 5, 0, 0, 0, 32, 32),

            keys.electric_staff: get_tiles_from_sheet('items/weapons/staff/electric_staff.png', 0, 0, 0, 0, 32, 32),
            keys.electric_staff_attack_cut: get_tiles_from_sheet('items/weapons/staff/electric_staff_attack.png', 5, 0, 0, 0, 32, 32),

        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_List(self):
        Weapons_assets = {
            keys.sword: get_tiles_from_sheet('items/weapons/sword/sword.png', 0, 0, 0, 0, 32, 32),
            keys.sword_idle: get_tiles_from_sheet('items/weapons/sword/sword_idle.png', 3, 0, 0, 0, 32, 32),
            keys.sword_running_up: get_tiles_from_sheet('items/weapons/sword/sword_running_behind.png', 5, 0, 0, 0, 32, 32),
            keys.sword_running_down: get_tiles_from_sheet('items/weapons/sword/sword_running_front.png', 5, 0, 0, 0, 32, 32),
            keys.sword_cut: get_tiles_from_sheet('items/weapons/sword/sword_attack_cut.png', 4, 0, 0, 0, 48, 48),
            keys.sword_stab: get_tiles_from_sheet('items/weapons/sword/sword_attack_stab.png', 4, 0, 0, 0, 48, 48),
            
            keys.torch: get_tiles_from_sheet('items/weapons/torch/torch.png', 7, 0, 0, 0, 32, 32),
            keys.torch_idle: get_tiles_from_sheet('items/weapons/torch/torch_idle.png', 3, 0, 0, 0, 32, 32),
            keys.torch_running_down: get_tiles_from_sheet('items/weapons/torch/torch_running_down.png', 5, 0, 0, 0, 32, 32),
            keys.torch_running_up: get_tiles_from_sheet('items/weapons/torch/torch_running_up.png', 5, 0, 0, 0, 32, 32),
            keys.torch_cut: get_tiles_from_sheet('items/weapons/torch/torch_attack.png', 4, 0, 0, 0, 48, 48),

            keys.halberd: get_tiles_from_sheet('items/weapons/halberd/halberd.png', 0, 0, 0, 0, 32, 32),
            keys.halberd_idle: get_tiles_from_sheet('items/weapons/halberd/halberd_idle.png',4, 0, 0, 0, 32, 32),
            keys.halberd_running_up: get_tiles_from_sheet('items/weapons/halberd/halberd_running_behind.png', 5, 0, 0, 0, 32, 32),
            keys.halberd_running_down: get_tiles_from_sheet('items/weapons/halberd/halberd_running_down.png', 5, 0, 0, 0, 32, 32),
            keys.halberd_cut: get_tiles_from_sheet('items/weapons/halberd/halberd_cut_attack.png', 4, 0, 0, 0, 48, 48),
            
            keys.spear: get_tiles_from_sheet('items/weapons/spear/spear.png', 0, 0, 0, 0, 32, 32),
            keys.spear_idle: get_tiles_from_sheet('items/weapons/spear/spear_idle.png', 3, 0, 0, 0, 32, 32),
            keys.spear_running_up: get_tiles_from_sheet('items/weapons/spear/spear_running_behind.png', 5, 0, 0, 0, 32, 32),
            keys.spear_running_down: get_tiles_from_sheet('items/weapons/spear/spear_running_down.png', 5, 0, 0, 0, 32, 32),
            keys.spear_stab: get_tiles_from_sheet('items/weapons/spear/spear_stab.png', 4, 0, 0, 0, 48, 48),
            
            keys.bow: get_tiles_from_sheet('items/weapons/bow/bow.png', 0, 0, 0, 0, 32, 32),
            keys.bow_attack: get_tiles_from_sheet('items/weapons/bow/bow_attack.png', 2, 0, 0, 0, 32, 32),
            
            keys.arrow: get_tiles_from_sheet('items/weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),
            keys.arrow_attack: get_tiles_from_sheet('items/weapons/arrow/arrow.png', 0, 0, 0, 0, 32, 32),

            keys.sceptre: get_tiles_from_sheet('items/weapons/sceptre/sceptre.png', 7, 0, 0, 0, 32, 32),
            keys.sceptre_attack_cut: get_tiles_from_sheet('items/weapons/sceptre/sceptre_cut_attack.png', 9, 0, 0, 0, 32, 32),

            keys.hatchet: get_tiles_from_sheet('items/weapons/hatchet/hatchet.png', 7, 0, 0, 0, 32, 32),
            keys.hatchet_attack_cut: get_tiles_from_sheet('items/weapons/hatchet/hatchet_cut_attack.png', 8, 0, 0, 0, 32, 32),

            keys.crossbow: get_tiles_from_sheet('items/weapons/crossbow/crossbow.png', 8, 0, 0, 0, 32, 32),
            keys.crossbow_attack: get_tiles_from_sheet('items/weapons/crossbow/crossbow_attack.png', 2, 0, 0, 0, 32, 32),

            keys.scythe: get_tiles_from_sheet('items/weapons/scythe/scythe.png', 7, 0, 0, 0, 32, 32),
            keys.scythe_attack_cut: get_tiles_from_sheet('items/weapons/scythe/scythe_attack.png', 9, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)

    def Asset_Weapons_Effects(self):
        Weapons_assets = {
            keys.slash_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.slash_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.slash_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.slash_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.slash_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.slash_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/slash_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.blunt_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.blunt_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.blunt_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.blunt_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.blunt_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.blunt_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/blunt_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.electric_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.electric_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.electric_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.electric_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.electric_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.electric_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/electric_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.fire_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_cut_attack.png', 4, 0, 0, 0, 48, 48),
            keys.fire_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.fire_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.fire_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.fire_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.fire_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/fire_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.frozen_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.frozen_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.frozen_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.frozen_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.frozen_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.frozen_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/frozen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.poison_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.poison_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.poison_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.poison_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.poison_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.poison_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/poison_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.regen_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.regen_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.regen_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.regen_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.regen_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.regen_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/regen_charge_attack.png', 5, 0, 0, 0, 32, 32),

            keys.vampiric_cut_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_cut_attack.png', 6, 0, 0, 0, 48, 48),
            keys.vampiric_stab_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_stab_attack.png', 6, 0, 0, 0, 48, 48),
            keys.vampiric_two_hand_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_two_hand_attack.png', 6, 0, 0, 0, 48, 48),
            keys.vampiric_spin_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_spin_attack.png', 7, 0, 0, 0, 48, 48),
            keys.vampiric_smash_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_smash_attack.png', 5, 0, 0, 0, 48, 48),
            keys.vampiric_charge_effect: get_tiles_from_sheet('items/weapons/weapon_effects/vampiric_charge_attack.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Weapons_assets)


    def Asset_Inventory(self):
        Weapon_Inventory_assets = {
            keys.sword_shield: get_tiles_from_sheet('inventory/sword_shield.png', 2, 0, 0, 0, 34, 34),
            keys.duel_wield: get_tiles_from_sheet('inventory/Duel_wield.png', 2, 0, 0, 0, 34, 34),
            keys.bow_arrow: get_tiles_from_sheet('inventory/Bow_Arrow.png', 2, 0, 0, 0, 34, 34),
            keys.left_right: get_tiles_from_sheet('inventory/left_right.png', 2, 0, 0, 0, 34, 34),
            keys.rune_background: get_tiles_from_sheet('inventory/rune_background.png', 1, 0, 0, 0, 34, 34),
        }
        self.assets.update(Weapon_Inventory_assets)

    def Asset_Interative_Objects_List(self):
        Objects_assets = {
            keys.chest: get_tiles_from_sheet('decoration/loot_containers/chest.png', 8, 0, 0, 0, 32, 32),
            keys.vase: get_tiles_from_sheet('decoration/loot_containers/vase/vase.png', 4, 0, 0, 0, 32, 32),
            keys.bookshelf: get_tiles_from_sheet('decoration/loot_containers/bookshelf.png', 3, 0, 0, 0, 32, 32),
            keys.soul_well: get_tiles_from_sheet('decoration/Shrine/soul_well.png', 3, 0, 0, 0, 64, 64),
            keys.potion_table: get_tiles_from_sheet('decoration/tables/potion_table.png', 0, 0, 0, 0, 64, 64),
            keys.door_basic: get_tiles_from_sheet('decoration/door/door_closed.png', 0, 0, 0, 0, 32, 32),
            keys.fragile_wall: get_tiles_from_sheet('decoration/door/fragile_wall.png', 0, 0, 0, 0, 32, 32),
            keys.rune_shrine: get_tiles_from_sheet('decoration/shrine/rune_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.portal_shrine: get_tiles_from_sheet('decoration/shrine/portal_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.hunter_shrine: get_tiles_from_sheet('decoration/shrine/hunter_shrine.png', 2, 0, 0, 0, 64, 64),
            keys.blood_shrine: get_tiles_from_sheet('decoration/shrine/blood_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.sacrifice_shrine: get_tiles_from_sheet('decoration/shrine/sacrifice_shrine.png', 3, 0, 0, 0, 64, 64),
            keys.teleportation_circle: get_tiles_from_sheet('decoration/interactive/teleportation_circle.png', 0, 0, 0, 0, 32, 32),
            keys.campfire: get_tiles_from_sheet('decoration/interactive/campfire.png', 4, 0, 0, 0, 32, 32),
            keys.lever: get_tiles_from_sheet('decoration/interactive/lever.png', 1, 0, 0, 0, 32, 32),
            keys.bones: get_tiles_from_sheet('decoration/environment/bones.png', 0, 0, 0, 0, 32, 32),
            keys.weapon_rack: get_tiles_from_sheet('decoration/loot_containers/weapon_rack.png', 0, 0, 0, 0, 32, 32),
            keys.plinth: get_tiles_from_sheet('decoration/loot_containers/plinth.png', 0, 0, 0, 0, 32, 32),
            keys.effigy_tomb: get_tiles_from_sheet('decoration/loot_containers/effigy_tomb.png', 1, 0, 0, 0, 32, 64),
            keys.brazier + '_1': get_tiles_from_sheet('decoration/light_sources/brazier_1.png', 5, 0, 0, 0, 32, 32),
            keys.brazier + '_2': get_tiles_from_sheet('decoration/light_sources/brazier_2.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Objects_assets)

    def Crystal_Cavern_Decorations(self):
        Objects_assets = {
            keys.amplifying_node + '_1': get_tiles_from_sheet('decoration\crystal_caverns/amplifying_node.png', 5, 0, 0, 0, 32, 32),
            keys.harmonic_crystal + '_2': get_tiles_from_sheet('decoration\crystal_caverns/harmonic_crystal.png', 5, 0, 0, 0, 32, 32),
        }
        self.assets.update(Objects_assets)

    def Glowing_Crystals_List(self):
        Objects_assets = {
                    keys.glowing_crystal + '_1': get_tiles_from_sheet('decoration/light_sources/glowing_crystal_1.png', 5, 0, 0, 0, 32, 32),
                    keys.glowing_crystal + '_2': get_tiles_from_sheet('decoration/light_sources/glowing_crystal_2.png', 5, 0, 0, 0, 32, 32),
                    keys.glowing_crystal + '_3': get_tiles_from_sheet('decoration/light_sources/glowing_crystal_3.png', 5, 0, 0, 0, 32, 32),
                    keys.glowing_crystal + '_4': get_tiles_from_sheet('decoration/light_sources/glowing_crystal_4.png', 5, 0, 0, 0, 32, 32),
                    keys.glowing_crystal + '_5': get_tiles_from_sheet('decoration/light_sources/glowing_crystal_5.png', 5, 0, 0, 0, 32, 32),
                }
        self.assets.update(Objects_assets)




    def Asset_Environment_List(self):
        Environment_assets = {
            keys.lava_env: get_tiles_from_sheet('environment/lava.png', 2, 0, 0, 0, 32, 32),
            keys.shallow_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 0, 32, 32),
            keys.medium_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            keys.deep_water_env: get_tiles_from_sheet('environment/water.png', 2, 0, 32, 32, 32, 32),
            keys.shallow_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 0, 32, 32),
            keys.medium_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
            keys.deep_ice_env: get_tiles_from_sheet('environment/water.png', 1, 0, 112, 32, 32, 32),
        }
        self.assets.update(Environment_assets)


    def Asset_Decoration_List(self):
        decoration_assets = {
        }
        self.assets.update(decoration_assets)


    def Asset_Potion_List(self):
        potion_assets = {
            keys.empty_bottle: get_tiles_from_sheet('items/potions/Healing_potions/empty.png', 0, 0, 0, 0, 32, 32),

            keys.invisibility + '_' + keys.full: get_tiles_from_sheet('items/potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            keys.invisibility + '_' + keys.half: get_tiles_from_sheet('items/potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),
            keys.invisibility + '_' + keys.low: get_tiles_from_sheet('items/potions/invisibility/invisibility.png', 2, 2, 0, 0, 32, 32),

            keys.healing + '_' + keys.full: get_tiles_from_sheet('items/potions/Healing_potions/healing_full.png', 2, 2, 0, 0, 32, 32),
            keys.healing + '_' + keys.half: get_tiles_from_sheet('items/potions/Healing_potions/healing_half.png', 2, 2, 0, 0, 32, 32),
            keys.healing + '_' + keys.low: get_tiles_from_sheet('items/potions/Healing_potions/healing_low.png', 2, 2, 0, 0, 32, 32),

            keys.increase_souls + '_' + keys.full: get_tiles_from_sheet('items/potions/soul_potions/soul_full.png', 2, 2, 0, 0, 32, 32),
            keys.increase_souls + '_' + keys.half: get_tiles_from_sheet('items/potions/soul_potions/soul_half.png', 2, 2, 0, 0, 32, 32),
            keys.increase_souls + '_' + keys.low: get_tiles_from_sheet('items/potions/soul_potions/soul_low.png', 2, 2, 0, 0, 32, 32),

            keys.arcane_hunger + '_' + keys.full: get_tiles_from_sheet('items/potions/soul_potions/arcane_hunger_full.png', 2, 2, 0, 0, 32, 32),
            keys.arcane_hunger + '_' + keys.half: get_tiles_from_sheet('items/potions/soul_potions/arcane_hunger_half.png', 2, 2, 0, 0, 32, 32),
            keys.arcane_hunger + '_' + keys.low: get_tiles_from_sheet('items/potions/soul_potions/arcane_hunger_low.png', 2, 2, 0, 0, 32, 32),

            keys.speed + '_' + keys.full: get_tiles_from_sheet('items/potions/speed_potions/speed_full.png', 2, 2, 0, 0, 32, 32),
            keys.speed + '_' + keys.half: get_tiles_from_sheet('items/potions/speed_potions/speed_half.png', 2, 2, 0, 0, 32, 32),
            keys.speed + '_' + keys.low: get_tiles_from_sheet('items/potions/speed_potions/speed_low.png', 2, 2, 0, 0, 32, 32),

            keys.luck + '_' + keys.full: get_tiles_from_sheet('items/potions/luck_potions/luck_full.png', 2, 2, 0, 0, 32, 32),
            keys.luck + '_' + keys.half: get_tiles_from_sheet('items/potions/luck_potions/luck_half.png', 2, 2, 0, 0, 32, 32),
            keys.luck + '_' + keys.low: get_tiles_from_sheet('items/potions/luck_potions/luck_low.png', 2, 2, 0, 0, 32, 32),

            keys.increase_strength + '_' + keys.full: get_tiles_from_sheet('items/potions/strength_potions/strength_full.png', 2, 2, 0, 0, 32, 32),
            keys.increase_strength + '_' + keys.half: get_tiles_from_sheet('items/potions/strength_potions/strength_half.png', 2, 2, 0, 0, 32, 32),
            keys.increase_strength + '_' + keys.low: get_tiles_from_sheet('items/potions/strength_potions/strength_low.png', 2, 2, 0, 0, 32, 32),

            keys.poison_resistance + '_' + keys.full: get_tiles_from_sheet('items/potions/poison_resistance_potions/poison_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.poison_resistance + '_' + keys.half: get_tiles_from_sheet('items/potions/poison_resistance_potions/poison_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.poison_resistance + '_' + keys.low: get_tiles_from_sheet('items/potions/poison_resistance_potions/poison_resistance_low.png', 2, 2, 0, 0, 32, 32),

            keys.purple + '_' + keys.full: get_tiles_from_sheet('items/potions/Purplepotions/Purple_full.png', 2, 2, 0, 0, 32, 32),
            keys.purple + '_' + keys.half: get_tiles_from_sheet('items/potions/Purplepotions/Purple_half.png', 2, 2, 0, 0, 32, 32),
            keys.purple + '_' + keys.low: get_tiles_from_sheet('items/potions/Purplepotions/Purple_low.png', 2, 2, 0, 0, 32, 32),

            keys.frozen_resistance + '_' + keys.full: get_tiles_from_sheet('items/potions/freeze_resistance_potions/freeze_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.frozen_resistance + '_' + keys.half: get_tiles_from_sheet('items/potions/freeze_resistance_potions/freeze_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.frozen_resistance + '_' + keys.low: get_tiles_from_sheet('items/potions/freeze_resistance_potions/freeze_resistance_low.png', 2, 2, 0, 0, 32, 32),

            keys.silence + '_' + keys.full: get_tiles_from_sheet('items/potions/silence_potions/silence_full.png', 2, 2, 0, 0, 32, 32),
            keys.silence + '_' + keys.half: get_tiles_from_sheet('items/potions/silence_potions/silence_half.png', 2, 2, 0, 0, 32, 32),
            keys.silence + '_' + keys.low: get_tiles_from_sheet('items/potions/silence_potions/silence_low.png', 2, 2, 0, 0, 32, 32),

            keys.regen + '_' + keys.full: get_tiles_from_sheet('items/potions/regen_potions/regen_full.png', 2, 2, 0, 0, 32, 32),
            keys.regen + '_' + keys.half: get_tiles_from_sheet('items/potions/regen_potions/regen_half.png', 2, 2, 0, 0, 32, 32),
            keys.regen + '_' + keys.low: get_tiles_from_sheet('items/potions/regen_potions/regen_low.png', 2, 2, 0, 0, 32, 32),

            keys.vampiric + '_' + keys.full: get_tiles_from_sheet('items/potions/vampiric_potions/vampiric_full.png', 2, 2, 0, 0, 32, 32),
            keys.vampiric + '_' + keys.half: get_tiles_from_sheet('items/potions/vampiric_potions/vampiric_half.png', 2, 2, 0, 0, 32, 32),
            keys.vampiric + '_' + keys.low: get_tiles_from_sheet('items/potions/vampiric_potions/vampiric_low.png', 2, 2, 0, 0, 32, 32),

            keys.fire_resistance + '_' + keys.full: get_tiles_from_sheet('items/potions/fire_resistance_potions/fire_resistance_full.png', 2, 2, 0, 0, 32, 32),
            keys.fire_resistance + '_' + keys.half: get_tiles_from_sheet('items/potions/fire_resistance_potions/fire_resistance_half.png', 2, 2, 0, 0, 32, 32),
            keys.fire_resistance + '_' + keys.low: get_tiles_from_sheet('items/potions/fire_resistance_potions/fire_resistance_low.png', 2, 2, 0, 0, 32, 32),
        }

        self.assets.update(potion_assets)

    def Asset_Loot(self):
        loot = {
            keys.gold: get_tiles_from_sheet('items/valuables/gold_coins.png', 3, 0, 0, 0, 16, 16),
            keys.hunter_treasure: get_tiles_from_sheet('items/valuables/hunter_treasure.png', 0, 0, 0, 0, 32, 32),
            keys.soul_shard: get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
            keys.echo_bell: get_tiles_from_sheet('items/utility/echo_bell.png', 0, 0, 0, 0, 32, 32),
            keys.shadow_cloak: get_tiles_from_sheet('items/utility/shadow_cloak.png', 0, 0, 0, 0, 32, 32),
            keys.lantern: get_tiles_from_sheet('items/passive/lantern.png', 0, 0, 0, 0, 32, 32),
            keys.anchor_stone: get_tiles_from_sheet('items/passive/anchor_stone.png', 0, 0, 0, 0, 32, 32),
            keys.blood_tomb: get_tiles_from_sheet('items/cursed/blood_tomb.png', 0, 0, 0, 0, 32, 32),
            keys.faith_pendant: get_tiles_from_sheet('items/passive/faith_pendant.png', 0, 0, 0, 0, 32, 32),
            keys.lucky_charm: get_tiles_from_sheet('items/passive/lucky_charm.png', 0, 0, 0, 0, 32, 32),
            keys.magnet: get_tiles_from_sheet('items/passive/magnet.png', 0, 0, 0, 0, 32, 32),
            keys.power_totem: get_tiles_from_sheet('items/passive/power_totem.png', 0, 0, 0, 0, 32, 32),
            keys.strength_totem: get_tiles_from_sheet('items/passive/strength_totem.png', 0, 0, 0, 0, 32, 32),
            keys.halo: get_tiles_from_sheet('items/passive/halo.png', 0, 0, 0, 0, 32, 32),
            keys.muffled_boots: get_tiles_from_sheet('items/passive/muffled_boots.png', 0, 0, 0, 0, 32, 32),
            keys.demonic_bargain: get_tiles_from_sheet('items/cursed/demonic_bargain.png', 0, 0, 0, 0, 32, 32),
            keys.temptress_embrace: get_tiles_from_sheet('items/cursed/temptress_embrace.png', 0, 0, 0, 0, 32, 32),
            keys.forsaken_grimoire: get_tiles_from_sheet('items/cursed/forsaken_grimoire.png', 0, 0, 0, 0, 32, 32),
            keys.black_coin: get_tiles_from_sheet('items/cursed/black_coin.png', 0, 0, 0, 0, 32, 32),
            keys.blood_ring: get_tiles_from_sheet('items/cursed/blood_ring.png', 0, 0, 0, 0, 32, 32),
            keys.blood_pact: get_tiles_from_sheet('items/revive/blood_pact.png', 0, 0, 0, 0, 32, 32),
            keys.phoenix_feather: get_tiles_from_sheet('items/revive/phoenix_feather.png', 0, 0, 0, 0, 32, 32),
            keys.light_pendant: get_tiles_from_sheet('items/revive/light_pendant.png', 0, 0, 0, 0, 32, 32),
            keys.gravediggers_coin: get_tiles_from_sheet('items/revive/gravediggers_coin.png', 0, 0, 0, 0, 32, 32),
            keys.faded_hourglass: get_tiles_from_sheet('items/utility/faded_hourglass.png', 4, 0, 0, 0, 32, 32),
            keys.ethereal_chains: get_tiles_from_sheet('items/utility/ethereal_chains.png', 0, 0, 0, 0, 32, 32),
            keys.recall_scroll: get_tiles_from_sheet('items/utility/recall_parchment.png', 0, 0, 0, 0, 32, 32),
            keys.recipe_scroll: get_tiles_from_sheet('items/passive/recipe_scroll.png', 0, 0, 0, 0, 32, 32),
            keys.echo_sigil: get_tiles_from_sheet('items/passive/echo_sigil.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Gems(self):
        loot = {
            keys.arcane_hunger_gem: get_tiles_from_sheet('items/gems/arcane_hunger.png', 0, 0, 0, 0, 32, 32),
            keys.blunt_gem: get_tiles_from_sheet('items/gems/blunt.png', 0, 0, 0, 0, 32, 32),
            keys.durability_gem: get_tiles_from_sheet('items/gems/durability.png', 0, 0, 0, 0, 32, 32),
            keys.electric_gem: get_tiles_from_sheet('items/gems/electric.png', 0, 0, 0, 0, 32, 32),
            keys.fire_gem: get_tiles_from_sheet('items/gems/fire.png', 0, 0, 0, 0, 32, 32),
            keys.frozen_gem: get_tiles_from_sheet('items/gems/freeze.png', 0, 0, 0, 0, 32, 32),
            keys.halo_gem: get_tiles_from_sheet('items/gems/halo.png', 0, 0, 0, 0, 32, 32),
            keys.multishot_gem: get_tiles_from_sheet('items/gems/multishot.png', 0, 0, 0, 0, 32, 32),
            keys.poison_gem: get_tiles_from_sheet('items/gems/poison.png', 0, 0, 0, 0, 32, 32),
            keys.power_gem: get_tiles_from_sheet('items/gems/power.png', 0, 0, 0, 0, 32, 32),
            keys.range_gem: get_tiles_from_sheet('items/gems/range.png', 0, 0, 0, 0, 32, 32),
            keys.toughness_gem: get_tiles_from_sheet('items/gems/toughness.png', 0, 0, 0, 0, 32, 32),
            keys.slash_gem: get_tiles_from_sheet('items/gems/sharpness.png', 0, 0, 0, 0, 32, 32),
            keys.speed_gem: get_tiles_from_sheet('items/gems/speed.png', 0, 0, 0, 0, 32, 32),
            keys.strength_gem: get_tiles_from_sheet('items/gems/strength.png', 0, 0, 0, 0, 32, 32),
            keys.terror_gem: get_tiles_from_sheet('items/gems/terror.png', 0, 0, 0, 0, 32, 32),
            keys.vampiric_gem: get_tiles_from_sheet('items/gems/vampiric.png', 0, 0, 0, 0, 32, 32),
            keys.vulnerable_gem: get_tiles_from_sheet('items/gems/vulnerable.png', 0, 0, 0, 0, 32, 32),
            keys.weakness_gem: get_tiles_from_sheet('items/gems/weakness.png', 0, 0, 0, 0, 32, 32),
            keys.wet_gem: get_tiles_from_sheet('items/gems/wet.png', 0, 0, 0, 0, 32, 32),
            keys.lockpick_gem: get_tiles_from_sheet('items/gems/blunt.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Ingots(self):
        loot = {
            keys.Steel_ingot: get_tiles_from_sheet('items/ingots/Steel_ingot.png', 0, 0, 0, 0, 32, 32),
            keys.jade_ingot: get_tiles_from_sheet('items/ingots/jade_ingot.png', 0, 0, 0, 0, 32, 32),
            keys.copper_ingot: get_tiles_from_sheet('items/ingots/copper_ingot.png', 0, 0, 0, 0, 32, 32),
            keys.Gold_ingot: get_tiles_from_sheet('items/ingots/Gold_ingot.png', 0, 0, 0, 0, 32, 32),
            keys.Silver_ingot: get_tiles_from_sheet('items/ingots/Silver_ingot.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Keys(self):
        loot = {
            keys.lockpick: get_tiles_from_sheet('items/keys/lockpick.png', 0, 0, 0, 0, 32, 32),
            keys.blood_key: get_tiles_from_sheet('items/keys/blood_key.png', 0, 0, 0, 0, 32, 32),
            keys.skeleton_key: get_tiles_from_sheet('items/keys/skeleton_key.png', 0, 0, 0, 0, 32, 32),
            keys.soul_key: get_tiles_from_sheet('items/keys/soul_key.png', 0, 0, 0, 0, 32, 32),
            keys.cursed_key: get_tiles_from_sheet('items/keys/cursed_key.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Bombs(self):
        loot = {
            keys.fire_bomb: get_tiles_from_sheet('items/bombs/fire_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.frozen_bomb: get_tiles_from_sheet('items/bombs/frozen_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.electric_bomb: get_tiles_from_sheet('items/bombs/electric_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.poison_bomb: get_tiles_from_sheet('items/bombs/poison_bomb.png', 0, 0, 0, 0, 32, 32),
            keys.vampiric_bomb: get_tiles_from_sheet('items/bombs/vampiric_bomb.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(loot)

    def Asset_Rune(self):
        rune = {
            keys.healing_rune: get_tiles_from_sheet('items/runes/healing_rune.png', 1, 0, 0, 0, 32, 32),
            keys.regen_rune: get_tiles_from_sheet('items/runes/regen_rune.png', 1, 0, 0, 0, 32, 32),
            keys.dash_rune: get_tiles_from_sheet('items/runes/dash_rune.png', 1, 0, 0, 0, 32, 32),
            keys.arcane_conduit_rune: get_tiles_from_sheet('items/runes/arcane_conduit_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.fire_cirlce_rune: get_tiles_from_sheet('items/runes/fire/fire_cirlce_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_resistance_rune: get_tiles_from_sheet('items/runes/fire/fire_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_shield_rune: get_tiles_from_sheet('items/runes/fire/fire_shield_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_spray_rune: get_tiles_from_sheet('items/runes/fire/fire_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.fire_ball_rune: get_tiles_from_sheet('items/runes/fire/fire_ball_rune.png', 1, 0, 0, 0, 32, 32),

            keys.freeze_circle_rune: get_tiles_from_sheet('items/runes/frost/frost_circle_rune.png', 1, 0, 0, 0, 32, 32),
            keys.frozen_resistance_rune: get_tiles_from_sheet('items/runes/frost/frost_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_storm_rune: get_tiles_from_sheet('items/runes/frost/frost_storm_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_spray_rune: get_tiles_from_sheet('items/runes/frost/frost_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.freeze_ball_rune: get_tiles_from_sheet('items/runes/frost/frost_ball_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.poison_resistance_rune: get_tiles_from_sheet('items/runes/poison/poison_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_ball_rune: get_tiles_from_sheet('items/runes/poison/poison_ball_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_cloud_rune: get_tiles_from_sheet('items/runes/poison/poison_cloud_rune.png', 1, 0, 0, 0, 32, 32),
            keys.poison_plume_rune: get_tiles_from_sheet('items/runes/poison/poison_plume_rune.png', 1, 0, 0, 0, 32, 32),

            keys.electric_resistance_rune: get_tiles_from_sheet('items/runes/electric/electric_resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.electric_ball_rune: get_tiles_from_sheet('items/runes/electric/electric_ball_rune.png', 1, 0, 0, 0, 32, 32),
            keys.electric_spray_rune: get_tiles_from_sheet('items/runes/electric/electric_spray_rune.png', 1, 0, 0, 0, 32, 32),
            keys.chain_lightning_rune: get_tiles_from_sheet('items/runes/electric/chain_lightning_rune.png', 1, 0, 0, 0, 32, 32),
            
            keys.soul_reap_rune: get_tiles_from_sheet('items/runes/vampiric/soul_reap_rune.png', 1, 0, 0, 0, 32, 32),
            keys.soul_pit_rune: get_tiles_from_sheet('items/runes/vampiric/soul_pit_rune.png', 1, 0, 0, 0, 32, 32),

            keys.invisibility_rune: get_tiles_from_sheet('items/runes/invisibility_rune.png', 1, 0, 0, 0, 32, 32),
            keys.key_rune: get_tiles_from_sheet('items/runes/key_rune.png', 1, 0, 0, 0, 32, 32),
            keys.light_rune: get_tiles_from_sheet('items/runes/light_rune.png', 1, 0, 0, 0, 32, 32),
            keys.resistance_rune: get_tiles_from_sheet('items/runes/resistance_rune.png', 1, 0, 0, 0, 32, 32),
            keys.shield_rune: get_tiles_from_sheet('items/runes/shield_rune.png', 1, 0, 0, 0, 32, 32),
            keys.silence_rune: get_tiles_from_sheet('items/runes/silence_rune.png', 1, 0, 0, 0, 32, 32),
            keys.speed_rune: get_tiles_from_sheet('items/runes/speed_rune.png', 1, 0, 0, 0, 32, 32),
            keys.increase_strength_rune: get_tiles_from_sheet('items/runes/strength_rune.png', 1, 0, 0, 0, 32, 32),
            keys.vampiric_rune: get_tiles_from_sheet('items/runes/vampiric_rune.png', 1, 0, 0, 0, 32, 32),
            keys.arcane_hunger_rune: get_tiles_from_sheet('items/runes/hunger_rune.png', 1, 0, 0, 0, 32, 32),
            keys.magnet_rune: get_tiles_from_sheet('items/runes/magnet_rune.png', 1, 0, 0, 0, 32, 32),
            keys.invulnerable_rune: get_tiles_from_sheet('items/runes/invulnerable_rune.png', 1, 0, 0, 0, 32, 32),
        }
        self.assets.update(rune)


    def Asset_Font(self):
        font = {
            keys.player_damage_font: get_tiles_from_sheet('font/player_damage_font.png', 7, 5, 0, 0, 16, 16),
            keys.font: get_tiles_from_sheet('font/font_default/font.png', 7, 5, 0, 0, 16, 16),
            keys.font_slash: get_tiles_from_sheet('font/font_default/font.png', 7, 5, 0, 0, 16, 16),
            keys.textbox_headline: get_tiles_from_sheet('font/font_headline/textbox_headline.png', 7, 5, 0, 0, 12, 12),
            keys.font_commmon: get_tiles_from_sheet('font/font_headline/textbox_headline.png', 7, 5, 0, 0, 12, 12),
            keys.font_uncommon: get_tiles_from_sheet('font/font_headline/font_uncommon.png', 7, 5, 0, 0, 12, 12),
            keys.font_rare: get_tiles_from_sheet('font/font_headline/font_rare.png', 7, 5, 0, 0, 12, 12),
            keys.font_epic: get_tiles_from_sheet('font/font_headline/font_epic.png', 7, 5, 0, 0, 12, 12),
            keys.font_legendary: get_tiles_from_sheet('font/font_headline/font_legendary.png', 7, 5, 0, 0, 12, 12),
            keys.font_blunt: get_tiles_from_sheet('font/font_default/font_blunt.png', 7, 5, 0, 0, 16, 16),
            keys.font_electric: get_tiles_from_sheet('font/font_default/font_electric.png', 7, 5, 0, 0, 16, 16),
            keys.font_fire: get_tiles_from_sheet('font/font_default/font_fire.png', 7, 5, 0, 0, 16, 16),
            keys.font_frozen: get_tiles_from_sheet('font/font_default/font_frozen.png', 7, 5, 0, 0, 16, 16),
            keys.font_poison: get_tiles_from_sheet('font/font_default/font_poison.png', 7, 5, 0, 0, 16, 16),
            keys.font_vampiric: get_tiles_from_sheet('font/font_default/font_vampiric.png', 7, 5, 0, 0, 16, 16),
            keys.font_wet: get_tiles_from_sheet('font/font_default/font_wet.png', 7, 5, 0, 0, 16, 16),
            keys.font_small: get_tiles_from_sheet('font/font_small/font_small.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_slash: get_tiles_from_sheet('font/font_small/font_small.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_fire: get_tiles_from_sheet('font/font_small/font_small_fire.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_frozen: get_tiles_from_sheet('font/font_small/font_small_frozen.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_poison: get_tiles_from_sheet('font/font_small/font_small_poison.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_blunt: get_tiles_from_sheet('font/font_small/font_small_blunt.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_electric: get_tiles_from_sheet('font/font_small/font_small_electric.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_vampiric: get_tiles_from_sheet('font/font_small/font_small_vampiric.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_wet: get_tiles_from_sheet('font/font_small/font_small_wet.png', 7, 5, 0, 0, 8, 8),
            keys.font_small_blunt: get_tiles_from_sheet('font/font_small/font_small_blunt.png', 7, 5, 0, 0, 8, 8),
            keys.floating_E: get_tiles_from_sheet('font/floating_e.png', 1, 0, 0, 0, 16, 16),
            keys.symbols: get_tiles_from_sheet('font/symbols.png', 7, 6, 0, 0, 16, 16),
            keys.souls: get_tiles_from_sheet('font/souls.png', 3, 0, 0, 0, 32, 32),
            keys.noise: get_tiles_from_sheet('font/noise.png', 2, 0, 0, 0, 16, 16),
        }
        self.assets.update(font)
    
    def Asset_UI(self):
        health_bars = {
            keys.healthbar_1: get_tiles_from_sheet('ui/healthbar/healthbar_1.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_2: get_tiles_from_sheet('ui/healthbar/healthbar_2.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_3: get_tiles_from_sheet('ui/healthbar/healthbar_3.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_4: get_tiles_from_sheet('ui/healthbar/healthbar_4.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_5: get_tiles_from_sheet('ui/healthbar/healthbar_5.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_6: get_tiles_from_sheet('ui/healthbar/healthbar_6.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_7: get_tiles_from_sheet('ui/healthbar/healthbar_7.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_8: get_tiles_from_sheet('ui/healthbar/healthbar_8.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_9: get_tiles_from_sheet('ui/healthbar/healthbar_9.png', 5, 0, 0, 0, 64, 64),
            keys.healthbar_10: get_tiles_from_sheet('ui/healthbar/healthbar_10.png', 5, 0, 0, 0, 64, 64),

            keys.awakening_skull_1: get_tiles_from_sheet('ui/skull/skull_1.png', 0, 0, 0, 0, 32, 32),
            keys.awakening_skull_2: get_tiles_from_sheet('ui/skull/skull_2.png', 0, 0, 0, 0, 32, 32),
            keys.awakening_skull_3: get_tiles_from_sheet('ui/skull/skull_3.png', 0, 0, 0, 0, 32, 32),
            keys.awakening_skull_4: get_tiles_from_sheet('ui/skull/skull_4.png', 0, 0, 0, 0, 32, 32),
            keys.awakening_skull_5: get_tiles_from_sheet('ui/skull/skull_5.png', 0, 0, 0, 0, 32, 32),

            keys.durability_bar: get_tiles_from_sheet('ui/durability_bar/durability_bar.png', 9, 0, 0, 0, 16, 8),
        }
        self.assets.update(health_bars)


    def Asset_Menu(self):
        menu = {
            keys.loading_bar: get_tiles_from_sheet('menu/loading_screen.png', 6, 0, 0, 0, 96, 96),
        }
        self.assets.update(menu)

    def Asset_Tooltips(self):
        tooltips = {
            keys.radius_tooltip: get_tiles_from_sheet('items/tooltips/radius.png', 0, 0, 0, 0, 32, 32),
        }
        self.assets.update(tooltips)

