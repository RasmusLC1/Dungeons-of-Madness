import pygame
import pygame.freetype

class Inventory_Slot():
    def __init__(self, game, pos, size, item):
        self.game = game
        self.pos = pos
        self.size = size
        self.item = item
        self.background = None
        self.inventory_type = None
        self.Setup_Inventory_Texture()
        self.active = False
        self.activate_counter = 0
        
        try:
            self.background_font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
            self.background_font = pygame.font.SysFont('freesans', 10)  # Fallback font


    def Setup_Inventory_Texture(self):
        light_grey = (211, 211, 211)
        self.box_surface = pygame.Surface(self.size)
        self.box_surface.fill(light_grey)
        self.box_surface.set_alpha(179)

    def Set_Active(self, status):
        self.active = status

    def Reset_Inventory_Slot(self):
        self.item = None
        self.active = False
        self.activate_counter = 0

    def Update(self):
        if self.active:
            self.activate_counter += 1
            return
        if self.item and self.item.used:
            self.item = None
        return

    def Add_Item(self, item):
        item.active = True
        self.item = item
        self.item.Move((self.pos[0] + 3, self.pos[1] + 3))
        if self.inventory_type:
            self.item.Set_Inventory_Type(self.inventory_type)
        else:
            self.item.Set_Inventory_Type(None)

    def Remove_Item(self):
        self.item = None

    def Add_Background(self, background):
        self.background = background

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Render(self, surf):
        black = (0, 0, 0)

        # Render the box surface with scaling
        scaled_box_surface = pygame.transform.scale(self.box_surface, (self.size[0], self.size[1]))
        surf.blit(scaled_box_surface, self.pos)
        pygame.draw.rect(surf, black, self.rect(), 1)

        if self.background and not self.item:
            background_image = pygame.transform.scale(self.background, (17, 17))
            surf.blit(background_image, self.pos)

        

        if self.item and not self.active:
            self.item.Render(surf)
        else:
            return

        if not self.item.amount > 1:
            return

        # Render text at base resolution
        text_surface = self.background_font.render(self.item.amount, True, (255, 255, 255))

        
        # Calculate the position for the text
        text_pos = (self.pos[0] + 10, self.pos[1] + 8)

        # Blit the text surface onto the screen
        surf.blit(text_surface, text_pos)