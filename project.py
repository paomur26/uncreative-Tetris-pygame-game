# uncreative Tetris Функция "переворачивания" не сделана
import pygame
import random

number = 0
x = True
score = 0


def draw(screen):
    font = pygame.font.Font(None, 100)
    text = "GAME OVER!"
    if score > 1000:
        text = "WIN!!!"
    text = font.render(text, True, (pygame.Color("Red")))
    text_x = 1000 // 2 - text.get_width() // 2
    text_y = 1000 // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def drawscr(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Score:", True, (pygame.Color("white")))
    text_x = 800 - text.get_width() // 2
    text_y = 200 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


def drawchis(screen, chis):
    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
        700, 230, 900, 400), 0)
    font = pygame.font.Font(None, 55)
    text = font.render(str(chis), True, (pygame.Color("white")))
    text_x = 800 - text.get_width() // 2
    text_y = 255 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


class Board:
    # создание поля
    def __init__(self, width, height):
        self.cp = []
        self.width = width
        self.height = height
        self.dt = []
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 50
        self.top = 50
        self.cell_size = 24
        self.cord = []
        self.cc = []

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
                self.cp.append((i * self.cell_size + self.left, j * self.cell_size + self.top, self.cell_size,
                                self.cell_size))
                self.dt.append(0)
        for i in range(self.width):  # Цикл повторный, так как сначала сделал неправильный тип определения
            # координат и создать новый цикл оказаолось проще и быстрее
            for j in range(self.height):
                self.cord.append((
                    j * self.cell_size + self.top, i * self.cell_size + self.left,
                    j * self.cell_size + self.top + self.cell_size,
                    self.cell_size + i * self.cell_size + self.left))
                self.cc.append((i, j))


class Cub:
    def __init__(self, col, cord, number):
        self.col = col
        self.cord = cord
        self.sost = 1
        self.number = number
        self.draw()

    def draw(self):
        pygame.draw.rect(sc, self.col, self.cord, 0)

    def hod(self, cord):
        pygame.draw.rect(sc, pygame.Color(0, 0, 0), self.cord, 0)
        pygame.draw.rect(sc, pygame.Color(255, 255, 255), self.cord, 1)
        self.cord = cord
        self.draw()

    def lejb(self):
        self.sost = 0
        board.dt[board.cp.index(self.cord)] = 1

    def death(self):
        pygame.draw.rect(sc, pygame.Color(0, 0, 0), self.cord, 0)
        pygame.draw.rect(sc, pygame.Color(255, 255, 255), self.cord, 1)
        return 20


class Tetromino:
    def __init__(self):
        global number
        number += 1
        self.number = number * 1
        self.type = random.choice([1, 2, 3, 4, 5, 6, 7])
        self.col = random.choice([pygame.Color("yellow"), pygame.Color("teal"), pygame.Color("Red"),
                                  pygame.Color("cyan"), pygame.Color("hot pink"),
                                  pygame.Color("blue"), pygame.Color("brown"),
                                  pygame.Color("green"), pygame.Color("purple"), pygame.Color("olive"),
                                  pygame.Color("orange")])
        self.noncon = True
        self.cr = []
        self.cb = []
        if self.type == 7:
            self.cifr = [61, 81, 80, 100]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 6:
            self.cifr = [60, 80, 81, 101]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 5:
            self.cifr = [60, 80, 100, 120]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 4:
            self.cifr = [60, 80, 100, 61]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 3:
            self.cifr = [60, 80, 100, 101]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 1:
            self.cifr = [60, 80, 100, 81]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))
        if self.type == 2:
            self.cifr = [60, 80, 61, 81]
            self.cr = [board.cp[self.cifr[0]], board.cp[self.cifr[1]], board.cp[self.cifr[2]],
                       board.cp[self.cifr[3]]]
            self.cb.append(Cub(self.col, self.cr[0], self.number))
            self.cb.append(Cub(self.col, self.cr[1], self.number))
            self.cb.append(Cub(self.col, self.cr[2], self.number))
            self.cb.append(Cub(self.col, self.cr[3], self.number))

    def xhod(self):
        self.cr = [board.cp[board.cp.index(self.cr[0]) + 1], board.cp[board.cp.index(self.cr[1]) + 1],
                   board.cp[board.cp.index(self.cr[2]) + 1],
                   board.cp[board.cp.index(self.cr[3]) + 1]]
        self.cb[2].hod(self.cr[2])
        self.cb[3].hod(self.cr[3])
        self.cb[0].hod(self.cr[0])

        self.cb[1].hod(self.cr[1])
        self.cb[2].hod(self.cr[2])
        self.cb[3].hod(self.cr[3])
        self.cb[0].hod(self.cr[0])
        self.cb[1].hod(self.cr[1])
        if board.cp.index(self.cr[0]) % 20 == 19 or board.cp.index(self.cr[1]) % 20 == 19 or board.cp.index(self.cr[2])\
                % 20 == 19 or board.cp.index(self.cr[3]) % 20 == 19:
            clock.tick()
            self.noncon = False
            self.cb[2].lejb()
            self.cb[3].lejb()
            self.cb[0].lejb()
            self.cb[1].lejb()
            self.cb[2].lejb()
            self.cb[3].lejb()
            self.cb[0].lejb()
            self.cb[1].lejb()
        try:
            if board.dt[board.cp.index(self.cr[0]) + 1] == 1 or board.dt[board.cp.index(self.cr[1]) + 1] == 1 \
                    or board.dt[board.cp.index(self.cr[2]) + 1] == 1 or board.dt[board.cp.index(self.cr[3]) + 1] == 1:
                clock.tick()
                self.noncon = False
                self.cb[2].lejb()
                self.cb[3].lejb()
                self.cb[0].lejb()
                self.cb[1].lejb()
                self.cb[2].lejb()
                self.cb[3].lejb()
                self.cb[0].lejb()
                self.cb[1].lejb()
        except IndexError:
            None

    def dxhod(self):
        try:
            if board.cp.index(self.cr[0]) + 20 >= 0 and board.cp.index(self.cr[1]) + 20 >= 0 \
                    and board.cp.index(self.cr[2]) + 20 >= 0 and board.cp.index(self.cr[3]) + 20 > 0 \
                    and board.dt[board.cp.index(self.cr[0]) + 20] == 0 and board.dt[board.cp.index(self.cr[1]) + 20] ==\
                    0 and board.dt[board.cp.index(self.cr[2]) + 20] == 0 \
                    and board.dt[board.cp.index(self.cr[3]) + 20] == 0:
                self.cr = [board.cp[board.cp.index(self.cr[0]) + 20],
                           board.cp[board.cp.index(self.cr[1]) + 20], board.cp[board.cp.index(self.cr[2]) + 20],
                           board.cp[board.cp.index(self.cr[3]) + 20]]
                self.cb[2].hod(self.cr[2])
                self.cb[3].hod(self.cr[3])
                self.cb[0].hod(self.cr[0])
                self.cb[1].hod(self.cr[1])
                self.cb[2].hod(self.cr[2])
                self.cb[3].hod(self.cr[3])
                self.cb[0].hod(self.cr[0])
                self.cb[1].hod(self.cr[1])
        except IndexError:
            None

    def axhod(self):
        try:
            if board.cp.index(self.cr[0]) - 20 >= 0 and board.cp.index(self.cr[1]) - 20 >= 0 \
                    and board.cp.index(self.cr[2]) - 20 >= 0 and board.cp.index(self.cr[3]) - 20 > 0 \
                    and board.dt[board.cp.index(self.cr[0]) - 20] == 0 and board.dt[board.cp.index(self.cr[1]) - 20] \
                    == 0 and board.dt[board.cp.index(self.cr[2]) - 20] == 0 \
                    and board.dt[board.cp.index(self.cr[3]) - 20] == 0:
                self.cr = [board.cp[board.cp.index(self.cr[0]) - 20],
                           board.cp[board.cp.index(self.cr[1]) - 20], board.cp[board.cp.index(self.cr[2]) - 20],
                           board.cp[board.cp.index(self.cr[3]) - 20]]
                self.cb[2].hod(self.cr[2])
                self.cb[3].hod(self.cr[3])
                self.cb[0].hod(self.cr[0])
                self.cb[1].hod(self.cr[1])
                self.cb[2].hod(self.cr[2])
                self.cb[3].hod(self.cr[3])
                self.cb[0].hod(self.cr[0])
                self.cb[1].hod(self.cr[1])
        except IndexError:
            None


