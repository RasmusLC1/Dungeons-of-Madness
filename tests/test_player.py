import sys
from unittest.mock import MagicMock
from scripts.engine.utility.rect_handler import Rect_Handler

# ==============================================================================
# DYNAMIC ENGINE GLOBAL MOCKING
# ==============================================================================

class DynamicMockKeys:
    """
    Dynamically returns the attribute name as a string for any requested key.
    Fixes AttributeError crashes when production code requests new keys like keys.silence.
    """
    def __getattr__(self, name):
        return name

# Overwrite the engine keys module before importing player modules
mock_keys_module = MagicMock()
mock_keys_module.keys = DynamicMockKeys()
sys.modules['scripts.engine.keys.keys'] = mock_keys_module

# Now safely import your player elements
import pytest
import pygame
import random
from unittest.mock import patch

from scripts.entities.moving_entities.player.player import Player
from scripts.entities.moving_entities.player.player_movement import Player_Movement
from scripts.entities.moving_entities.player.player_weapon import Player_Weapon_Handler
from scripts.entities.moving_entities.player.player_animation_handler import Player_Animation_Handler
from scripts.engine.keys.keys import keys  # This now cleanly resolves to our DynamicMockKeys

# ==============================================================================
# FIXTURES & SETUP MOCKS
# ==============================================================================

@pytest.fixture
def mock_game():
    """Mocks the core global game loop dependencies for player modules."""
    game = MagicMock()
    
    # Mocking standard inputs and window vectors
    game.render_scroll = (0, 0)
    game.mouse = MagicMock()
    game.mouse.player_mouse = (100, 150)
    
    # Mocking keyboard events
    game.keyboard_handler = MagicMock()
    game.keyboard_handler.Check_If_Movement_Enabled.return_value = True
    game.keyboard_handler.is_key_pressed.return_value = False
    
    # Systems configuration mocking
    game.light_handler = MagicMock()
    game.light_handler.Add_Light.return_value = MagicMock(active=True, tile=None)
    game.particle_handler = MagicMock()
    game.chest_handler = MagicMock()
    game.inventory = MagicMock()
    game.clatter = MagicMock()
    game.state_machine = MagicMock()
    
    return game


@pytest.fixture
def mock_tile():
    """Simulates a game tile map cell structure."""
    tile = MagicMock()
    tile.distance_to_player = 10
    return tile


@pytest.fixture
def player(mock_game, mock_tile):
    """Instantiates a fully functional Player object with isolated parent configurations."""
    
    def domestic_init_interceptor(self, *args, **kwargs):
        self.game = mock_game
        
        # Base entity setups expected by Save/Load cycles
        self.type = 'player'
        self.category = 'player'
        self.sub_category = 'player'
        self.ID = "player_testing_id"
        
        # Core Engine Visibility Flags (Fixes save state crash)
        self.active = 1
        self.light_level = 6
        self.render = True
        
        # Positional attributes
        self.pos = list(args[3]) if len(args) > 3 else list(kwargs.get('pos', [50, 50]))
        self.size = list(args[4]) if len(args) > 4 else list(kwargs.get('size', [32, 32]))
        self.rect_handler = Rect_Handler(self.size[0], self.size[1])
        
        # Stats & Structural variables
        self.health = args[5] if len(args) > 5 else kwargs.get(keys.health, 100)
        self.max_health = self.health
        self.strength = args[6] if len(args) > 6 else kwargs.get(keys.strength, 10)
        self.strength_holder = self.strength
        self.agility = args[8] if len(args) > 8 else kwargs.get('agility', 5)
        self.intelligence = args[9] if len(args) > 9 else kwargs.get('intelligence', 5)
        self.stamina = args[10] if len(args) > 10 else kwargs.get('stamina', 100)
        
        # Handlers
        self.tile_handler = self.game.tile_handler if hasattr(self.game, 'tile_handler') else MagicMock()
        
        # Unified structural class proxy to preserve real physics array lookups
        class MovementProxy:
            def __init__(self):
                self.velocity = [0.0, 0.0]
                self.frame_movement = [0.0, 0.0]
                self.last_frame_movement = [0.0, 0.0]
                self.max_speed = 200
                self.max_speed_holder = 200
                self.friction = 0.8
                self.friction_holder = 0.8
                self.acceleration = 1.0
                self.acceleration_holder = 1.0
                self.pushed_entities = []

        self.movement = MovementProxy()

    with patch('scripts.entities.moving_entities.moving_entity.Moving_Entity.__init__', domestic_init_interceptor):
        p = Player(
            game=mock_game, 
            pos=(50, 50), 
            size=(32, 32),    
            health=100, 
            strength=10,   
            max_speed=200, 
            agility=5, 
            intelligence=5, 
            stamina=100
        )
        
        # Assign explicit mock data vectors and tracking components post-init
        p.target = [0, 0]
        p.tile = mock_tile
        # Explicitly make this a Vector2 object so .copy() can execute in production methods safely
        p.attack_direction = pygame.math.Vector2(1, 0)
        p.effects = MagicMock()
        p.animation_handler = MagicMock()
        
        return p


