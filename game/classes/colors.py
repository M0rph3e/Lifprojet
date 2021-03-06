from pygame import Color

DISTANCE_DEPL_MAX=7

WIDTH = 400 
HEIGHT = 400
CELLWIDTH = 20
CELLHEIGHT = 20

TRANSPARENT = (0,0,0,255)

BLACK  = Color(0, 0, 0)
WHITE  = Color(255, 255, 255)
GREEN  = Color(0, 255, 0)
RED    = Color(255, 0, 0)
BLUE   = Color(0, 0, 255)
YELLOW = Color(255, 200, 0)
GREY   = Color(160, 160, 160)
ICE    = Color(92, 247, 251)

GREEN_A50  = Color(0, 255, 0, 50)
RED_A50    = Color(255, 0, 0, 50)
BLUE_A50   = Color(0, 0, 255, 50)
YELLOW_A50 = Color(255, 200, 0, 50)
GREY_A50   = Color(160, 160, 160, 50)
GREY_A200  = Color(100, 100, 100, 200)

SELECTED = Color(255, 200, 0, 100)
MOVE     = Color(0, 0, 255, 75)
ATTACK   = Color(255, 0, 0, 75)
PLAYED   = Color(75, 75, 75, 150)

WALL = (120,120,115)
GROUND = (170,110,80)
UNIT = Color (100,100,255)
ENEMY = Color(255,100,100)

HACHE = (75,125,0)
EPEE = (125,0,0)
LANCE = (0,50,125) 


def getPositionMoy(tabPawn):
    posX = 0
    posY = 0
    for p in tabPawn:
        posX += p.x
        posY += p.y
    posX = round(posX / len(tabPawn))
    posY = round(posY / len(tabPawn))
    
    return (posX,posY)

