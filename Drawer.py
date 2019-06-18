from engineM2 import *
dotList = []
pacman = sprite(100, 100, "pacman.png")

def spawnDots(amount):

    sideMargin = 10
    topMargin = 10
    spacing = 2
    
    for i in range(0, amount):
        for j in range(0, amount):
            dotList.append(sprite(sideMargin + i * spacing, topMargin + j * spacing, "dot.png"))
spawnDots(300)

while True:
    runGame(black)
