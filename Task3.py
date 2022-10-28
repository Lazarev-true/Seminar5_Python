# Создайте программу для игры в "Крестики-нолики"

print('\nИгра "Крестики-нолики", нужно вводить две цифры через пробел, от 1 до 3\n')

from random import *

name = []
symbol = []
array = [''] * 3
for i in range(3):
    array[i] = [' '] * 3

symbol.append('O')
symbol.append('X')

name.append(input('Введите ваше имя - '))
name.append('computer')

gamer = randrange(2)
s = randrange(2)
print(f'\nНачинает игрок {name[gamer]} и ходит "{symbol[s]}"\n')

cell = 9

def motion(x, y):
    array[x - 1][y - 1] = symbol[s]

def fun(f):
    if f == 1:
        f = 0
    else:
        f += 1
    return f

while cell > 0:
    if gamer == 0:
        while True:
            x, y = map(int,input('Ваш ход - ').split())
            if x < 1 or y < 1 or y > 3 or x > 3:
                print('Такой клетки нет!')
            elif array[x - 1][y - 1] in 'XO':
                    print('Эта клетка уже занята!')
            else:
                motion(x, y)
                break
 
    if gamer == 1:
        print('Ходит computer')
        while True:
            x = randint(1, 3)
            y = randint(1, 3)
            if array[x - 1][y - 1] not in 'XO':
                motion(x, y)
                break

    

    print('-------------')
    for i in range(3):
        print(f'| {array[i][0]} | {array[i][1]} | {array[i][2]} |')
        print('-------------')

    for i in range(3):
        if (array[i][0] == array[i][1] and array[i][1] == array[i][2] and array[i][2] == 'X') \
            or (array[i][0] == array[i][1] and array[i][1] == array[i][2] and array[i][2] == 'O') \
            or (array[0][i] == array[1][i] and array[1][i] == array[2][i] and array[2][i] == 'X') \
            or (array[0][i] == array[1][i] and array[1][i] == array[2][i] and array[2][i] == 'O'):
            print(f'Выиграл игрок {name[gamer]}')
            exit()
    if (array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[2][2] == 'X') \
        or (array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[2][2] == 'O') \
        or (array[2][0] == array[1][1] and array[1][1] == array[0][2] and array[0][2] == 'X') \
        or (array[2][0] == array[1][1] and array[1][1] == array[0][2] and array[0][2] == 'O'):
        print(f'Выиграл игрок {name[gamer]}')
        exit()
    
    if cell == 1:
        print(f'Победила дружба!')
        exit()

    gamer = fun(gamer)
    s = fun(s)
   
    cell -= 1