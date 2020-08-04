import pygame

# Game setup
field_width = 700
field_height = 500
field_cols = 14
field_rows = 10

# Variables
hero_angle = 0

# Get the size of the full display
def getDisplaySize():
    return (field_width,field_height)

# Get the field rectangle
def getFieldRect():
    return (0,0,field_width,field_height)


pygame.init()

display = pygame.display.set_mode(getDisplaySize())
pygame.display.update()

def draw():
    pygame.draw.rect(display,(0,185,0),getFieldRect())
    image_hero = pygame.image.load("./mimes/ladybug.png")
    image_hero = pygame.transform.scale(image_hero,(77,98))
    image_hero = pygame.transform.rotate(image_hero,hero_angle)
    display.blit(image_hero,(10,10))
    pygame.display.update()

draw()


# Actions
def actionHeroRotateLeft():
    global hero_angle
    hero_angle = hero_angle + 90
    hero_angle = hero_angle % 360
    draw()
#image_hero = pygame.image.load("./mimes/ladybug.png")
#image_hero = pygame.transform.scale(image_hero,(77,98))
#image_hero = pygame.transform.rotate(image_hero,198)
#display.blit(image_hero,(20,20))
#pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #event.pos
            actionHeroRotateLeft()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
