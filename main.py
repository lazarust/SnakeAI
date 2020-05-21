import random
from classes import *
import classes
import tkinter as tk
from tkinter import messagebox

def drawGrid(width, rows, surface):
    sqrSize = width // rows
    x = 0
    y = 0

    for row in range(rows):
        x += sqrSize
        y += sqrSize
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width), 1)
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y), 1)


def redrawWindow(surface):
    global rows, width, snake, snack
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(body):
    global rows
    positions = body.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return tuple((x, y))


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, snake, snack
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width))
    snake = classes.snake((0, 255, 0), (10,10))
    snack = classes.block(randomSnack(snake), color=(255, 0, 0))
    running = True
    clock = pygame.time.Clock()

    while running is True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = block(randomSnack(snake), color=(255, 0, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                print('Score: ', len(snake.body))
                message_box('You Lost!', 'Play again...')
                snake.reset((10, 10))
                break

        redrawWindow(window)
    pass


main()
