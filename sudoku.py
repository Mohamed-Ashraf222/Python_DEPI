import pygame
pygame.font.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Sudoku')
x = 0
y = 0
diff = 500 / 9
value = 0

defaultgrid = [
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [7, 8, 0, 4, 0, 0, 0, 2, 0],
    [0, 0, 2, 6, 0, 1, 0, 7, 8],
    [6, 1, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 7, 5, 4, 0, 0, 6, 1],
    [0, 0, 1, 7, 5, 0, 9, 3, 0],
    [0, 7, 0, 3, 0, 0, 0, 1, 0],
    [0, 4, 0, 2, 0, 6, 0, 0, 7],
    [0, 2, 0, 0, 0, 7, 4, 0, 0]
]

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)

def cord(pos):
    global x, y
    x = pos[0] // diff
    y = pos[1] // diff

def highlightbox():
    for k in range(2):
        pygame.draw.line(screen, (0, 0, 0), (x * diff - 3, y * diff + k * diff), (x * diff + diff + 3, y * diff + k * diff), 7)
        pygame.draw.line(screen, (0, 0, 0), (x * diff + k * diff, y * diff), (x * diff + k * diff, y * diff + diff), 7)

def drawlines():
    for i in range(9):
        for j in range(9):
            if defaultgrid[i][j] != 0:
                pygame.draw.rect(screen, (255, 255, 0), (j * diff, i * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))

                text_width = text1.get_width()
                text_height = text1.get_height()
                center_x = j * diff + (diff - text_width) / 2
                center_y = i * diff + (diff - text_height) / 2
                
                screen.blit(text1, (center_x, center_y))


    for l in range(10):
        thick = 7 if l % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(screen, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)

def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    screen.blit(text1, (x * diff + 15, y * diff + 15))

def raiseerror():
    text1 = font.render("Wrong!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

def raiseerror1():
    text1 = font.render("Wrong! Enter a valid key for the game", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it] == value or m[it][l] == value:
            return False
    it = k // 3
    jt = l // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == value:
                return False
    return True

def solvegame(defaultgrid, i, j):
    while defaultgrid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()

    for it in range(1, 10):
        if validvalue(defaultgrid, i, j, it):
            defaultgrid[i][j] = it
            global x, y
            x, y = i, j
            screen.fill((255, 255, 255))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(20)
            if solvegame(defaultgrid, i, j):
                return True
            defaultgrid[i][j] = 0
            screen.fill((0, 0, 0))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(50)
    return False

def gameresult():
    text1 = font.render("Game Finished", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

flag = True
flag1, flag2, rs, error = 0, 0, 0, 0

while flag:
    screen.fill((255, 182, 193))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cord(pos)
            flag1 = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = max(0, x - 1)
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x = min(8, x + 1)
                flag1 = 1
            if event.key == pygame.K_UP:
                y = max(0, y - 1)
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y = min(8, y + 1)
                flag1 = 1
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                value = int(event.unicode)
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs, error, flag2 = 0, 0, 0
                defaultgrid = [[0] * 9 for _ in range(9)]
            if event.key == pygame.K_d:
                rs, error, flag2 = 0, 0, 0
                defaultgrid = [
                    [0, 0, 4, 0, 6, 0, 0, 0, 5],
                    [7, 8, 0, 4, 0, 0, 0, 2, 0],
                    [0, 0, 2, 6, 0, 1, 0, 7, 8],
                    [6, 1, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 7, 5, 4, 0, 0, 6, 1],
                    [0, 0, 1, 7, 5, 0, 9, 3, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                ]

    if flag2 == 1:
        if not solvegame(defaultgrid, 0, 0):
            error = 1
        else:
            rs = 1
        flag2 = 0

    if value != 0:
        fillvalue(value)
        if validvalue(defaultgrid, int(y), int(x), value):
            defaultgrid[int(y)][int(x)] = value
        else:
            defaultgrid[int(y)][int(x)] = 0
            raiseerror1()
        value = 0

    if error == 1:
        raiseerror()
    if rs == 1:
        gameresult()

    drawlines()
    if flag1 == 1:
        highlightbox()
    pygame.display.update()

pygame.quit()