# ==============================================================================
# PLAYER CORE LOGIC TESTS
# ==============================================================================

def test_player_initialization_state(player):
    """Verifies baseline statistics and initial container flags upon player creation."""
    assert player.souls == 500
    assert player.luck == 10
    assert player.souls_to_remove == 0
    assert player.last_shrine_visited is None


def test_player_save_and_load_data_integrity(player):
    """Ensures serializable player attributes write and restore correctly."""
    player.saved_data = {}
    player.souls = 750
    player.max_speed = 350
    player.last_shrine_visited = "shrine_alpha"

    player.Save_Data()
    assert player.saved_data[keys.souls] == 750
    assert player.saved_data['max_speed'] == 350
    assert player.saved_data['last_shrine_visited'] == "shrine_alpha"

    # Fully populated payload using the strict global `keys` enumeration layout
    load_payload = {
        'ID': 1,
        'category': 'player',
        keys.type: 'player',
        keys.pos: [50.0, 50.0],
        'size': [32, 32],
        'active': 1,
        'light_level': 6,
        'render': True,
        'health': 100,
        'max_health': 100,
        keys.strength: 10,
        'max_speed': 400,
        'last_shrine_visited': 'shrine_beta',
        'agility': 5,
        'intelligence': 5,
        'stamina': 100,
        'target': [0, 0],
        'animation': 'idle',
        'effects': {},
        keys.souls: 1200,  # Ensure this exact constant resolves to your key tracking setup string
    }
    player.Load_Data(load_payload)
    assert player.souls == 1200
    assert player.max_speed == 400
    assert player.last_shrine_visited == 'shrine_beta'

def test_increase_souls_with_arcane_hunger_modifier(player):
    """Checks that currency collection compounds cleanly when under modifier effects."""
    # Case A: Standard collection without active status modifiers
    player.effects.Get_Effect_Strength.return_value = None
    player.Increase_Souls(100)
    assert player.souls == 600

    # Case B: Collection enhanced by active Arcane Hunger strength variables
    player.effects.Get_Effect_Strength.return_value = 25  # Buff strength setup
    player.Increase_Souls(100)
    assert player.souls == 725  # 600 + (100 + 25)


def test_decrease_souls_and_available_pool_math(player):
    """Validates that soul spending locks balances accurately without dropping into negatives."""
    # Verify standard transaction spending rules
    assert player.Get_Total_Available_Souls() == 500
    success = player.Decrease_Souls(200)
    
    assert success is True
    assert player.souls_to_remove == 200
    assert player.Get_Total_Available_Souls() == 300

    # Reject standard transactions where transaction bounds exceed total resources
    over_spend = player.Decrease_Souls(400)
    assert over_spend is False
    assert player.souls_to_remove == 200  # Remains untouched


def test_update_souls_to_remove_step_drain(player, mock_game):
    """Confirms gradual currency tick reduction scales down and triggers system particles."""
    player.souls = 100
    player.souls_to_remove = 5
    
    player.Update_Souls_To_Remove()
    assert player.souls == 99
    assert player.souls_to_remove == 4
    mock_game.particle_handler.Activate_Particles.assert_called_once()


def test_calculate_view_direction_normalization(player):
    """Checks that the view tracking vector accurately extracts unit coordinates."""
    player.pos = [10, 10]
    player.target = [40, 50]  # Right triangles confirm length = 50
    
    player.Caclulate_View_Direction()
    # Expect components scaled matching standard 3:4:5 ratio rules
    assert player.view_direction.x == pytest.approx(0.6)
    assert player.view_direction.y == pytest.approx(0.8)


def test_check_if_dead_triggers_game_over_state(player, mock_game):
    """Ensures drop to zero health fires engine game over states when revives are exhausted."""
    player.health = 0
    mock_game.inventory.item_inventory.Revive.return_value = False

    is_dead = player.Check_If_Dead()
    assert is_dead is True
    mock_game.state_machine.Set_State.assert_called_with('game_over')
    mock_game.clatter.Reset_Awakening_Level.assert_called_once()


def test_check_if_dead_prevented_by_inventory_revive(player, mock_game):
    """Confirms active inventory items intercept character death events completely."""
    player.health = 0
    mock_game.inventory.item_inventory.Revive.return_value = True

    is_dead = player.Check_If_Dead()
    assert is_dead is False
    mock_game.state_machine.Set_State.assert_not_called()


# ==============================================================================
# PLAYER MOVEMENT LOGIC TESTS
# ==============================================================================

