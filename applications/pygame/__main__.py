import pygame

# Game setup
field_width = 700
field_height = 450
field_cols = 14
field_rows = 9

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



# Hideout
hero_hideouts = [(7,1),(3,3),(10,6),(6,4)]
heroHideoutImage = None
heroHideoutPosition = None

pygame.init()

display = pygame.display.set_mode(getDisplaySize())
pygame.display.update()

def draw():
    global hero_position
    global heroHideoutImage
    global heroHideoutPosition

    # Background
    pygame.draw.rect(display,(0,185,0),getFieldRect())

    # Hideouts
    heroHideoutImage = None
    for hideoutPosition in hero_hideouts:
        image_hideout = pygame.image.load("./mimes/bush.png")
        image_hideout = pygame.transform.scale(image_hideout,(50,50))
        hideout_rect = getFieldPositionRect(hideoutPosition)
        image_hideout = display.blit(image_hideout,hideout_rect[0:2])
        # Check, if hero is there
        if hideoutPosition == heroHideoutPosition:
            heroHideoutImage = image_hideout


    # Hero
    if heroHideoutPosition == None:
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
    global heroHideoutImage
    if heroHideoutImage != None:
        return
    hero_angle = hero_angle + 90
    hero_angle = hero_angle % 360

    draw()
def actionHeroMove():
    global hero_position
    global hero_angle
    global heroHideoutImage
    global heroHideoutPosition
    if heroHideoutImage != None:
        return
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
    for hideoutPosition in hero_hideouts:
        if hideoutPosition == hero_position:
            heroHideoutPosition = hideoutPosition

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
            if heroHideoutImage != None:
                #print(heroHideoutImage.get_rect())
                if heroHideoutImage.collidepoint(event.pos):
                    heroHideoutPosition = None
                    draw()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
