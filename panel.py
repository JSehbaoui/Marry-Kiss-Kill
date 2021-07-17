import requests
import pygame
pygame.init()

class Tile:

    all_tiles = []

    def __init__(self, master, x, y, w, h, color_t, command, font_size = 20, font = None, name = 'Unknown', anime = 'Unknown',anchor_point_x = 0, anchor_point_y = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.button_rect = pygame.Rect(x, y, w, h)
        self.master = master
        self.surface = master
        self.color_t = color_t
        self.name = name
        self.anime = anime
        self.font = pygame.font.Font(font, font_size)
        self.command = command
        self.anch_x = anchor_point_x
        self.anch_y = anchor_point_y

        self.picture = None
        Tile.all_tiles.append(self)


    def draw(self):
        color = (0,0,0)

        pygame.draw.rect(self.master, color , self.button_rect)
        
        label = self.font.render(self.name, True, self.color_t)
        label_rect = label.get_rect()
        self.master.blit(label, (self.x + self.w/2 - label_rect.w/2, self.y + self.h/2 - label_rect.h/2))

    def processEvent(self, event):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = mouse_pos[0]-self.anch_x, mouse_pos[1]-self.anch_y

        if self.button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.command()
        
    def check_for_animation(self, screen, bg_color, corner_size):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = mouse_pos[0]-self.anch_x, mouse_pos[1]-self.anch_y
        if self.button_rect.collidepoint(mouse_pos):
            self.hover_animation(screen=screen, bg_color=bg_color, corner_size=corner_size)
        

    def hover_animation(self, screen):
        pass

    def getimage(self):
        pass

if __name__ == "__main__":
    #Properties#
    WIDTH = 1280
    HEIGHT = 720
    tick = 60

    #Initiating pygame#
    pygame.init()

    # colors
    black = (0, 0, 0)
    grass_green = (81, 128, 45)
    crimson_red = (153, 32, 23)

    # mainloop-boolean
    go = True

    #creating window#
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
    window.fill(grass_green)
    clock = pygame.time.Clock()

    #CREATING THE SURFACE FOR CONTENTS
    surface = pygame.Surface((WIDTH, HEIGHT))

    test = Tile(master = surface, x = 0, y = 0, w = 100, h = 300, color_t = (255,255,255),
                command = lambda:[print("Hello World!")], name = "Dabi", anime="Boko No Hero Akademia")

    while go:
        # frames per second
        clock.tick(tick)

        # drawing all tiles
        surface.fill(grass_green)

        # drawing Tile
        test.draw()



        #checking for events
        for event in pygame.event.get():

            test.processEvent(event)

            #is there for quitting
            if event.type == pygame.QUIT:
                    go = False
                
            # Keyboard Inputs
            if event.type == pygame.KEYDOWN:

                # closing the window if "ESC" is pressed
                if event.key == pygame.K_ESCAPE:
                    quit()
        
        window.blit(surface, (0,0))

        #refreshing the window
        pygame.display.flip()
                