e = True
if e:  # Рудимент
    pygame.init()
    pygame.display.set_caption("Куб")
    size = wi, h = 1000, 1000
    # screen — холст, на котором нужно рисовать:
    sc = pygame.display.set_mode(size)
    pygame.display.flip()
    # ожидание закрытия окна:
    board = Board(20, 10)
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 500)
    board.set_view(50, 50, 47)
    board.render(sc)
    d = Tetromino()
    pygame.display.flip()
    running = True
    drawscr(sc)
    drawchis(sc, score)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if board.dt[2] + board.dt[22] + board.dt[42] + board.dt[62] + board.dt[82] \
                    + board.dt[102] + board.dt[122] + board.dt[142] + board.dt[162] \
                    + board.dt[182] > 1:
                draw(sc)
                x = False
            if not d.noncon and x:
                d = Tetromino()
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed()[pygame.K_s] and d.noncon or event.type == MYEVENTTYPE and d.noncon and x:
                sq = True
                d.xhod()
                pygame.time.set_timer(MYEVENTTYPE, 500)
            if pygame.key.get_pressed()[pygame.K_a] and clock.tick() > 5 and d.noncon and x:
                d.axhod()
                clock.tick()
            if pygame.key.get_pressed()[pygame.K_d] and clock.tick() > 5 and d.noncon and x:
                clock.tick()
                d.dxhod()
            for i in range(20):
                if board.dt[i] + board.dt[i + 20] + board.dt[i + 40] + board.dt[i + 60] + board.dt[i + 80] \
                        + board.dt[i + 100] + board.dt[i + 120] + board.dt[i + 140] + board.dt[i + 160] \
                        + board.dt[i + 180] == 10 and x:
                    board.dt[i] = 0
                    board.dt[i + 20] = 0
                    board.dt[i + 40] = 0
                    board.dt[i + 60] = 0
                    board.dt[i + 80] = 0
                    board.dt[i + 100] = 0
                    board.dt[i + 120] = 0
                    board.dt[i + 140] = 0
                    board.dt[i + 160] = 0
                    board.dt[i + 180] = 0
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 20], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 20], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 40], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 40], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 60], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 60], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 80], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 80], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 100], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 100], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 120], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 120], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 140], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 140], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 160], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 160], 1)
                    pygame.draw.rect(sc, pygame.Color(0, 0, 0), board.cp[i + 180], 0)
                    pygame.draw.rect(sc, pygame.Color(255, 255, 255), board.cp[i + 180], 1)
                    score += 100
                    drawchis(sc, score)

        pygame.display.flip()
    pygame.quit()
else:  # Рудимент
    print("Неправильный формат ввода")
