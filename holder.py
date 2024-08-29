import pygame

pygame.font.init()

# Global font variable
font = pygame.font.Font(None, 20)

class Inventory_Slot():
    global font
    font=pygame.font.Font(None,20)
    def __init__(self, game, pos, size, item):
        self.game = game
        self.pos = pos
        self.size = size
        self.item = item
        self.background = None
        self.inventory_type = None
        Inventory_Slot.Setup_Inventory_Texture(self)
        self.active = False
        self.activate_counter = 0
        
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
        if self.item.used:
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
        surf.blit(self.box_surface, self.pos)
        pygame.draw.rect(surf, black, self.rect(), 1)
        if self.background and not self.item:
            background_image = pygame.transform.scale(self.background, (17,17))  
            surf.blit(background_image, self.pos)

        surf.blit(font.render("3",True,(0,0,0)), self.pos)
        if self.item and not self.active:
            self.item.Render(surf)
        else:
            return
        
        if not self.item.amount > 1:
            return
