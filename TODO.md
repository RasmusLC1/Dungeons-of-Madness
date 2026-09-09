# Gameplay Loop
    - Choose between 2 modes, descend or endless. Decent takes you through 7 layers of the dungeon to a final boss
    - Collect gold and artifcats in dungeon to buy items, upgrades, healing etc
    - Lower levels have better rewards
    - To get to lower levels you need to pay a soul cost on each floor
    - Each layer has different themes, with unique enemies, mechanics, decoration and traps
    - Each time you complete a floor the next one becomes more difficult
    - There are shrines in the dungeon where you can pay with souls of slain enemies to buy upgrades
    -  Shrines are found in boss rooms and around the dungeon, risk damage to upgrade
    - Different Shrines do different things and are tied to the dungeon theme
    - Game ends when you die, you can find resurrection items in the dungeon, but they are rare or high risk
    - Noice attracts enemies and generates Clatter
    - Clatter system that spawns enemies using a director similar to left4dead
    - Score based on dungeon depth reached, loot and souls collected
        

# Engine Features:
    # Tile systsem
    # Use A* for path finding
    # Inventory System
    # Weapon inventory system
    # Dropping item, triggers trap
    # Raytracer that limits players vision, so enemies can sneak up from behind
    # Light engine
    # Clatter System where enemies are attracted to noise
    # Dungeon generator
    # Chunk system to prevent slowdown with larger maps
    # Save Load System
    # Particle Engine
    # Sound engine
    # Threat metre, a skull that fills up or something. If player generates clatter it has a chance to increase. It will also have a chance to decrease if player is quiet for longer periods of time
    # Minimap, adjust rendering scale for minimap and only display tiles that has been in raycaster

# UI
    # Item Inventory in grid at bottom center of the screen, 9 inventory slots, each with hotkey
    # Rune Inventory to the right of the item inventory, limit of 3 runes in grid, each with hotkey
    # Weaopon Inventory to the left of the item inventory, limit of 2 weapons in grid. Can be switched between with scroll wheel
    # Awakening skull that changes animation and fades in as the awakening level increases
    # Bottom left, the health bar, using an hour glass dripping blood for visual interesting design
    Top right rune amount, currently just a soul symbol with number, needs unique design, probably tying it to the minimap frame
    # Top right minimap of the explored dungeon, grows as the player explores more, resets each time new dungeon layer is reached
    # Top left side and down, player status effects, can be curses etc. Each effect is an item that can be hovered over for information

# Loading page:
    # Menu screen that renders parts of a loading bar every time a step in dungeon generator generates a new chunk
    # Save it in a seperate class that accepts an increment from dungeon generator
    Display the description of the dungeon you're entering and give little tips and tricks to the player while loading
    Have unique art for each dungeon theme

# Shop
Buy and sell items to help complete levels
Upgrade weapons

# Awakening engine
    Generating clatter has a chance to increase the difficulty of the dungeon layer (Awakening)
    Use an aggro budget, similar to Left 4 dead, where each clatter gives the aggro engine resources
    The budget slowly goes up over time even if player does not generate clatter (Prevents boring game)
    Big budget increases for certain events, like discovering the portal or activating certain shrines

    Increasing difficulty can have the following effects
        - Spawn enemies
        - Add traps
        - Give player debuffs
        - Buff enemies
        - Replace doors with walls
        - Replace chests with mimics
        - Reduce light level of all light sources
        - Spawn elite enemies
        - Increase overall clatter level, which increases the consequence of the other effects
        
    Clatter always notifies nearby enemies

    Add skull that gradually fills up with clatter level, hover over for clatter level

    When clatter is generated and has a negative effect apply screen shake and particles on the screen to simulate dungeon shaking and a deep rumble sound

    5 clatter levels, each has different probabilities for events, the higher the clatter level the worse the consequences

    Higher clatter levels generate better loot spawns as well

# Progression mechanic
    Player profile starts with basic items like potions and 

