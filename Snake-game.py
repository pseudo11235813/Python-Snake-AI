import sys,pygame,random,time,math
from pygame.locals import *

pygame.init()
FPS = 60

green = (0,200,0)
red = (255,0,0)
blue = (0,0,255)
grey = (35,35,35)
snake_color = green
apple = red

window_width =810
window_height = 600
snake_x = window_width/2
snake_y = window_height/2
snake_width = 15
snake_height = 15
snake_speed = 15
speed_x = 15
speed_y = 0
direction = 0 #right = 0, left = 1, up = 2 , down = 3

font = pygame.font.Font('freesansbold.ttf',25)

disp = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("SNAKEBOI")

clock = pygame.time.Clock()

snakeList = []
snakeLength = 5

apfel_x = round(random.randint(0,760)/15)*15
apfel_y = round(random.randint(0,560)/15)*15
def Snake(snakeList,snake_width,snake_height,snake_color):
    if len(snakeList) >= snakeLength:
        del snakeList[0]
    for snake in snakeList:
        pygame.draw.rect(disp, snake_color, (snake[0], snake[1], snake_width, snake_height))



def SnakeFormatting(snake_x,snake_y):
    global snakeLength
    ax = apfel_x
    ay = apfel_y
    snakehead = []
    snakehead.append(snake_x)
    snakehead.append(snake_y)
    snakeList.append(snakehead)
    x = random.randrange(0,255)
    y = random.randrange(0,255)
    z = random.randrange(0,255)
    color = (x, y, z)
    apfel(apfel_x, apfel_y)
    Snake(snakeList, snake_width, snake_height, color)
    if snake_x == apfel_x and snake_y == apfel_y:
        snakeLength += 2
        ax,ay = random_Apfel_coords()
    for seg in snakeList[0:len(snakeList) - 1]:
        if snake_x == seg[0] and snake_y == seg[1]:
            quit()
    return ax,ay
def apfel(apfel_x,apfel_y):
    x = random.randrange(0, 255)
    y = random.randrange(0, 255)
    z = random.randrange(0, 255)
    color = (x, y, z)
    pygame.draw.rect(disp,color,(apfel_x,apfel_y,snake_width,snake_height))

def random_Apfel_coords():
    global apfel_x,apfel_y
    apfel_x = round(random.randint(0, 760) / 15) * 15
    apfel_y = round(random.randint(0, 570) / 15) * 15
    return apfel_x,apfel_y


def eventHandeling():
    global speed_x,speed_y,direction
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and direction != 0:
                speed_x = -snake_speed
                speed_y = 0
                direction = 1
            elif event.key == K_RIGHT and direction != 1:
                speed_x = snake_speed
                speed_y = 0
                direction = 0
            elif event.key == K_DOWN and direction != 2:
                speed_y = snake_speed
                speed_x = 0
                direction = 3
            elif event.key == K_UP and direction != 3:
                speed_y = -snake_speed
                speed_x = 0
                direction = 2
def x_movement():
    global snake_x
    snake_x += speed_x

def y_movement():
    global snake_y
    snake_y += speed_y

def set_boundaries():
    if snake_x + snake_width > window_width or snake_x < 0 or snake_y + snake_height > window_height or snake_y < 0:
        quit()

def drawGrid():
    for x in range(0,window_width,snake_width):
        pygame.draw.line(disp,(15,15,15),(x,0),(x,window_height))
    for y in range(0,window_height,snake_width):
        pygame.draw.line((disp),(15,15,15),(0,y),(window_width,y))

