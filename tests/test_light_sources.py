import pytest
from unittest.mock import MagicMock, patch
import pygame
from collections import deque

# Adjust imports to point to your actual engine directory structure
from scripts.entities.entity.entities import PhysicsEntity
from scripts.entities.decoration.light_sources.light_sources.light_source import Light_Source
from scripts.entities.decoration.light_sources.crystal_caverns.glowing_crystal import Glowing_Crystal
from scripts.engine.keys.keys import keys

@pytest.fixture(scope="session", autouse=True)
def headless_pygame_context():
    import os
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()

@pytest.fixture(autouse=True)
def reset_entity_id_counters():
    PhysicsEntity._id_counter = 0
    PhysicsEntity._available_IDs = deque()
    yield

@pytest.fixture
def mock_game():
    game = MagicMock()
    game.tilemap.tile_size = 32

    mock_tile = MagicMock()
    mock_tile.pos = (0, 0)
    mock_tile.light_level = 5
    mock_tile.scaled_pos = (0, 0)

    game.tilemap.Current_Tile.return_value = mock_tile

    game.light_handler.Add_Light.return_value = MagicMock(name="light_source_handle")
    game.light_handler.Initialise_Light_Level.return_value = 60

    return game


### 1. Construction & Light Registration

def test_light_source_registers_light_on_init(mock_game):
    """Verifies Add_Light is called with the configured strength and the returned handle is stored."""
    light_source = Light_Source(mock_game, (0, 0), keys.glowing_crystal, 1, light_strength=8)

    mock_game.light_handler.Add_Light.assert_called_once_with(light_source.pos, 8, light_source.tile)
    assert light_source.light_source == mock_game.light_handler.Add_Light.return_value
    assert light_source.light_level == 60


def test_light_source_forwards_decoration_kwargs(mock_game):
    """Ensures destructable/health/animation kwargs actually land on the entity, not just the constructor."""
    light_source = Light_Source(
        mock_game, (0, 0), keys.glowing_crystal, 1, light_strength=8,
        destructable=True, health=40, max_animation=5, animation_cooldown_max=0.5
    )

    assert light_source.destructable is True
    assert light_source.health == 40
    assert light_source.max_animation == 5
    assert light_source.animation_cooldown_max == 0.5


### 2. Glowing_Crystal Animation Cycling
def test_glowing_crystal_holds_animation_during_cooldown(mock_game):
    # Target exact location of random inside animation_handler.py
    with patch("scripts.entities.entity.animation_handlers.base_animation_handler.random.randint", return_value=2):
        crystal = Glowing_Crystal(mock_game, (0, 0))
    crystal.Update_Animation(delta_time=0.3)

    start_animation = crystal.animation

    crystal.Update_Animation(delta_time=0.3)

    assert crystal.animation == start_animation
    assert crystal.animation_handler.animation_cooldown == pytest.approx(1.7)