# Weapons:
    # Weapons have health, forcing players to either repair them with ingots at weapon shrines or to get new weapons 
    # Weapons have a pool of damage stats, so for instance a sword might have a dictionary with fire, frozen, sharpness and the damage value of each effect
    # Weapons can be upgraded with gems
    # weapons have their animations tied to the player sprite
    # Implement better animations, bright arcs for where the damage area is
    # Torch, emits light and be be used to set enemies on fire, relatively low damage
    # Sword, best damage, little utility
    # Spear, can be thrown
    # Bow, can press button, different arrows that can do certain things
    # Axe, can break wood doors
    # Hatchet, small axe, faster than axe
    # Mace/Hammer, can break certain walls and enviorement, special ground pound to stun nearby enemies
    # Halberd, swing and stab attack, charge attack
    # Scythe, swing attack, soul reap magic attack
    # Crossbow, Same as bow, but takes longer to load, but can be preloaded
    # Bomb, one time use, splash damage, can break enviorement, knockback from blast
    # magic Staff, improved runes but poor melee damage, different staffs for different lores of magic, costs souls per cast. Special attack for each lores
    # Shield, can block damage, can be used to rocket jump with bomb
    

# Items
    Items are held in inventory, not worth a lot of money, but helps navigate dungeon
    Rare objects found in loot rooms
    
    
    ## Passive:
        # Lantern, Sets the player light to 7, passive light
        # Magnet, autopickup of items
        # Totem of Power, increases Rune power, stacks with more totems
        # Totem of Strength, increases strength
        # Anchor Stone – Prevents the player from being pushed by traps or enemies.
        # Muffled boots – Reduces the noise generated by movement.
        # Halo, 1/10 chance to cancel damage
        # Echo Sigil, increases the activations of items by 1
        # Recipe scroll, increase potion strength by + 1, works similar to echo sigil
        # Lucky Charm - Improves player luck

        Compass that points towards boss room
        Pendant of Faith, Highlights traps, Needs trap rework first
        Different types of Cursed Talisman, Gives scaling benefits for each curse, maybe 10% movement increase for 1 curse, 20 for 2 etc
        Shrine hunter items, increases an effect for each shrine visited, health, strength, speed etc.
        Greed echo that gives gold when clatter is generated (needs cooldown to prevent spam), tied to enemies attracted
        Soul echo, same as Greed echo 


    # Utility:
        # Pendant of light, Revive on death for souls 
        # Phoenix Feather – Upon death, revives the player with 1 health, then burns up.
        # Gravedigger’s Coin – Revive the player one time to full health for 100 gold
        # Blood Pact Scroll – Allows revival at the cost of a permanent debuff.



    ## utility:
        ### Keys:
            # lockpick, has a 1/3chance to open the door and persist
            # Skeleton Key – Unlocks any door but disappears after 1 use
            # Blood Key – Unlocks any door but costs health
            # Soul Key – Unlocks any door but costs souls
            # Cursed Key – Unlocks any door but gives a random curse


        # Echo Bell – Creates a noise at a targeted location to lure enemies away.
        # Cloak of Shadows – Temporarily makes the player invisible to enemies.
        # Faded Hourglass – Slows down nearby enemies movement
        # Ethereal Chains – snares nearby enemies for a short duration.
        # Recall Parchment – Teleports the player back to the last shrine visited.


        Crystal Skull, reduce clatter level by 1, only 1 use
        Torch of Guidance - Reveal the portal shrine on minimap
        Rope Hook – Can be thrown to pull the player across gaps.
        Alchemy Flask – Randomly turns a minor item into another item upon use.
        Dungeon Map Fragment – Reveals part of the current dungeon layer.

    ## Combat item
        # electric Bomb – electric explosion
        # Fire Bomb – Fire explosion
        # Frozen Bomb – Frozen Explosion
        # Poison Bomb – Poison Explosion
        # Vampiric Bomb – Vampiric Explosion

        Oil Flask – Can be thrown to create a flammable puddle.
        Holy Water – Weapons deals extra damage to undead and ghosts.
        Hexing Charm – Weakens the next enemy hit, cooldown.
        Hunter’s Fang – Increases weapon damage against beasts.
    
    ## Cursed Items:
        Items are soul bound, meaning destroyed when dropped
        # Blood tomb, Gain souls when damaged
        # Demonic Bargain – Increases damage output but prevents healing
        # Temptress Embrace - Reduces damage output when health > 50% but increases below 50%
        # Black Coin – Increases gold earned but increases damage taken
        # Vampire’s Locket – Grants lifesteal but disables all other healing.
        # Forsaken Grimoire – Increases rune power but reduces player strength

        Eldritch Mirror – Reflects a portion of damage taken but doubles negative status effect duration.
        Cracked Talisman – Grants resistance to elemental damage but causes physical damage to double
        Echoing Skull – Reveals hidden secrets in the dungeon but whispers eerie sounds, attracting enemies

    ## Gems
        Different gems that gives attributes to weapons, also valuable to sell
        # fire - Set fire effect on weapon
        # freeze - Set freeze effect on weapon
        # poison - Set poison effect on weapon
        # vampiric - Set vampiric effect on weapon
        # electric - Set electric effect on weapon
        # Arcane hunger - Set Arcane hunger effect on weapon
        # blunt - Set blunt damage on weapon
        # slash - Set slash damage on weapon
        # halo - Grants wielder a chance to protect from damage
        # power - Increases rune power while equipped
        # range - Increases weapon range
        # resistance - Chance for weapon not to take damage
        # speed - Increases weapon attack speed
        # strength - Increases wielders strength
        # terror - Chance for enemies to run away
        # vulnerable - Entities hit take extra damage
        # weakness - entities hit gets weakness
        # wet - Set wet effect on weapon, can combo with electric, water and fire (steam)
        # durability - Increases weapon health
        multishot - Fires two arrows at a time

    ## Ingots
        # Can be used to repair items and add upgrades, also have high value at market depending on rarety
        # Steel ingot - repairs weapons
        # Jade ingot - repairs runes
        # copper ingot - repairs items
        # Gold ingot - can add gem slots
        # Silver ingot - can upgrade rune power


    ## Potions
        # Based on player effects
        # Health
        # strength
        # movement
        # Soul
        # health regen, more health than health potion but slower
        # silence
        # invisibility
        # poison resistance
        # fire resistance
        # freeze resistance
        # luck
        # vampire, heals based on damage dealt