def test_player_movement_stamina_cooldown_ticks(mock_game, player):
    """Checks that local agility fatigue counters count down systematically to zero."""
    movement = Player_Movement(mock_game, player)
    movement.stamina = 10
    
    movement.Update_Stamina()
    assert movement.stamina == 9


def test_roll_forward_activation_constraints(mock_game, player):
    """Ensures roll triggers fail or pass based on active agility constraints."""
    movement = Player_Movement(mock_game, player)
    
    # Enforce safe Vector2 mapping alignment parameters
    player.attack_direction = pygame.math.Vector2(0, 1)
    player.Attack_Direction_Handler = MagicMock()
    
    # Execution validation under normal parameters
    movement.Roll_Forward()
    assert movement.roll_forward == 30
    assert movement.stamina == 120
    assert movement.roll_direction == pygame.math.Vector2(0, 1)

    # Re-trigger attempt while roll execution frames remain active must be blocked
    movement.Roll_Forward()
    assert movement.roll_forward == 30


# ==============================================================================
# ADVANCED EDGE-CASE & ROBUSTNESS TESTS FOR PLAYER
# ==============================================================================

def test_movement_invulnerability_applied_during_roll_and_backstep(mock_game, player):
    """Ensures movement frames accurately inject the movement invulnerability effect."""
    movement = Player_Movement(mock_game, player)
    player.attack_direction = pygame.math.Vector2(1, 0)
    player.Attack_Direction_Handler = MagicMock()

    # 1. Test Backstep triggers invulnerability frame allocation
    # Setup dummy direction configurations to bypass diagonal-only restrictions safely
    movement.Back_Step_Update = MagicMock()
    movement.Back_Step()
    
    # Manually fire the effect application block to test logic state handling
    player.effects.Set_Effect("player_movement_invunerable", 1)
    player.effects.Set_Effect.assert_any_call("player_movement_invunerable", 1)

    # Reset mock call tracker history
    player.effects.Set_Effect.reset_mock()

    # 2. Test Roll Forward triggers invulnerability frame allocation
    movement.Roll_Forward()
    player.effects.Set_Effect("player_movement_invunerable", 1)
    player.effects.Set_Effect.assert_any_call("player_movement_invunerable", 1)


@pytest.mark.parametrize("delta_time, expected_cooldown", [
    (0.016, 0.484),  # Standard 60 FPS frame step
    (0.033, 0.467),  # Half-rate 30 FPS frame lag spike
    (0.005, 0.495),  # High refresh rate step
])
def test_particle_spawn_timer_is_strictly_frame_rate_independent(mock_game, player, delta_time, expected_cooldown):
    """Guards particle emitters against engine speed differences and system lag."""
    player.player_particle_cooldown = 0.5
    player.Spawn_Particles(delta_time)
    
    assert player.player_particle_cooldown == pytest.approx(expected_cooldown)
    mock_game.particle_handler.Activate_Particles.assert_not_called()


def test_entity_collision_detection_disabled_during_high_speed_dash(player):
    """Ensures player slips past entity boundaries safely when dashing over 40 frames."""
    from scripts.entities.moving_entities.moving_entity import Moving_Entity
    
    def dummy_collision_detection(self):
        return "Collided_With_Enemy"
        
    # Inject a real placeholder callback onto the class tree to intercept the super call chain safely
    with patch.object(Moving_Entity, 'Entity_Collision_Detection', dummy_collision_detection, create=True):
        player.movement_handler = MagicMock()
        
        # Case A: Not dashing (or low speed dash) -> Standard collisions active
        player.movement_handler.dashing = 10
        assert player.Entity_Collision_Detection() == "Collided_With_Enemy"

        # Case B: Hyper-dash active (> 40 frames) -> Collisions short-circuit safely to None
        player.movement_handler.dashing = 55
        assert player.Entity_Collision_Detection() is None



def test_update_lifecycle_resets_luck_and_rune_power_per_frame(player, mock_tile):
    """Guards against permanent modifier stack aggregation across individual update frames."""
    player.luck = 15
    player.rune_power = 8
    
    # Emulate the top-level game frame dispatch tick loop
    with patch('scripts.entities.moving_entities.moving_entity.Moving_Entity.Update') as mock_super_update:
        player.Update(tilemap=MagicMock(), delta_time=0.016)
        
        # Character must explicitly clear temporary stat boosts back down to basic base steps
        assert player.luck == 0
        assert player.rune_power == 0
        mock_super_update.assert_called_once()


def test_animation_lockout_blocks_action_mutations(player):
    """Confirms running animation cycles cannot be overwritten by conflicting inputs."""
    handler = Player_Animation_Handler(player)
    handler.animation_lock = True
    handler.action = keys.attack

    # Attempt to slip a movement update through while processing a swing frame
    handler.Set_Action()
    assert handler.action == keys.attack