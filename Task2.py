# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import *

print('''Режимы:
1 - несколько игроков
2 - против компьютера
3 - умный компьютер''')

N = int(input('Введите режим - '))

candies = 2021
name = []

def rnd():
    gamer = randrange(len(name))
    print(f'\nНачинает игрок {name[gamer]}')
    return(gamer)

def win(candies):
    if candies == 0:
        print(f'Игрок {name[gamer]} победил!')
        quit()
    print(f'Осталось {candies} шт.')
    return candies

def G(gamer):
    if gamer == len(name) - 1:
        gamer = 0
    else:
        gamer += 1
    return gamer

def rules(candies):
    while True:
        took = input(f'\nСколько конфет берёт игрок {name[gamer]}? - ')
        if not (took.isdigit()):
            print('Неверный ввод')
        else:
            took = int(took)
            if took == 0:
                print('Нужно взять конфеты')
            elif took > candies:
                print('Нельзя взять больше конфет, чем осталось')
            elif took > 28:
                print('За один ход можно взять не более, чем 28 конфет')
            else:
                candies -= took
                return candies

if N == 1:
    n = int(input('Введите количество игроков - '))

    for i in range(n):
        name.append(input (f'Введите имя {i + 1}-ого игрока: '))

    gamer = rnd()

    while candies > 0:
        for i in range(len(name)):
            candies = rules(candies)
            candies = win(candies)
            gamer = G(gamer)

elif N == 2 or N == 3:
    name.append(input (f'Введите ваше имя: '))
    name.append('computer')

    gamer = rnd()

    while candies > 0:
        if gamer == 0:
            candies = rules(candies)
            candies = win(candies)
            gamer = G(gamer)
        else:
            if N == 2:
                if gamer == 1:
                    if candies < 29:
                        comp = randint(1, candies)
                    else:
                        comp = randint(1, 28)
                    print(f'\nКомпьютер взял {comp} шт.')
                    candies -= comp
                    candies = win(candies)
                    gamer = G(gamer)

            else:
                if gamer == 1:
                    if candies <= 28:
                        comp = candies
                    elif candies <= 56 and candies != 29:
                        comp = candies - 29
                    else:
                        if candies < 29:
                            comp = randint(1, candies)
                        else:
                            comp = randint(1, 28)
                    print(f'\nКомпьютер взял {comp} шт.')
                    candies -= comp
                    candies = win(candies)
                    gamer = G(gamer)
else:
    print('Нет такого режима!')