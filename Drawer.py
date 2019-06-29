from engineM2 import *
pacman = sprite(100, 100, "pacman.png")
laserList = []
dotList = []
fallSpeed = 4
pac_speed = 4



def spawnDots(amount):

    sideMargin = 10
    topMargin = 10
    spacing = 2
    
    for i in range(0, amount):
        for j in range(0, amount):
            dotList.append(sprite(sideMargin + i * spacing, topMargin + j * spacing, "dot.png"))

spawnDots(300)
while True:
    if kb.keysPressed[K_RIGHT]:
        pacman.x += pac_speed
    if kb.keysPressed[K_LEFT]:
        pacman.x -= pac_speed
    if kb.keysPressed[K_UP]:
        pacman.y -= pac_speed
    if kb.keysPressed[K_DOWN]:
        pacman.y += pac_speed
        


    for someDot in dotList:
        if someDot.collide(pacman):
            dotList.remove(someDot)
            someDot.destroy()
                
 
        
    runGame(black)
    
 