# Runes
    You can have 3 runes equipped at a time
    Can buy new runes or upgrade existing ones in shrines 

    Costs souls each time it's cast
    Two types of runes, passive runes and activated runes
    Passive runes don't cost souls, but they are less powerful
    Active runes:
        # Dash,
        # Healing
        # Speed
        # Invisibility
        # Silence
        # Door unlock
        # Speed
        # Strength
        # Immunity
        Random Teleport to a random telport circle, to get out of bad situations
        Scream, make enemies run away from you
        # Vampiric, regen from damaging enemies
    
    Passive Runes:
        # Regen
        # Light
        # Arcane conduit, increase power level of your other runes
        # arcane_Hunger, increase souls generation
        # Magnet, Auto pickup of items
        # Resistance
        Thorns, enemies take damage when they hit you
        Frost Shield, enemies freeze when damaging you

    Fire runes:
        # Fireball, ball of fire that leads to fire explosion
        # Fire spew, flamethrower attack
        Fire wall, wall of fire that damage anything that tries to cross it
    
    Frost runes:
        # Iceball, ball that causes a freeze explosion that slows everything in it
        # Ice projectiles, fast ice projectiles shot like a bullet
        ice storm, Creates a tornado on entity that shoots ice projectiles at random 

    Electric runes:
        # Chain ligtning, Lightning projectile that bounces between entities
        # Electric ball, electric ball that generates electric explosion
        # Electric homing particle, electric projectiles that target nearest entity

    Poison runes:
        # Poison ball, Poison ball that turns into a poison cloud
        # Posion cloud, creates a big poison cloud around entity, area of effect
        # Poison plumes, creates  poison clouds around entity at random positions

    Vampiric runes:
        Life drain, slowly drain health from all nearby entities
        # Soul reap, broad projectile that sucks health from everything it hits
        # Soul pit that pulls entities in and sucks health from them

# Arrows:
    # Basic Arrow, Higher base damage
    Rope arrow, allows you to cross traps
    Fire arrow, lights enemies on fire and lights up the envoirement
    Ice arrow, ice effect, if it touches water it freezes the water
    Poison arrow, poison effect, if it touches water it poisons it
    Electric arrow, electric effect, triggers traps and electrifies water

# Movements:
    # Dash, Move rapidly without hit detection to a location
    # Roll, avoid damage and roll in the direction of the mouse
    # Backstep, move backwards a little and be immune
    # Block, block damage, if the player has shield block all damage, if not then it only blocks melee

