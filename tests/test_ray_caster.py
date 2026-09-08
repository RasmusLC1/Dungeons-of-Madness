import pytest
from unittest.mock import MagicMock, call
import pygame
from scripts.engine.ray_caster import Ray_Caster, DEFAULT_ACTIVITY

# --- Fixtures ---

@pytest.fixture
def mock_game():
    """Sets up a complex mock structure mirroring the game context."""
    game = MagicMock()
    
    # Mock player structure
    game.player.pos = (0, 0)
    game.player.tile.pos = (10, 10)
    
    # Mock tilemap structure
    game.tilemap = MagicMock()
    game.render_scale = 1.0
    return game

@pytest.fixture
def mock_tile():
    """Helper to generate a tile with standard defaults."""
    tile = MagicMock()
    tile.active = DEFAULT_ACTIVITY
    tile.scaled_pos = (0, 0)
    tile.pos = (5, 5)
    tile.translucent = False
    return tile


# --- Test Suite ---

## Initialization Tests
def test_ray_vectors_generation(mock_game):
    """Ensure vectors are initialized cleanly and cover a spread."""
    raycaster = Ray_Caster(mock_game)
    
    assert len(raycaster.ray_vectors) == 100
    
    # The first and last vectors should match symmetrically across the x-axis
    first_vec = raycaster.ray_vectors[0]
    last_vec = raycaster.ray_vectors[-1]
    assert abs(first_vec[0] - last_vec[0]) < 1e-5
    assert abs(first_vec[1] - (-last_vec[1])) < 1e-5


## Data Saving & Loading Tests
def test_save_data(mock_game, mock_tile):
    """Verify that current tile positions are mapped and indexed correctly."""
    raycaster = Ray_Caster(mock_game)
    raycaster.tiles = [mock_tile]
    
    mock_game.tilemap.Convert_Tile_Pos_To_Key.return_value = "5,5"
    
    raycaster.Save_Data()
    
    mock_game.tilemap.Convert_Tile_Pos_To_Key.assert_called_once_with((5, 5))
    assert raycaster.saved_data == {"5,5": (5, 5)}

def test_load_data_success(mock_game, mock_tile):
    """Verify loading restores existing tiles into the engine array."""
    raycaster = Ray_Caster(mock_game)
    mock_game.tilemap.Get_Tile.return_value = mock_tile
    
    saved_payload = {"5,5": [5, 5]}
    raycaster.Load_Data(saved_payload)
    
    mock_game.tilemap.Get_Tile.assert_called_with((5, 5))
    assert mock_tile in raycaster.tiles

def test_load_data_missing_tile(mock_game, capsys):
    """Ensure standard graceful stdout logs if saved layout tiles go missing."""
    raycaster = Ray_Caster(mock_game)
    mock_game.tilemap.Get_Tile.return_value = None
    
    raycaster.Load_Data({"9,9": [9, 9]})
    
    captured = capsys.readouterr()
    assert "RAYCASTER TILE NOT FOUND AT (9, 9)" in captured.out
    assert len(raycaster.tiles) == 0


## Tile Activity & Update Filtering Tests
def test_process_tile_activity_in_range(mock_game, mock_tile):
    """Tiles within active range should decrement activity counters and stay active."""
    raycaster = Ray_Caster(mock_game)
    mock_tile.active = 10
    mock_tile.scaled_pos = (100, 100) # Distance squared = 20,000 (< 640,000)
    
    is_active = raycaster._process_tile_activity(mock_tile, (0, 0))
    
    assert is_active is True
    assert mock_tile.active == 9

def test_process_tile_activity_out_of_range(mock_game, mock_tile):
    """Tiles beyond safe ranges must flatten counters and trigger an inactivation state."""
    raycaster = Ray_Caster(mock_game)
    mock_tile.active = 10
    mock_tile.scaled_pos = (2000, 2000) # Distance squared = 8,000,000 (> 640,000)
    
    is_active = raycaster._process_tile_activity(mock_tile, (0, 0))
    
    assert is_active is False
    assert mock_tile.active == 0

def test_check_tile_active_filters_list(mock_game):
    """Ensure Check_Tile_Active purges dead nodes entirely from the tracker array."""
    raycaster = Ray_Caster(mock_game)
    mock_game.player.pos = (0, 0)
    
    tile1 = MagicMock(active=5, scaled_pos=(0, 0))
    tile2 = MagicMock(active=5, scaled_pos=(2000, 2000)) # Far tile
    raycaster.tiles = [tile1, tile2]
    
    raycaster.Check_Tile_Active()
    
    assert tile1 in raycaster.tiles
    assert tile2 not in raycaster.tiles
    assert len(raycaster.tiles) == 1

