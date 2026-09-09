from scripts.entities.decoration.shared.shrine.shrine import Menu_Shrine
from scripts.engine.keys.keys import keys
from scripts.entities.decoration.shared.shared_registry import Register_Decoration
from scripts.entities.decoration.shared.shrine.shrine_registry import Register_Shrine


Register_Shrine(keys.portal_shrine)
@Register_Decoration(keys.portal_shrine)
class Portal_Shrine(Menu_Shrine):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.portal_shrine, pos, (64, 64), cycle_requires_open=True, max_animation=3)
        self.available_rune = None  # appears unused past storage — flag if dead
        self.animation_handler.Set_Static_Animation(0) # Initialise without animation

    def Remove_Available_Rune(self):
        self.available_rune = None

    def Open(self):
        if not self.is_open:
            self.game.menu_handler.portal_shrine_menu.Initialise_Shrine(self)
            self.game.clatter.Generate_Clatter(self.pos, 400)
        self.Activate_Shrine()
        self.game.state_machine.Set_State('portal_shrine_menu')

    def Activate(self):
        self.light_level = 5
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.min_animation = 1
        self.is_open = True