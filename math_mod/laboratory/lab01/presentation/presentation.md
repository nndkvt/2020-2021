---
## Front matter
lang: ru-RU
title: Презентация по первой лабораторной. Предмет - Математическое моделирование.
author: |
	Попов Олег Павлович\inst{1}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: NEC--2021, 11 Февраля -- 13 Февраля

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
mainfont: DejaVuSerif
romanfont: DejaVuSerif
sansfont: DejaVuSans
monofont: DejaVuSansMono
---

# Вкратце о git и github

## Что и зачем? (про git) (1/2)

- Git — распределённая система контроля версий, которая даёт возможность разработчикам отслеживать изменения в файлах и работать совместно с другими разработчиками.

- Разработана в 2005 году Линусом Торвальдсом, создателем Linux, для того, чтобы другие разработчики могли вносить свой вклад в ядро Linux.

- Большинство СКВ хранят информацию в виде списка изменений в файлах. Вместо этого, подход Git к хранению данных больше похож на набор снимков миниатюрной файловой системы.

## Что и зачем? (про git) (2/2)

- Каждый раз, когда вы сохраняете состояние своего проекта в Git, система запоминает, как выглядит каждый файл в этот момент, и сохраняет ссылку на этот снимок.

## Преимущества git (1/2)

- **Бесплатный и open-source**. Это значит, что его можно бесплатно скачать и вносить любые изменения в исходный код;

- **Небольшой и быстрый**. Он выполняет все операции локально, что увеличивает его скорость. Кроме того, Git локально сохраняет весь репозиторий в небольшой файл без потери качества данных;

- **Резервное копирование**. Git эффективен в хранении бэкапов, поэтому известно мало случаев, когда кто-то терял данные при использовании Git;

## Преимущества git (2/2)

- **Простое ветвление**. В других СКВ создание веток— утомительная и трудоёмкая задача, так как весь код копируется в новую ветку. В Git управление ветками реализовано гораздо проще и эффективнее.

## А что такое GitHub?

- GitHub — сервис онлайн-хостинга репозиториев, обладающий всеми функциями распределённого контроля версий и функциональностью управления исходным кодом.

- Обычно используется вместе с Git и даёт разработчикам возможность сохранять их код онлайн, а затем взаимодействовать с другими разработчиками в разных проектах.

# Основные команды git

## Основные команды настройки (1/3)

- *git init* - создает git репозиторий из каталога, в котором на данный момент находится user.

- *git remote add <repos name> <repos url>* - подключает локальный репозиторий к репозиторию, url которого указан в команде. Если нам надо изменить url репозитория, заменяем команду *add* на команду *set-url*.

- *git config --global user.name <name>* - настройка своего имени пользователя на github.

- *git config --global user.email <email>* - настройка своего адреса электронной почты, к которому привязан аккаунт github.

## Основные команды настройки (2/3)

- *git config --global core.autocrlf <true | input>* - git автоматически (*true*) конвертирует CRLF->LF при коммите и обратно LF->CRLF при выгрузке кода из репозитория на файловую систему (*true* используют в Windows, *input* - в Mac и Linux).

## Основные команды настройки (3/3)

- *git config --global core.safecrlf <true>* - отвержение необратимого преобразования lf<->crlf. Полезно, когда специфические бинарники похожие на текстовые файлы. *..core.safecrlf warn* - печать только предупреждение, но принимает необратимый переход.

- *git config --global core.quotepath off* - по умолчанию, git будет печатать не-ASCII символов в именах файлов в виде восьмеричных последовательностей. Чтобы избежать нечитаемых строк, устанавливается соответствующий флаг *off*.

## Основные команды взаимодействия с файлами (1/2)

- *mkdir <folder name>* - создание папки с именем *<folder name>*.

- *cd <folder name | - | ~>* - переход в дочернюю папку с именем *folder name* | переход в папку, в которой user находился *до* предыдущего перехода | переход в *корневую папку*

- *ls <options> <folder path>* - просмотр всех файлов папки. Если путь папки не указан, показывает файлы текущей папки.

- *git add <file name>* - создает файлы или индексирует их изменение в репозитории (***не сохраняет их при этом***).

- *git rm <file name>* - удаляет файл из репозитория.

## Основные команды взаимодействия с файлами (2/2)

- *git commit -m <commit>* - добавляет "коммит" ко всем файлам, добавленным в репозиторий через команду add.

- *git push -u <repos name> <branch>* - сохраняет все изменения, внесенные в репозиторий.

- *git status* - индексикация изменений.

- *git log* - выводит список изменений.

## Немного о Markdown

Markdown — облегчённый язык разметки, созданный с целью обозначения форматирования в простом тексте, с максимальным сохранением его читаемости человеком, и пригодный для машинного преобразования в языки для продвинутых публикаций (HTML, Rich Text и других).

## Синтаксис Markdown

Ниже представлен упорядоченный список


1. *#..# Заголовок*
2. > Это цитата.
3. *Италик*, **жирный**, ***жирный италик***
4. Ниже представлен неупорядоченный список
	- [это ссылка на Makefile](Makefile)
	- Текст в ^верхнем^ и ~нижнем~ регистрах
	- Формула: $\sin^2 (x) + \cos^2 (x) = 1$

## {.standout}

Спасибо за внимание