# Effects:
    # Fire – Burns the entity over time, dealing continuous damage.
    # Poison – Deals damage over time, but slower than fire.
    # Frozen – Slows movement speed and attack speed, may completely immobilize if stacked.
    # Wet – Makes the entity take extra damage from electric attacks and reduces fire damage.
    # Regeneration – Slowly restores health over time.
    # Speed Boost – Increases movement speed for a duration.
    # Strength Boost – Increases melee attack damage.
    # Invisibility – Makes the player undetectable by enemies unless they attack or make noise.
    # Fire Resistance – Reduces or nullifies fire damage.
    # Poison Resistance – Reduces or nullifies poison effects.
    # Frozen Resistance – Reduces or nullifies freeze effects.
    # Electric Charge – Causes electric attacks to arc to nearby enemies.
    # Silence – Prevents the affected entity from casting spells or using magic-based attacks.
    # Luck Boost – Increases the chance for critical hits, rare drops, or dodging attacks.
    # Vampirism – Heals based on damage dealt.
    # Shielded – Grants temporary immunity to damage until shield is broken.
    # Thorns – Reflects damage back to attackers.
    # Magnetized – Automatically attracts loot, gold, and items.
    # Slow – Reduces movement and attack speed.
    # Curse – Lowers stats temporarily or causes random negative effects.
    # Confusion – Inverts enemy movement or attack patterns.
    # Stone – Immobilizes but provides high defense.
    # Snare – Stops movement for a short period.
    # Arcane conduit - Reduce the cost runes
    # Arcane_Hunger - Gain souls from entity kills
    Terror – Makes enemies flee from the player.
    

# Rooms:
    # Walls generated in dungeon generator and loot determined by the room type in decoration handler
    # Treasure room, contains loot
    # Library, contains bookshelves and potion tables
    # Boss room, spawns a boss that then spawns a weapon or rune shrine when killed
    # Lakes, can be any kind of elements
    Trapped room, contains traps but more valuable loot


# Enemies:
    Enemies start out basic but can upgrade to elite as dungeon effects trigger
    Spawn enemies using dungeon director when effects trigger
    Enemies have a difficulty attribute to make the spawning dynamic
    Enemies seperated into tribes with different strengths and weaknesses
    - pack swarms the player
    - Solo, goes after the player alone
    - Scout, looks for and calls allies to attack the player
    - Sentry, calls enemies in a wide range to notify if they spot the player, but they don't move unless they see the player
    - Ambusher, waits and attacks the player
    - Support, supports the other enemies with healing
    - Ranged, shoots the player from range 
    - Melee, attacks the player up close

### Shared decorations
    - # Braziers with fire, lights up area, can be extinguished/ignited
    - # Pots and urns that can be smashed to get loot, generates clatter
    - # Chest, standard loot, safe but multiple tiers that can determine the loot table
    - # Weapon racks, contains weapons
    - # Teleportation Circles, linked to each other, can be used to traverse the dungeon
    - Shops where you can buy different items for gold, maybe a little kobold with a shop. This happens when you transition between levels, use it hide loading screen. Opens a menu, you can sell loot for gold and use gold to buy random selection of items
    - # Campfires, rest locations player can regain 50% hp, one per floor, one per floor, using it increases awakening by 1
    - # Sacrifice Shrine, sacrifice loot for rewards, which are status effects. Scales with the gold value of the sacrificed item
    - # Soul well, Sacrifice items for souls but can summon/attract enemies
    - # Portal Shrine, each floor has a portal shrine that can be activated using scaling souls cost. Will transport the player to the next dungeon layer. Player needs to hunt enemies or sacrifice loot at 


