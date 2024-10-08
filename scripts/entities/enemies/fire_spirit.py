from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.projectiles.fire_particle import Fire_Particle


import math


class Fire_Spirit(Enemy):
    def __init__(self, game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina)
        
        self.animation = 'fire_spirit'
        self.path_finding_strategy = 'ignore_lava'
        self.attack_strategy = 'medium_range'
        self.look_for_health_cooldown = 0
        self.fire_cooldown = 0
        self.spewing_fire = False

        self.animation_num_max = 3
        self.attack_animation_num_max = 3
        self.attack_animation_num_cooldown_max = 100
        self.animation_num_cooldown_max = 100

    def Update(self, tilemap, movement = (0, 0)):
        
        super().Update(tilemap, movement)

        self.Look_For_Health()

        if self.distance_to_player < 60:
            self.Attack()

        if self.distance_to_player > 70 and self.charge:
            self.charge = 0


        
    
    def Attack(self):
        if not super().Attack():
            return
        self.charge += 1

        if self.charge >= 100:
            self.spewing_fire = True

        if self.spewing_fire:
            self.Fire_Particle_Creation()

        if self.charge <= 0:
            self.spewing_fire = False
    
    def Fire_Particle_Creation(self):
        self.Set_Target(self.game.player.pos)
        self.Set_Attack_Direction()
        # Handle cooldown for spacing between fire particles
        if self.fire_cooldown:
            self.fire_cooldown -= 1
            return
        else:
            self.fire_cooldown = 3
            self.charge = max(0, self.charge - 20)

        # Basic raycasting attributes
        num_lines = 8  # Define the number of lines and the spread angle (in degrees)
        spread_angle = 50  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1)  # Calculate the angle increment between each line

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(self.attack_direction[1], self.attack_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)

        damage = 1
        speed = 1
        max_range = 50

        # Generate fire particles
        for j in range(num_lines):
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle) * speed
            pos_y = math.sin(angle) * speed
            direction = (pos_x, pos_y)

            # Create the fire particle with the direction
            fire_particle = Fire_Particle(
                self.game,
                self.rect(),
                (2, 2),
                'fire_particle',
                damage,
                speed,
                max_range,
                'particle',
                self.charge,
                direction, 
                self
            )

            self.game.item_handler.Add_Item(fire_particle)

    # TODO: IMPLEMENT 
    def Look_For_Health(self):
        if self.look_for_health_cooldown:
            self.look_for_health_cooldown = max(0, self.look_for_health_cooldown - 1)
            return
        

        if self.health < self.max_health / 2:
            self.Set_Locked_On_Target(0)

            self.look_for_health_cooldown = 2000

            nearby_traps = self.game.trap_handler.Find_Nearby_Traps(self.pos, 200)
            for trap in nearby_traps:

                if trap.type == 'Lava_env':
                    self.Find_New_Path(trap.pos)
                    self.locked_on_target = True
                    break

            self.Set_Locked_On_Target(4000)
        
        return

    def Set_Idle(self):
        pass

    def Set_Action(self, movement):
        # Check for movement
        if not movement[0] and not movement[1]:
            self.Set_Animation('standing_still')
            return
        

        if movement[1] or movement[0]:
            self.Set_Animation('running')
            return

    def Set_On_Fire(self, fire_time):
        self.status_effects.Set_Effect('health', fire_time)
        return False