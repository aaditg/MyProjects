from engineM2 import *
pacman = sprite(100, 100, "pacman.png")
alienList = []
laserList = []
dotList = []
UFOList = []
fallSpeed = 4
pac_speed = 4
shootSpeed = 6
ammo = 0
wave = 0
cooldown = 0
chase = 0
score = 0
exist = 0

def destroyp(self):
    del(self)
    return None

def spawnDots(amount):

    sideMargin = 10
    topMargin = 10
    spacing = 20
    
    for i in range(0, amount):
        for j in range(0, amount):
            dotList.append(sprite(sideMargin + i * spacing, topMargin + j * spacing, "dot.png"))

spawnDots(30)
def spawnAliens(amount):

    sideMargin = 700
    topMargin = 50
    spacing = 100
    
    for i in range(0, amount):
        alienList.append(sprite(sideMargin, topMargin + i * spacing, "alien.png"))
        

spawnAliens(6)
def spawnUFO(amount):
    sideMargin = 750
    topMargin = 50
    spacing = 100
    
    for i in range(0, amount):
        alienList.append(sprite(sideMargin, topMargin + i * spacing, "UFO.png"))
    
while True:
    if kb.keysPressed[K_RIGHT] and exist == 0:
        pacman.x += pac_speed
    if kb.keysPressed[K_LEFT] and exist == 0:
        pacman.x -= pac_speed
    if kb.keysPressed[K_UP] and exist == 0:
        pacman.y -= pac_speed
    if kb.keysPressed[K_DOWN] and exist == 0:
        pacman.y += pac_speed
        
    for someAlien in alienList:
        someAlien.x -= fallSpeed
    
    if wave == 5 and cooldown == 0:
        spawnUFO(1)
        cooldown = cooldown + 1
        chase = chase + 1
                
    for someLaser in laserList:
        someLaser.x += shootSpeed
        for someAlien in alienList:
            if someLaser.collide(someAlien):
                alienList.remove(someAlien)
                someAlien.destroy()
                score = score + 1
                laserList.remove(someLaser)
                someLaser.destroy()
                
    for someAlien in alienList:
        if someAlien.x <= 0:
                alienList.remove(someAlien)
                someAlien.destroy()
                wave = wave + 1

    for someDot in dotList:
        if someDot.collide(pacman)  and exist == 0:
            dotList.remove(someDot)
            someDot.destroy()
            ammo = ammo + 1
                
    for someUFO in UFOList:
        if someUFO.x <= 0:
            UFOList.remove(someUFO)
            someUFO.destroy()
            wave += wave
            for someLaser in laserList:
                if someLaser.collide(someUFO):
                    alienList.remove(someUFO)
                    someUFO.destroy()
                    laserList.remove(someLaser)
                    someLaser.destroy()

    for someAlien in alienList:
        if pacman.collide(someAlien):
            exist = 1
            del(pacman)
            print("Game Over. Your score was " + str(score))
        
    if alienList == []:
        spawnAliens(6)
    
    if kb.singlePress(K_SPACE)and exist == 0 and ammo> 1:
    

            laserList.append(sprite(pacman.x, pacman.y, "laser.png"))
            ammo = ammo -1
        
    if ammo > 20 and kb.singlePress(K_SPACE) and exist == 0:
                laserList.append(sprite(pacman.x, pacman.y, "laser.png"))
                ammo = ammo - 1

        
    runGame(black)
    
 
