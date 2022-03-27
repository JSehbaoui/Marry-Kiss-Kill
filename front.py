# "MFK in a GUI" by Julian Sehbaoui
# started working on 07/17/21

#importing all the nessessary libaries
import pygame
import json
import random

#Importing other relavant classes
from panel import Tile
from main import Player

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

# font
font = pygame.font.Font(None, 40)

#opening the json file and loading all packages
with open("presets.json") as f:
    packages = json.load(f)

#getting all characters from the chosen packages into one list
chosen_packages = ["Anime_Female"]
characters = []
for package in chosen_packages:
    characters.extend(packages[package])

#replacing the raw names with objects of the class Player
for i in range(len(characters)):
    characters[i] = Player(name = characters[i])

# mainloop-boolean
go = True
turn_ended = False

#creating window#
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
window.fill(grass_green)
clock = pygame.time.Clock()

#Surfaceproperties
top_surface_properties = (WIDTH, HEIGHT*(1/5))
tile_size = (WIDTH*(1/3), HEIGHT*(4/5))
left_surface_properties = tile_size
middle_surface_properties = tile_size
right_surface_properties = tile_size

#CREATING THE SURFACE FOR CONTENTS
surface = pygame.Surface((WIDTH, HEIGHT))

#creating subsurfaces
top_surface = pygame.Surface(top_surface_properties)
left_surface = pygame.Surface(left_surface_properties)
middle_surface = pygame.Surface(middle_surface_properties)
right_surface = pygame.Surface(right_surface_properties)

#creating a list with all subsurfaces
subsurfaces = [top_surface, left_surface, middle_surface, right_surface]

#creating the labels for "Marry", "Fuck" and "Kill"
labels = [font.render("Marry", True, black), font.render("Fuck", True, black), font.render("Kill", True, black)]

while go:

    #loading 3 random entries from the list
    victims = random.sample(characters, k = 3)

    #creating three tiles with anyone representing one of the chosen entries 
    tile_left   = Tile(master = left_surface, x = 0, y = 0, w = tile_size[0], h = tile_size[1],
        color_t = (255, 255, 255), command = lambda:[print("Hello World!")], name = victims[0].getName(), anchor_point_y=HEIGHT*(1/5))
    tile_middle = Tile(master = middle_surface, x = 0, y = 0, w = tile_size[0], h = tile_size[1],
        color_t = (255, 255, 255), command = lambda:[print("Hello World!")], name = victims[1].getName(), anchor_point_x=WIDTH*(1/3), anchor_point_y=HEIGHT*(1/5))
    tile_right  = Tile(master = right_surface, x = 0, y = 0, w = tile_size[0], h = tile_size[1],
        color_t = (255, 255, 255), command = lambda:[print("Hello World!")], name = victims[2].getName(), anchor_point_x=WIDTH*(2/3), anchor_point_y=HEIGHT*(1/5))
    all_tiles = [tile_left, tile_middle, tile_right]

    #starting the window
    while not turn_ended:

        # frames per second
        clock.tick(tick)

        #resetting the surface
        surface.fill(grass_green)
        top_surface.fill(grass_green)

        #drawing all tiles
        for tile in all_tiles:
            tile.draw()

        #drawing labels
        fuck_label_prop_w = labels[1].get_rect()[0]
        for label in labels:
            top_surface.blit(label, ((fuck_label_prop_w+WIDTH)*(1/2)-300+labels.index(label)*300, 50))
        
        #checking for events
        for event in pygame.event.get():
            for tile in all_tiles:
                tile.processEvent(event)

            #is there for quitting
            if event.type == pygame.QUIT:
                go = False
                turn_ended = True
                
            # Keyboard Inputs
            if event.type == pygame.KEYDOWN:

                # closing the window if "ESC" is pressed
                if event.key == pygame.K_ESCAPE:
                    quit()
        
        #blitting the subserfaces on the main surface
        surface.blit(top_surface, (0,0))
        surface.blit(left_surface, (0,HEIGHT*(1/5)))
        surface.blit(middle_surface, (WIDTH*(1/3),HEIGHT*(1/5)))
        surface.blit(right_surface, (WIDTH*(2/3),HEIGHT*(1/5)))

        #blitting the main surface on the window
        window.blit(surface, (0,0))

        #refreshing the window
        pygame.display.flip()

print("completed code")