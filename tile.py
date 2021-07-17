import pygame
import math
pygame.init()

class Polygon:
    def __init__(self, angle, size, color, pos) -> None:
        self.angle = angle
        self.size = size
        self.color = color

        kante = size*0.35

        point1 = pos
        point2 = (math.sin(math.radians(angle))*size + point1[0], math.cos(math.radians(angle))*size + point1[1])
        point3 = (math.sin(math.radians(angle+90))*size + point1[0], math.cos(math.radians(angle+90))*size + point1[1])
        point4 = (math.sin(math.radians(angle+90))*kante+point2[0], math.cos(math.radians(angle+90))*kante+point2[1])
        point5 = (math.sin(math.radians(angle))*kante+point3[0], math.cos(math.radians(angle))*kante+point3[1])
        point6 = (math.sin(math.radians(angle+180))*(size-kante)+point4[0], math.cos(math.radians(angle+180))*(size-kante)+point4[1])

        self.points = [point1, point2, point4, point6, point5, point3]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)

class Tile:

    all_tiles = []

    def __init__(self, x, y, w, h, color_b, color_t, command, font_size = 20, font = None, text = 'Button', anchor_point_x = 0, anchor_point_y = 0, icon = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.button_rect = pygame.Rect(x, y, w, h)
        self.color_b = color_b
        self.color_t = color_t
        self.text = text
        self.font = pygame.font.Font(font, font_size)
        self.command = command
        self.anch_x = anchor_point_x
        self.anch_y = anchor_point_y
        self.icon = icon
        self.last_pos = 0
        Tile.all_tiles.append(self)


    def draw(self, screen):
        color = self.color_b

        pygame.draw.rect(screen, color , self.button_rect)
        if self.icon != None:
            icon = pygame.transform.scale(self.icon, (self.w-10, self.h-10))
            screen.blit(icon, (self.x+5,self.y+5))
        else:
            label = self.font.render(self.text, True, self.color_t)
            label_rect = label.get_rect()
            screen.blit(label, (self.x + self.w/2 - label_rect.w/2, self.y + self.h/2 - label_rect.h/2))

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
        else:
            self.last_pos = 0

    def hover_animation(self, screen ,bg_color, corner_size):

        pos_add = math.sin(math.radians(self.last_pos))*10-30

        corners = [ Polygon(0, corner_size, (255, 255, 255),         (pos_add+self.x,        pos_add+self.y)),
                    Polygon(90, corner_size, (255, 255, 255),        (pos_add+self.x,        self.y+self.h-pos_add)),
                    Polygon(270, corner_size, (255, 255, 255),       (self.x+self.w-pos_add, pos_add+self.y)),
                    Polygon(180, corner_size, (255, 255, 255),       (self.x+self.w-pos_add, self.y+self.h-pos_add))]

        screen.fill(bg_color)
        for tile in self.all_tiles:
            tile.draw(screen)
        for corner in corners:
            corner.draw(screen)

        self.last_pos += 5
        
            
def printHello():
    print("hello")

def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    Button1 = Tile(100, 100, 300, 200, (0,0,0), (100, 100, 100), printHello)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            Button1.processEvent(event)
        

        screen.fill((255, 255, 255))

        Button1.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()