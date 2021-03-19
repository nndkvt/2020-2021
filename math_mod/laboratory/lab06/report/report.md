---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №6"
author: Попов Олег Павлович
institute: RUDN University, Moscow, Russian Federation
date: 2021, 18 Марта -- 20 Марта

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: DejaVuSerif
romanfont: DejaVuSerif
sansfont: DejaVuSans
monofont: DejaVuSansMono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

В ходе данной работы необходимо ознакомиться с моделью SIR и решить задачу об эпидемии.

# Задание

1) Ознакомиться с файлами по лабораторной работе №6, находящимися в открытом доступе на ТУИС: файлом с теоретической частью и файлом с вариантами задач.
2) Решить свой вариант задачи, расположенный в файле с вариантами.

# Выполнение лабораторной работы

Ниже представлены скриншоты выполнения лабораторной работы

![Теория](image/theory.png){ #fig:001 width=85% }

![Вариант работы](image/var.png){ #fig:002 width=85% }

![Модель №1](image/matmod1.png){ #fig:003 width=85% }

![Модель №2](image/matmod2.png){ #fig:004 width=85% }

# Выводы

В ходе данной работы я ознакомился с моделью SIR и научился решать задачи, связанные с данной моделью.
