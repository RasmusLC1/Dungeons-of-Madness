import logging

import pytest
from unittest.mock import MagicMock, patch
import pygame
from collections import deque

# Adjust imports to point to your actual engine directory structure
from scripts.entities.entity.entities import PhysicsEntity
from scripts.entities.entity.tile_handler import Tile_Handler
from scripts.engine.keys.keys import keys

@pytest.fixture(scope="session", autouse=True)
def headless_pygame_context():
    """Initializes a headless video environment to support test-driven Surface manipulation."""
    import os
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.quit()

@pytest.fixture(autouse=True)
def reset_entity_id_counters():
    """Resets class-level tracking states between isolated tests to guarantee predictable IDs."""
    PhysicsEntity._id_counter = 0
    PhysicsEntity._available_IDs = deque()
    yield

@pytest.fixture
def mock_game():
    """Generates a complete mock game context with pre-wired Tilemap dependencies."""
    game = MagicMock()
    game.tilemap.tile_size = 32
    
    # Setup mock tile nodes
    mock_tile = MagicMock()
    mock_tile.pos = (0, 0)
    mock_tile.light_level = 5
    mock_tile.scaled_pos = (0, 0)
    
    game.tilemap.Current_Tile.return_value = mock_tile
    game.tilemap.Get_Random_Tile_With_Path_To_Player.return_value = mock_tile
    return game



### 1. Identity Lifecycle & Recycling Tests

def test_entity_id_generation_and_recycling(mock_game):
    """Verifies incremental allocation and proper stack recycling of entity IDs via Delete()."""
    entity_a = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity_b = PhysicsEntity(mock_game, "goblin", "monster", (32, 0), (32, 32))
    
    assert entity_a.ID == 0
    assert entity_b.ID == 1
    
    # Delete first entity to queue its ID for reclamation
    entity_a.Delete()
    assert 0 in PhysicsEntity._available_IDs
    
    # Next instantiation should pull from recycled pool rather than incrementing counter
    entity_c = PhysicsEntity(mock_game, "spider", "monster", (64, 0), (32, 32))
    assert entity_c.ID == 0



### 2. Component Logic and Spatial Registration Tests

def test_tile_handler_registration_on_init(mock_game):
    """Ensures initialization successfully executes components to bind spatial map links."""
    mock_tile = MagicMock()
    mock_tile.pos = (1, 2)
    mock_game.tilemap.Current_Tile.return_value = mock_tile

    # Positioning at coordinates (32, 64) over a 32px grid matches key index (1, 2)
    entity = PhysicsEntity(mock_game, "kobold", "monster", (32, 64), (32, 32))
    
    assert entity.tile == mock_tile
    mock_game.tilemap.Add_Entity_To_Tile.assert_called_with(mock_tile, entity)

def test_tile_handler_crosses_boundaries(mock_game):
    """Validates that modifying entity positions re-allocates active tiles across update steps."""
    tile_start = MagicMock(pos=(0, 0))
    tile_destination = MagicMock(pos=(1, 0))
    
    # Orchestrate safe multi-stage tile handoffs
    mock_game.tilemap.Current_Tile.side_effect = [tile_start, tile_destination]
    
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    assert entity.tile == tile_start
    
    # Walk right into adjacent tile coordinate workspace boundaries
    entity.pos = pygame.Vector2(32, 0)
    
    # Trigger spatial refresh block (Must bypass initial cooldown delay)
    has_changed = entity.Update_Tile(delta_time=0.2)
    
    assert has_changed is True
    assert entity.tile == tile_destination
    tile_start.Remove_Entity.assert_called_once_with(entity.ID)



### 3. State Management & Light Calculation Tests

def test_light_level_clamping(mock_game):
    """Guarantees illumination thresholds clamp perfectly within array bounds."""
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    
    # Test maximum values clamp to byte max limit (255)
    entity.Set_Light_Level(500)
    assert entity.light_level == 255
    assert entity.render_needs_update is True
    
    # Test minimal bounds fallback to structural minimums
    entity.Set_Light_Level(10)
    assert entity.light_level == entity.min_light_level

def test_light_level_interpolation_steps(mock_game):
    """Checks that entity lighting interpolates incrementally toward ambient tile values."""
    mock_tile = MagicMock()
    mock_tile.light_level = 2 # Target light = 2 * LIGHT_ALPHA_SCALE (30) = 60
    mock_game.tilemap.Current_Tile.return_value = mock_tile
    
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity.light_level = 40 # Set default flat floor baseline
    
    # Execute single tick of lighting updates
    entity.Update_Light_Level()
    assert entity.light_level == 45
    assert entity.render_needs_update is True



### 4. Serialization Integrity Tests

