# Одномерное горение с неявной разностной схемой

import pygame as p
from pygame.locals import *
import numpy as np
import time


hi = 0.4
ti = 0.1
E = 1
Ekrit = 6.56
delta_t = 1
h = 1
step = 250

m = 50*2
n = 26*2

pix = 10

N = np.zeros(m)
T = np.zeros(m)

y_s = int(n/2-1)

T[0] = 1



for i in range(0,m):
    N[i] = 1


def print_mas():
    for i in range(0,m):
        p.draw.rect(root, (255-255*N[i], 255-255*N[i], 255-255*N[i]), [i * pix, (y_s+1) * pix, pix, pix])

def print_temper():
    p.draw.rect(root, (255, 255, 255), [0, 0, 1000, 260])
    for i in range(0,m):
        p.draw.rect(root, (255, 0, 0), [i * pix, 260-260*T[i], pix, 260*T[i]])




# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Создаем окно
root = p.display.set_mode((1000, 520))
# Основной цикл
while 1:
    # Заполняем экран белым цветом
    root.fill(WHITE)

    for i in p.event.get():
        if i.type == QUIT:
            quit()
    p.display.update()

    print_mas()
    print_temper()

    p.display.update()
    time.sleep(1)


    for x in range(step):
        A = 0
        B = 0
        for i in range(0,m):
            b = -1 * (2 + 2 * (h * h) / (hi * delta_t))
            bd = 2 - 2 * (h * h) / (hi * delta_t)
            if T[i] != 0:
                deltaN = -1 * N[i] / ti * np.exp(-1 * E / T[i]) * delta_t
            else:
                deltaN = 0
            N[i] = N[i] + deltaN

            if i == 0:
                d = -1 * T[i+1] + bd * T[i]
                a = 0
                c = 1
                A_next = (-1 * c) / (b - a * A)
                B_next = (d - a * B) / (b - a * A)
                T[i] = A_next * T[i+1] + B_next - deltaN
            elif i == m - 1:
                d = -1 * T[i-1] + bd * T[i]
                c = 0
                a = 1
                A_next = (-1 * c) / (b - a * A)
                B_next = (d - a * B) / (b - a * A)

                T[i] = A_next * T[i-1] + B_next - deltaN
            else:
                a = 1
                c = 1
                d = -1 * T[i-1] + bd * T[i] - T[i+1]
                A_next = (-1 * c) / (b - a * A)
                B_next = (d - a * B) / (b - a * A)
                T[i] = A_next * T[i+1] + B_next - deltaN

            if (T[i] > 1): T[i] = 1
            if (T[i] < 0): T[i] = 0
            if (N[i] < 0): N[i] = 0

            A = A_next
            B = B_next

        print_mas()
        print_temper()
        p.display.update()
        time.sleep(0.2)