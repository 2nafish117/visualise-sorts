import random
import pygame as pg

FPS = 100
maxNum = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
arr = [i for i in range(1, maxNum + 1)]
random.shuffle(arr)

windowHeight = 600
windowWidth = 800
numElements = len(arr)
rectWidth = windowWidth / numElements

gameDisplay = pg.display.set_mode((windowWidth, windowHeight))
pg.display.set_caption('Visualise Sorts')
clock = pg.time.Clock()

def handleInput():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    return

def render():
    gameDisplay.fill(BLACK)
    for i in range(len(arr)):
        rectHeight = (windowHeight / maxNum) * arr[i]
        left = i * rectWidth
        top = windowHeight - rectHeight
        rect = pg.Rect(left, top, rectWidth, rectHeight)
        pg.draw.rect(gameDisplay, WHITE, rect)
    pg.display.update()
    clock.tick(FPS)
    return

def basicStep():
    handleInput()
    render()

def reset():
    global arr
    arr = [i for i in range(1, maxNum + 1)]
    random.shuffle(arr)