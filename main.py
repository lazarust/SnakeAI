import random
from classes import *
import classes


def redrawWindow(surface):
    global rows, width, snake, snack
    surface.fill((96, 96, 96))
    snake.draw(surface)
    snack.draw(surface)
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


def main():
    global width, rows, snake, snack
    width = 1000
    rows = 40
    window = pygame.display.set_mode((width, width))
    snake = classes.snake((0, 255, 0), (10,10))
    snack = classes.block(randomSnack(snake), color=(255, 0, 0))
    running = True
    clock = pygame.time.Clock()

    while running is True:
        pygame.time.delay(10)
        clock.tick(100)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            pygame.display.set_caption(f'Score: {len(snake.body)}')
            snack = block(randomSnack(snake), color=(255, 0, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                pygame.display.set_caption(f'Score: 0')
                snake.reset((10, 10))
                break

        redrawWindow(window)
    pass


main()
