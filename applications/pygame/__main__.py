import pygame

# Game setup
field_width = 700
field_height = 500
field_cols = 14
field_rows = 10

# Variables
hero_angle = 0
hero_position = (2,7)


# UI Elements
rectButtonLeft = None
rectButtonMove = None

# Get the size of the full display
def getDisplaySize():
    return (field_width+200,field_height)

# Get the field rectangle
def getFieldRect():
    return (0,0,field_width,field_height)

def getFieldElementWidth():
    global field_width
    global field_cols
    return field_width / field_cols

def getFieldElementHeight():
    global field_height
    global field_rows
    return field_height / field_rows

# Hero Utilities


# Coordinate Utilities
def getFieldPositionRect(xy_tuple): # (xPosition,yPosition) => (xPixel,yPixel,width,height)
    xPixel = xy_tuple[0] * getFieldElementWidth()
    yPixel = xy_tuple[1] * getFieldElementHeight()
    return (int(xPixel),int(yPixel),int(getFieldElementWidth()),int(getFieldElementHeight()))

pygame.init()

display = pygame.display.set_mode(getDisplaySize())
pygame.display.update()

def draw():
    global hero_position

    pygame.draw.rect(display,(0,185,0),getFieldRect())
    image_hero = pygame.image.load("./mimes/ladybug.png")
    image_hero = pygame.transform.scale(image_hero,(39,50))
    image_hero = pygame.transform.rotate(image_hero,hero_angle)

    hero_rect = getFieldPositionRect(hero_position)
    display.blit(image_hero,hero_rect[0:2])
    pygame.display.update()

# Print the Buttons
rectButtonLeft = pygame.draw.rect(display, (255, 0, 0),(720, 100, 160, 100))
rectButtonMove = pygame.draw.rect(display, (0, 0, 250),(720, 250, 160, 100))

draw()


# Actions
def actionHeroRotateLeft():
    global hero_angle
    hero_angle = hero_angle + 90
    hero_angle = hero_angle % 360
    draw()
def actionHeroMove():
    global hero_position
    global hero_angle
    if hero_angle == 0:
        newX = hero_position[0]
        newY = hero_position[1] - 1
    elif hero_angle == 90:
        newX = hero_position[0] - 1
        newY = hero_position[1]
    elif hero_angle == 180:
        newX = hero_position[0]
        newY = hero_position[1] + 1
    elif hero_angle == 270:
        newX = hero_position[0] + 1
        newY = hero_position[1]
    else:
        newX = hero_position[0]
        newY = hero_position[1]
    if newX < 0:
        newX = 0
    if newX >= field_cols:
        newX = field_cols - 1
    if newY < 0:
        newY = 0
    if newY >= field_rows:
        newY = field_rows - 1
    hero_position = (newX,newY)
    draw()
#image_hero = pygame.image.load("./mimes/ladybug.png")
#image_hero = pygame.transform.scale(image_hero,(77,98))
#image_hero = pygame.transform.rotate(image_hero,198)
#display.blit(image_hero,(20,20))
#pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rectButtonLeft.collidepoint(event.pos):
                actionHeroRotateLeft()
            if rectButtonMove.collidepoint(event.pos):
                actionHeroMove()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