### Loot mechanic
    - # 3 attributes that affect the loot, depth (1 to 7), clatter (0 to 5) and luck (0 to 10), depth being the most important
    - # 5 tiers of items with the following basic drop rates
        - Common: 400
        - uncommon: 300
        - rare: 200
        - Epic: 80
        - Legendary 20
    - # Formula something like this:
        mult = 1
            + Depth*(tier_norm*1.6 - 0.20)
            + luck*(tier_norm*1.0)
            - Clatter*(tier_norm*0.8 - 0.10)
            
    - # Design loottables for more powerful items to have higher rarities
    - # Basic items that are higher rarity like gems or gold will have a higher amount to represent higher quality
    - # Weapons will have buffs applied to them randomly according to their rarity, common will have none.
        - Generate file with random names based on the rarity of the weapon
    - # Status effects will also have a loot table, where higher quality status effects will be smaller amount at higher rarities and commons will have higher amounts
    - Runes will also be buffed depending on rarity
    - When opening loot container or shrine, 3 options are presented to the player, optional if positive and forced if negative
    - # If a loot container is smashed (like vase) a random item is provided based on the rarity formula
    - # Different kinds of loot containers have different base levels, for example an epic chest will only spawn epic or above loot, meaning the tier distribution becomes Epic 80 and legendary 20
        - # Loot containers get better the deeper in the dungeon you go, each depth layer allows spawning of new types of container, depth 1 only common and uncommon, 2 adds rares, 3 adds epic and 4 adds legendary
    - # Different loot tables based on loot containers, loot containers dictated by dungeon and room type
    - # When spawning loot, check the current player attributes and inventory and increase spawn chance of synergy items for better player experience

# Dugeon types
## Ancient Tomb - COMPLETE
### Description
    Long forgotten tomb of an ancient culture that worshipped the dead
### Specialty
    Basic dungeon, used as introduction
### Enemies
    # Skeleton Warrior, basic warrior uses standard weapons
    # Skeleton scout, uses ranged weapons
    # Skeleton Cleric, heals undead in the area but does no damage
    # Skeleton Bell Toller, alerts nearby enemies if it sees the player
    # Skeleton Undertaker, revieves dead enemies
    # Skeleton Guard, slow, high health and medium damage
    # Skeleton warlock, uses magic poison attacks
    # Wight Lord, boss, armoured skeleton with shield and sword, can dash to close range
    # Banner bearer, Increases strength of nearby enemies
    # Phantom, immune to physical attacks, pathfinds directly to the target, phasing through walls, high damage, high speed and low health
    # Wraith, immune to physical attacks, pathfinds directly to the target, phasing through walls, low damage but steals soul (player mana), high speed and low health
    # Shade, immune to physical attacks, will always pathfind towards player, medium damage, low speed, low health
    # Vampire, boss, life steal, flying bat form when travelling, close combat
    # Crypt Ghoul, bone club, fast and high damage, but glass cannon

### Traps
    - # Soul bind, disables player healing and spawns item (soul shard) that needs to be found to enable healing again
    - # Pressure plate that opens nearby tombs and spawns enemies
    - # Bell trap from pressure plate, that alerts nearby enemies
    - # Spike pits, fall into and slows you down
    - # Spike traps, that move up and harm you when they're extended
    - # Loose rubble, generates clatter when stepped on
    - # Arrow traps - shoots arrows, triggered by pressure plates
### Decorations
    - # Braziers with fire, lights up area, can be extinguished/ignited
    - # Plinths, contains runes
    - # Rune shrine, pay souls to aquire new runes
    - # False walls, can be destroyed to reveal treasure rooms
    - # Levers that spawn items, open doors etc when activated
    - Blood Fountains player loses half current health, gets permanent vampiric 1
    
    


## Crystal Caverns
### Description
    Caverns that resonate with strange energies
### Specialty
    Crystal Growth, walls occasionally dissapear or spawn changing the structure of the dungeon. Spawned walls can be broken
    Weapon gems spawn more often
    Crystaline enemies that grow a crystal skin that acts as armor, grows back if not damaged for a while
### Enemies
    # Earth Elemental, high health and strength, close combat
    # Ice spirit, shoots freeze projectiles
    # Fire spirit, high speeds shoot flamethrower at close range and retreats
    # Electric Elemental, damages the player indirectly if in range
    # Poison Elemental, creates poison plumes around the player and explodes when damaged
    # Minotaur, boss mob, charges and breaks envoirement, high damage, low defence
    # Medusa, shoots electric projetiles and fast but very low health, will switch to melee if player is to close, chance to stun player if player mouse is closer to medusa than player
    # Clicker, blind but good hearing, prefers the dark and can detect the faintest sounds
    # Echo shard, becomes visible for 10 seconds when clatter is generated
    # Echo Wraith, teleports close to clatter source when clatter is generated
    # Crystal Scarab, basic enemy that swarms player, immune to magic
    # Hydra, boss mob, regens health fast, gains immunity to the last effect type that damaged it
    Kobold, steals items from player and runs away
