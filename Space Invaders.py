from engineM2 import *

shipSpeed = 4
ship = sprite(display_width/2, display_height - 64, "ship.png")

fallSpeed = 2
alienList = []

shootSpeed = 3
laserList = []

def spawnAliens(amount):

    sideMargin = 30
    topMargin = 50
    spacing = 100
    
    for i in range(0, amount):
        alienList.append(sprite(sideMargin + i * spacing, topMargin, "alien.png"))

spawnAliens(6)

while True:

    if kb.keysPressed[K_RIGHT] and ship.x + ship.width < display_width:
        ship.x += shipSpeed

    if kb.keysPressed[K_LEFT] and ship.x > 0:
        ship.x -= shipSpeed

    for someAlien in alienList:
        someAlien.y += fallSpeed

    for someLaser in laserList:
        someLaser.y -= shootSpeed
        for someAlien in alienList:
            if someLaser.collide(someAlien):
                alienList.remove(someAlien)
                someAlien.destroy()
                laserList.remove(someLaser)
                someLaser.destroy()
                

    if kb.singlePress(K_SPACE):
        laserList.append(sprite(ship.x, ship.y, "laser.png"))


    runGame(blue)
