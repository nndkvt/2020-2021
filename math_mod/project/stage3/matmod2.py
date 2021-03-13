# Двумерное горение с явной схемой

import pygame as p
from pygame.locals import *
import numpy as np
import time


hi = 0.4 #температурапроводность
ti = 0.00001 #характерное время перераспределения энергии
E = 1 #энергия активации
Ekrit = 6.56
delta_t = 1
h = 1
step = 250

m = 50*4
n = 26*4

pix = 5

N = np.zeros((n,m))
T = np.zeros((n,m))

newT = T

x_s = int(m/2-1)
y_s = int(n/2-1)


#___________________________________
# Вертикальынй стержень
#____________________________________

"""
T[y_s][x_s] = 1

for i in range(y_s,n):
    for j in range(x_s-3,x_s+3):
        N[i][j] = 1
"""
#___________________________________
# Горизонтальный стержень
#____________________________________


T[y_s-3][x_s] = 1

for i in range(y_s-3,y_s+3):
    for j in range(x_s-40,x_s+40):
        N[i][j] = 1


#вывод температуры
def print_temper():
    for i in range(0,n):
        for j in range(0,m):
            p.draw.rect(root, (255 * T[i][j],255 * T[i][j],255 * T[i][j]), [j * pix, i * pix, pix, pix])
#вывод вещества
def print_mas():
    for i in range(0,n):
        for j in range(0,m):
            p.draw.rect(root, (255 - 255 * N[i][j],255 - 255 * N[i][j],255 - 255 * N[i][j]), [j * pix, i * pix, pix, pix])


# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Создаем окно
root = p.display.set_mode((1000, 520))

# Основной цикл
while 1:
    root.fill(BLACK)

    for i in p.event.get():
        if i.type == QUIT:
            quit()
    p.display.update()

    # print_temper()
    print_mas()


    p.display.update()
    time.sleep(0.5)

    coef = hi * (delta_t / (h * h))

    for x in range(step):




        for i in range(1,n):
            for j in range(1,m):
                #считаем изменение вещества
                if T[i][j]!=0:
                    deltaN = -1 * N[i][j] / ti * np.exp(-1*E/T[i][j]) * delta_t
                else: deltaN = 0


                #изменение температуры в зависимости от точки
                if (i == 0 and j == 0):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j]) - deltaN

                if (i == 0 and j > 0 and j < m - 1):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j]) - deltaN

                if (i == 0 and j == m - 1):
                    newT[i][j] = T[i][j] + coef * (- 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j]) - deltaN

                if (i > 0 and j == 0 and i < n - 1):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j] + T[i - 1][j]) - deltaN

                if (i > 0 and j > 0 and i < n - 1 and j < m - 1):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j] + T[i - 1][j]) - deltaN

                if (i > 0 and j == m - 1 and i < n - 1):
                    newT[i][j] = T[i][j] + coef * (- 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (T[i + 1][j] - 2 * T[i][j] + T[i - 1][j]) - deltaN

                if (i == n - 1 and j == 0):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j]) \
                                 + coef * (- 2 * T[i][j] + T[i - 1][j]) - deltaN

                if (i == n - 1 and j > 0 and j < m - 1):
                    newT[i][j] = T[i][j] + coef * (T[i][j + 1] - 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (- 2 * T[i][j] + T[i - 1][j]) - deltaN
                if (i == n - 1 and j == m - 1):
                    newT[i][j] = T[i][j] + coef * (- 2 * T[i][j] + T[i][j - 1]) \
                                 + coef * (- 2 * T[i][j] + T[i - 1][j]) - deltaN


                N[i][j] = N[i][j] + deltaN
                if (N[i][j] < 0): N[i][j] = 0

                if(newT[i][j]>1): newT[i][j] = 1
                if(newT[i][j]<0): newT[i][j] = 0



        T = newT

        # print_temper()
        print_mas()


        p.display.update()