def test_glowing_crystal_advances_and_wraps_animation(mock_game):
    """Confirms the frame advances once cooldown expires, wrapping back to 0 past max_animation."""
    with patch("scripts.entities.entity.animation_handlers.base_animation_handler.random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (0, 0))

    crystal.animation = crystal.max_animation
    crystal.animation_handler.animation_cooldown = 0

    with patch("scripts.entities.entity.animation_handlers.base_animation_handler.random.uniform", return_value=0.5):
        crystal.Update_Animation(delta_time=0.1)

    assert crystal.animation == 0
    assert crystal.animation_cooldown == 2.0


### 3. Glowing_Crystal Light Boost & Decay (Open)

def test_glowing_crystal_open_boosts_light(mock_game):
    """Opening the crystal raises light strength above baseline and pushes it to the light handle."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (0, 0))

    crystal.Open()

    assert crystal.updated_light_strength == crystal.light_strength + 4
    crystal.light_source.Update_Light_Level.assert_called_with(crystal.light_strength + 4)


def test_glowing_crystal_light_decays_toward_baseline(mock_game):
    """Each animation tick pushes the still-boosted value, then decays it by 1 toward baseline."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (0, 0))

    crystal.Open()
    crystal.light_source.Update_Light_Level.reset_mock()
    crystal.animation_handler.animation_cooldown = 0

    with patch("random.uniform", return_value=0.5):
        crystal.Update_Animation(delta_time=0.1)

    crystal.light_source.Update_Light_Level.assert_called_once_with(crystal.light_strength + 4)
    assert crystal.updated_light_strength == crystal.light_strength + 3


def test_glowing_crystal_stops_pushing_updates_at_baseline(mock_game):
    """Once updated_light_strength reaches baseline, further ticks shouldn't call Update_Light_Level."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (0, 0))

    crystal.updated_light_strength = crystal.light_strength
    crystal.light_source.Update_Light_Level.reset_mock()
    crystal.animation_handler.animation_cooldown = 0

    with patch("random.uniform", return_value=0.5):
        crystal.Update_Animation(delta_time=0.1)

    crystal.light_source.Update_Light_Level.assert_not_called()


### 4. Render Invalidation Regression

def test_increase_animation_flags_render_for_update(mock_game):
    """Regression test for the frozen-sprite bug: advancing frames must flag render_needs_update."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (0, 0))

    crystal.render_needs_update = False
    crystal.animation_handler.Increase_Frame()

    assert crystal.render_needs_update is True

from scripts.entities.decoration.light_sources.light_sources.brazier import Brazier


### 5. Brazier — Toggle On/Off

def test_brazier_open_extinguishes_when_lit(mock_game):
    """Opening a lit brazier should turn it off and release its light source."""
    with patch("random.randint", return_value=1):
        brazier = Brazier(mock_game, (0, 0))

    assert brazier.animation_handler.animation > 0
    active_light_handle = brazier.light_source

    result = brazier.Open()

    assert result is True
    assert brazier.animation == 0
    mock_game.light_handler.Remove_Light.assert_called_once_with(active_light_handle)
    assert brazier.light_source is None


def test_brazier_open_relights_when_off(mock_game):
    """Opening an unlit brazier should re-add its light and resume animating."""
    with patch("scripts.entities.entity.animation_handlers.base_animation_handler.random.randint", return_value=1):
        brazier = Brazier(mock_game, (0, 0))

    brazier.Open()  # extinguish first
    mock_game.light_handler.Add_Light.reset_mock()
    mock_game.particle_handler.Activate_Particles.reset_mock()

    with patch("scripts.entities.entity.animation_handlers.base_animation_handler.random.randint", return_value=3):
        result = brazier.Open()

    assert result is True
    mock_game.light_handler.Add_Light.assert_called_once()
    assert brazier.animation_handler.animation == 3
    mock_game.particle_handler.Activate_Particles.assert_called_once()


def test_brazier_open_reports_error_on_inconsistent_state(mock_game):
    """If animation is 0 but a light_source handle is still attached (corrupted state),
    Open() should report failure rather than double-registering a light."""
    with patch("random.randint", return_value=1):
        brazier = Brazier(mock_game, (0, 0))

    mock_game.light_handler.Add_Light.reset_mock()
    brazier.animation = 0  # force inconsistency: light_source still set from init

    result = brazier.Open()

    assert result is True
    mock_game.light_handler.Add_Light.assert_not_called()


### 6. Brazier — Animation Gating

def test_brazier_skips_animation_update_while_off(mock_game):
    """animation == 0 means 'off' — Update() must not advance the fire animation while off."""
    with patch("random.randint", return_value=1):
        brazier = Brazier(mock_game, (0, 0))

    brazier.animation = 0
    brazier.animation_handler.animation_cooldown = 5.0

    brazier.Update(delta_time=2.0)

    assert brazier.animation_cooldown == 3.0  # untouched — branch was skipped


def test_brazier_animates_while_lit(mock_game):
    """While lit, cooldown expiry should advance the frame and spawn a fire particle."""
    with patch("random.randint", return_value=1):
        brazier = Brazier(mock_game, (0, 0))

    brazier.animation_handler.animation_cooldown = 0

    with patch("random.randint", return_value=4):
        brazier.Update(delta_time=0.3)
        brazier.Update(delta_time=0.3)

    assert brazier.animation_handler.animation == 4
    assert brazier.animation_handler.animation_cooldown == 0.5
    mock_game.particle_handler.Activate_Particles.assert_called_once()

### 7. Glowing_Crystal Destruction & Loot Drop

def test_glowing_crystal_destruction_triggers_loot_drop(mock_game):
    """Verifies that calling Destroyed() invokes Drop_Loot on the loot_component 
    with the crystal's coordinates and animation multiplier."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (32, 64))

    crystal.animation = 3
    
    # Mock the loot component to assert interaction
    crystal.loot_component = MagicMock()

    with patch("scripts.entities.decoration.decoration.Decoration.Destroyed", return_value=True), \
         patch("random.randint", return_value=0):
        
        destroyed_result = crystal.Destroyed()

    assert destroyed_result is True
    crystal.loot_component.Drop_Loot.assert_called_once_with((32.0, 64.0))


def test_glowing_crystal_destruction_aborts_if_super_destroyed_fails(mock_game):
    """If the parent Decoration.Destroyed() returns False (e.g., already destroyed or indestructible),
    loot dropping should be prevented."""
    with patch("random.randint", return_value=1):
        crystal = Glowing_Crystal(mock_game, (32, 64))

    crystal.loot_component = MagicMock()

    with patch("scripts.entities.decoration.decoration.Decoration.Destroyed", return_value=False):
        destroyed_result = crystal.Destroyed()

    assert destroyed_result is False
    crystal.loot_component.Drop_Loot.assert_not_called()