def test_update_ticks_entities(mock_game, mock_tile):
    """Verify update loop steps execute both filter tasks and entity frame ticks."""
    raycaster = Ray_Caster(mock_game)
    raycaster.tiles = [mock_tile]
    
    # Stub Check_Tile_Active to keep mock_tile in place
    raycaster.Check_Tile_Active = MagicMock()
    
    raycaster.Update(16.6)
    
    raycaster.Check_Tile_Active.assert_called_once()
    mock_tile.Set_Entity_Active.assert_called_once_with(16.6)


## Tile Life cycle Management Tests
def test_remove_tile_pipeline(mock_game, mock_tile):
    """Ensure forced tile purging clears its presence safely and sets activity to zero."""
    raycaster = Ray_Caster(mock_game)
    raycaster.tiles = [mock_tile]
    
    raycaster.Remove_Tile(mock_tile)
    
    assert mock_tile.active == 0
    assert mock_tile not in raycaster.tiles

def test_check_tile_already_active(mock_game, mock_tile):
    """Refreshing an active tile should simply extend its longevity window."""
    raycaster = Ray_Caster(mock_game)
    mock_game.tilemap.Current_Tile.return_value = mock_tile
    mock_tile.active = 50
    mock_tile.translucent = True
    
    is_translucent = raycaster.Check_Tile((2, 2))
    
    mock_tile.Set_Active.assert_called_once_with(DEFAULT_ACTIVITY)
    assert is_translucent is True

def test_check_tile_inactive_triggers_addition(mock_game, mock_tile):
    """Checking a dead or inactive tile pushes structural creation routines."""
    raycaster = Ray_Caster(mock_game)
    mock_game.tilemap.Current_Tile.return_value = mock_tile
    mock_tile.active = 0
    
    raycaster.Add_Tile = MagicMock()
    raycaster.Check_Tile((2, 2))
    
    raycaster.Add_Tile.assert_called_once_with(mock_game.tilemap, mock_tile)

def test_clear_entity_from_tiles(mock_game, mock_tile):
    """Verify entity tracking lists broadcast eviction IDs down to all tiles."""
    raycaster = Ray_Caster(mock_game)
    raycaster.tiles = [mock_tile]
    
    raycaster.Clear_Entity_From_Tiles("enemy_42")
    mock_tile.Remove_Entity.assert_called_once_with("enemy_42")


## Engine Core Raycasting Loop Tests
def test_ray_caster_loop_execution(mock_game):
    """Verify that raycasting loops probe tiles outwards up to maximum scaling limits."""
    raycaster = Ray_Caster(mock_game)
    mock_game.player.tile.pos = (10, 10)
    mock_game.render_scale = 1.0  # max_steps = 8
    
    # Overwrite ray_vectors to track simple directional outputs
    raycaster.ray_vectors = [(1.0, 0.0)] # Single ray pointing right
    
    # Return True (translucent) so the ray doesn't break early
    raycaster.Check_Tile = MagicMock(return_value=True)
    
    raycaster.Ray_Caster()
    
    # First call checks player origin
    raycaster.Check_Tile.assert_any_call((10, 10))
    
    # Check steps 1 through 7 along the vector (max_steps is 8, range(1, 8))
    expected_calls = [call((10, 10))] + [call((10 + float(i), 10.0)) for i in range(1, 8)]
    raycaster.Check_Tile.assert_has_calls(expected_calls)

def test_ray_caster_breaks_on_solid_tile(mock_game):
    """Rays must halt and cease further linear exploration when hitting opaque geometry."""
    raycaster = Ray_Caster(mock_game)
    mock_game.player.tile.pos = (10, 10)
    mock_game.render_scale = 1.0 
    raycaster.ray_vectors = [(1.0, 0.0)]
    
    # Ray caster hits an opaque wall at step 1 and returns False
    raycaster.Check_Tile = MagicMock(side_effect=lambda pos: True if pos == (10, 10) else False)
    
    raycaster.Ray_Caster()
    
    # Should check origin and the first step, then break immediately
    assert raycaster.Check_Tile.call_count == 2


## Utilities
def test_rect_utility():
    """Assert convenience mapping generates an accurate Pygame primitive bounding box."""
    raycaster = Ray_Caster(MagicMock())
    pos = (15, 25)
    rect = raycaster.rect(pos)
    assert isinstance(rect, pygame.Rect)
    assert rect.topleft == raycaster.rect_handler.Calculate_Rect_Pos(pos)
    assert rect.size == (10, 10)