### Traps
    - Crystal shards, shoots crystal spikes, basically arrow trap
    - Shifting walls, changes the layout of the dungeon
    # Unstable Crystals, explode when damaged
    # Spike pits, fall into and slows you down
    # Loose rubble, generates clatter when stepped on
### Decorations
    # Glowing crystals, lights up area, can be shattered to remove light
    # Small rocks strewn around
    # Gem shrine, Spawns a high level gem somewhere in the dungeon
    # Amplifying node, runes are more effective when in range
    # Crystal plinths, contains gems
    # Harmonic crystal, activate to generate souls, but generate clatter
    # Crystal Fountains gives player damage resistance when interacted with
    - Crystalisation shrine, give a gem and return a random one in return with negative 1 effectiveness, trade in low value gem for potential to get better gem
    - Weapon shrine, pay souls to bind gems to weapons for bonuses increased bonuses
    - Fragile walls, can be broken by hitting with blunt weapons, acts as doors
    - Blood shrine, Gives an item that tracks player kills, when 10 are killed reduce awakening level
    - Prism pedestal, activate to disable shifting walls



## Mycelium Depths enemies
### Description
    In the deep dark the roots of the world have come alive
### Specialty
    Mycelium network, clank is disabled. Instead enemies are aggroed by attacks or stepping on spore traps
    Potions spawn more often
### Enemies
    Fungal burrower, digs under the maps and attacks player from underground
    Unstable spore, charges and explodes if it touches the player with a short delay
    Sporeling, fast and small spores that attacks player
    Fungal brute, strong and slow mushroom creature, weak to fire
    Spore spitter, ranged enemy that shoots spores
    Poisioned spores, spawns poison plumes
    Glowcap Stalker, pretends to be a decorative mushroom and attacks when player is close, emits light
    Mycelium roots, snares the player
    Vitalcap, heals nearby enemies
    Gravebloom, hiding somewhere on the map. Needs to be killed to prevent enemies respawning
    Rot king, can snare player and spawns sporelings
### Traps
    - Vines, snare the player if stepped in
    - Glowing mushrooms, explodes when player to close
    - Burrows, enemies spawns if player gets to close
    - Spike traps poison, that move up and harm you when they're extended, 
    - Toxic clouds, weakens player if in radius
    - Fungal pathch, generates clatter when stepped on
### Decorations
    - Glowing mushrooms, lights up area, can be shattered for random effect, sometimes explode, heal etc
    - Blood shrine, activate with blood sacrifice, spawns mushrooms when killing enemies
    - Small mushrooms and roots strewn around
    - Fungal growth, can be plucked for mushrooms, regrows if enemy is killed nearby
    - Shroom shrine, Spawns a rare mushroom that can be consumed for high level permanent effect
    - Root walls, can be destroyed to reveal treasure rooms
    - Spore bloom, activating heals player, but generates clatter
    - Overgrown cache, destroy to reval potions / mushrooms


## Serpents Lair
### Description
    Ancient culture that guards the world from a curse
### Specialty
    Quatlz curse, player will slowly get more and more curse the longer they stay. Gold idols loot spawned throughout map to reduce Quatlz curse
    Cursed items spawn more often
### Enemies
    Serpent Warriors, basic enemies that are decently strong individually
    Chameleons scouts, shoots poisoned darts, slightly transparent and difficult to spot
    Skink fanatics, high damage low health that charges the player aggressively
    Salamander hunters, shoots fire projectiles and high mobility, hunts in packs
    Temple guards, large crocodiles with high defence that aim to hold player in place
    Komodo priests, increases strength of nearby enemies, reduces Quatlz curse when killed
    Quetzalcoatl shaman, heals nearby enemies, reduces Quatlz curse when killed
    Ancient Tyrant, bos box t-rex, high damage and speed but low defence
    Embermaw, boss shoots fire from the front and has ball tail in back that can attack player, high defence and damage, but low movement 
    Great Python, constricts the player for a time allowing other enemies to attack
    Venomscale Lurker, posioned attack that jumps at player
### Traps
    - Vines, snare the player if stepped in
    - Poison darts, shoots darts at player
    - Cursed totem, weakens player if in radius
    - Gass vents, spawns gass clouds
    - Swinging blade, swing from central tile, all affected tiles are marked as traps, rotate the sprite as it swings
    - # Spike traps poison, that move up and harm you when they're extended, 
    - # Loose rubble, generates clatter when stepped on
