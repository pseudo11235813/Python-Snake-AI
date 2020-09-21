from Snakke import *



def drawGrid():
    for x in range(0,window_width,snake_width):
        pygame.draw.line(disp,(15,15,15),(x,0),(x,window_height))
    for y in range(0,window_height,snake_width):
        pygame.draw.line((disp),(15,15,15),(0,y),(window_width,y))

def EuclidianDistance(snake_x,snake_y,apfel_x,apfel_y): #heuristic function
    x_diff = abs(snake_x - apfel_x)
    y_diff = abs(snake_y - apfel_y)
    euclidianDistance = math.sqrt(x_diff * x_diff + y_diff * y_diff)
    return euclidianDistance

def ManhattanDistance(snake_x,snake_y,apfel_x,apfel_y): #heuristic function
    x_diff = abs(snake_x - apfel_x)
    y_diff = abs(snake_y - apfel_y)
    ManhattanDistance = x_diff + y_diff
    return ManhattanDistance

def isForbidden(snake_x,snake_y):
    print(snake_x,snake_y)
    for seg in snakeList[0:len(snakeList) - 1]:
        if snake_x == seg[0] and snake_y == seg[1]:
            return True
    if snake_x + snake_width > window_width or snake_x <= 0.0 or snake_y + snake_height > window_height or snake_y <= 0.0:
            return True
    return False

def worstMove(dist):
    global direction

    maxx = max(dist[0][0], dist[1][0], dist[2][0], dist[3][0])
    print(dist[0][0], dist[1][0], dist[2][0], dist[3][0])
    for foo in dist:
        if foo[0] == maxx and not isForbidden(foo[1],foo[2]):
            direction = dist.index(foo)
            return foo[1], foo[2]


def cost(distances):
    for seg in snakeList[0:len(snakeList) - 1]:
        for dem in distances:
            if dem[1] == seg[0] and dem[2] == seg[1]:
                dem[0] += 2000000000000000
    return distances

def xSurface(distances): #heuristic function
    areas = [0]*4
    for i in range(4):
        areas[i] = [distances[i][1] - 30, distances[i][2] - 30, 60, 60]
    i = 0

    for area in areas:
        counter = 0
        for seed in range(int(distances[i][1]) - 45 , int(distances[i][1]) - 45 + 91,15):
            for seem in range(int(distances[i][2]) - 45, int(distances[i][2]) - 45+ 91,15):
                for seg in snakeList[0:len(snakeList) - 1]:
                    if seg[0] == seed and seg[1] == seem:
                        counter += 15
            i += i
        area.append(counter)
    return areas



def successor(dist):
    global direction
    minn = dist[0][0]
    for item in dist:
        if item[0] <= minn:
            minn = item[0]
    for foo in dist:
        if minn == foo[0]:
            return foo[1],foo[2]

def euclidianDistances(snake_x, snake_y , apfel_x , apfel_y): #GREEDY BEST FIRST SEARCH
    x1 = snake_x + snake_speed
    x2 = snake_x - snake_speed
    y1 = snake_y + snake_speed
    y2 = snake_y - snake_speed
    distances = [0] * 4
    distances[0] = [EuclidianDistance(x1, snake_y, apfel_x, apfel_y), x1, snake_y]
    distances[1] = [EuclidianDistance(x2, snake_y, apfel_x, apfel_y), x2, snake_y]
    distances[2] = [EuclidianDistance(snake_x, y1, apfel_x, apfel_y), snake_x, y1]
    distances[3] = [EuclidianDistance(snake_x, y2, apfel_x, apfel_y), snake_x, y2]
    # if direction == 0:
    #     distances[1] = [56156154524524525424526156,156156156,1561561]
    # elif direction == 1:
    #     distances[0] = [5615615615111111111111111116,156156156,1561561]
    # elif direction == 2:
    #     distances[3] = [5615615645242782452425272542156,156156156,1561561]
    # elif direction == 3:
    #     distances[2] = [56156156156,156156156,1561561]
    return distances

def ManhattenDistances(snake_x,snake_y,apfel_x,apfel_y): #GREEDY BEST FIRST SEARCH
    x1 = snake_x + snake_speed
    x2 = snake_x - snake_speed
    y1 = snake_y + snake_speed
    y2 = snake_y - snake_speed
    distances = [0] * 4

    distances[0] = [ManhattanDistance(x1, snake_y, apfel_x, apfel_y), x1, snake_y]
    distances[1] = [ManhattanDistance(x2, snake_y, apfel_x, apfel_y), x2, snake_y]
    distances[2] = [ManhattanDistance(snake_x, y1, apfel_x, apfel_y), snake_x, y1]
    distances[3] = [ManhattanDistance(snake_x, y2, apfel_x, apfel_y), snake_x, y2]

    return distances

def BFS():
    pass


def agentGameLoop():
    global snake_x,snake_y,apfel_x,apfel_y
    qx = apfel_x
    qy = apfel_y
    while True:
        disp.fill(grey)
        eventHandeling()
        drawGrid()
        distances = euclidianDistances(snake_x, snake_y , qx,qy)
        cost(distances)
        snake_x,snake_y = successor(distances)
        qx,qy = SnakeFormatting(snake_x,snake_y)
        set_boundaries()
        pygame.display.update()
        clock.tick(FPS)


agentGameLoop()