def test_entity_serialization_loop(mock_game):
    """Ensures structural metrics store and restore cleanly across save/load state routines."""
    entity = PhysicsEntity(mock_game, "kobold", "monster", (10, 20), (16, 24))
    entity.ID = 77
    entity.light_level = 120
    entity.active = 50
    
    serialized_dump = entity.Save_Data()
    
    # Spawn completely un-configured object frame
    blank_entity = PhysicsEntity(mock_game, "placeholder", "temp", (0, 0), (32, 32))
    blank_entity.Load_Data(serialized_dump)
    
    assert blank_entity.ID == 77
    assert blank_entity.category == "monster"
    assert blank_entity.type == "kobold"
    assert blank_entity.pos == pygame.Vector2(10, 20)
    assert blank_entity.size == [16, 24]
    assert blank_entity.active == 50
    assert blank_entity.light_level == 120
    
    # Ensure ID allocation updates system counters safely to avoid overlapping IDs
    assert PhysicsEntity._id_counter == 78



### 5. Animation Handler Property Delegation Tests

def test_min_animation_property_delegates_correctly(mock_game):
    """
    Regression test: min_animation must forward to animation_handler.min_animation,
    not animation_handler.animation_max. These are backward-compat convenience
    properties (entity.min_animation instead of entity.animation_handler.min_animation),
    so returning the wrong underlying attribute silently corrupts anything that
    reads entity.min_animation.
    """
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32),
                            max_animation=4, animation_cooldown_max=0.2)

    # Sanity: the two underlying values must differ for this test to mean anything
    entity.animation_handler.min_animation = 1
    entity.animation_handler.animation_max = 4
    assert entity.animation_handler.min_animation != entity.animation_handler.animation_max

    assert entity.min_animation == entity.animation_handler.min_animation
    assert entity.max_animation == entity.animation_handler.animation_max

def test_min_animation_property_setter_writes_through(mock_game):
    """Setting entity.min_animation should mutate the handler, not shadow it locally."""
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32),
                            max_animation=4, animation_cooldown_max=0.2)

    entity.min_animation = 2
    assert entity.animation_handler.min_animation == 2



### 6. Render Pipeline Tests

def test_render_blits_existing_cached_image(mock_game):
    """When rendered_image is already cached and light checks pass, Render should blit directly."""
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity.active = 255
    entity.entity_image = MagicMock(spec=pygame.Surface)
    entity.render_needs_update = True

    # Isolate Render()'s own logic from Tile_Handler's separate light-ramp
    # behavior (light_level climbs by 5/tick and starts below min_light_level).
    with patch.object(entity, "Update_Light_Level", return_value=True):
        surf = MagicMock()
        entity.Render(surf, offset=(0, 0))

    surf.blit.assert_called_once()
    blitted_image, blitted_pos = surf.blit.call_args[0]
    assert blitted_image is entity.rendered_image
    assert blitted_pos == (entity.pos[0], entity.pos[1])

def test_render_reloads_sprite_when_entity_image_missing(mock_game):
    """
    If entity_image is None (e.g. never set), Render should attempt Set_Sprite()
    once, then produce a lit rendered_image and blit it in the same frame rather
    than falling back to a raw unlit image and skipping the blit.
    """
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity.active = 255
    assert entity.entity_image is None

    # mock_game.assets[key] and sprite[frame].convert_alpha() resolve automatically
    # via MagicMock, simulating a successful late sprite load.
    with patch.object(entity, "Update_Light_Level", return_value=True):
        surf = MagicMock()
        entity.Render(surf, offset=(0, 0))

    assert entity.entity_image is not None
    surf.blit.assert_called_once()
    blitted_image, _ = surf.blit.call_args[0]
    assert blitted_image is entity.rendered_image

def test_render_skips_blit_and_warns_when_no_image_available(mock_game, caplog):
    """
    If entity_image is still missing after the reload attempt (e.g. asset lookup
    genuinely fails), Render should not blit anything and should log a warning
    instead of silently rendering a stale/blank frame.
    """
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity.active = 255

    # Force the reload attempt to fail regardless of mock_game's auto-mocking,
    # and isolate from the light-ramp behavior as above.
    with patch.object(entity, "Update_Light_Level", return_value=True), \
         patch.object(entity.animation_handler, "Set_Sprite", return_value=False), \
         patch.object(entity.animation_handler, "Set_Entity_Image", lambda: None):
        surf = MagicMock()
        with caplog.at_level(logging.WARNING):
            entity.Render(surf, offset=(0, 0))

    surf.blit.assert_not_called()
    assert any("kobold" in record.message for record in caplog.records)

def test_render_skips_when_light_level_too_low(mock_game):
    """Render should bail out before any blit attempt if Update_Light_Level reports darkness."""
    entity = PhysicsEntity(mock_game, "kobold", "monster", (0, 0), (32, 32))
    entity.entity_image = MagicMock(spec=pygame.Surface)

    with patch.object(entity, "Update_Light_Level", return_value=False):
        surf = MagicMock()
        entity.Render(surf, offset=(0, 0))

    surf.blit.assert_not_called()