### Decorations
    - # Braziers with fire, lights up area, can be extinguished/ignited
    - Spawning pool, enter to gain a permanent buff
    - Venemous idol, pay gold to gain poison resistance
    - Camouflaged cache, hidden treasure rooms behind vines
    - Shedding altar, activate to lose max health, but remove all curses
    - Offering altar, place cursed item to remove negative effect, pay with souls
    - Cleansing pool, reset Quatlz curse
    - Hunter Trial shrine, kill X enemies and gain immunity from Quatlz curse
    - Offering stone, sacrifice cursed item for a blessing



## Titan Forge
### Description
    Forge masters of the deep, that have combined metal and demon
### Specialty
    Ash storms, lowers visibility for a period of time at random
    Utility items spawn more often
    Better opportunity to upgrade weapons
    Overheat, player will slowly become slower and start taking damage unless cooled
### Enemies
    Magma warden, Molten armor, high health and damage, but low speeds, sets player on fire if contact
    # Fire spirit, high speeds shoot flamethrower at close range and retreats
    Ash wraith, invisible until close then ignites and attacks player. High speed and damage, very fragile
    Ironbound demon, wraps player in chains to temporarily snare, low speed and damage, but high health
    Forge demon, revives fallen enemies
    Ember swarm, small enemies that swarm the player and do little damage, but dangerous in swarm
    Molten slug, immortal enemy that moves very slowly but very high damage if it touches player
    Phoenix, explodes when killed and revives itself. High speed, low damage and health
    Lava Lurker, hides in lava pools and jumps on the player, high damage and speed, but low health
    Ashen Tyrant , shoots burning chains out to attack player. Chains deal damage and pulls the player into lava traps.
    Forgeheart Titan, boss, shoots fireballs, high health and low speed. Area of effect attacks
### Traps
    - Explosive barrels, explodes when destroyed
    - Molten floor, gradually spawn lava tiles when pressure plate is triggered
    - Flamethrower trap triggered by pressure plate
    - Fire traps, sets you on fire
    - # Spike traps, that move up and harm you when they're extended
    - Arrow traps - shoots arrows, triggered by pressure plates
    - Loose rubble, generates clatter when stepped on
### Decorations
    - Forge anvil, when adding ingots to weapon, improved efficiency
    - Cooling basin, resets heat meter
    - Grindstone, increases weapon damage, but decreases durability
    - Shrine of war, sacrifice items for legendary weapons
    - Scrap heap, search for utility items and ingots
    - Smelter, smelt weapons for ingots
    - 

# Glacial Caverns
### Description
    Eternal winter and ancient creatures haunt this land
### Specialty
    Player needs to seek out heat sources (fire) to prevent freezing to death
    Runes spawn more often
    Lots of ice lakes changing movement
### Enemies
    Ice spirit, shoots freeze projectiles
    Shard golemn, explodes when killed, slow and high health, but low damage
    Glacial spider, hides in snow and shoots freeze projectiles and inflict frost on bites
    Yeti, mid speed, damage and health melee attack
    Frost warden, high defence and slow. Inflict slow in a radius around it
    Frost wolf, attacks in packs, weak individually, howls to attract others when one spots player
    Femir, wolf monsters with clubs. Medium damage and health, but high speed
    Shaman, summons blizzards
    Ice demon, boss, lowers temperature in area and causes player to freeze faster. High health and damage, but slow
    Leshy, boss, snares player with roots and shoots projectiles. Can teleport away when damage threshold is reached
### Traps
    - Freezing pools, water tiles that slows and damages player
    - Icicle drops, when clatter is generated, chance to drop icicle with short warning 
    - Thin ice, causes the player to fall through into iceicle pit trap
    - Freeze vents, spawns frozen storm
    - Cracking ice, generates clatter

### Decorations
    - Ice walls, use torches / fire to melt
    - Frost shrine, sacrifice souls to gain freeze resistance
    - Ice lanterns, glows but does not heat
    - Frozen statues, thaw with fire, can spawn loot of enemies
    - Rune smith, use gem and ingot to create random rune (determined by their value)
    - Icicles growing out of the ground, can be shot for explosion effect