# Реализуйте RLE алгоритм: реализуйте 
# модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся 
# в отдельных текстовых файлах

from itertools import groupby

f1 = open('Task4_1original.txt', 'r')
f2 = open('Task4_2original.txt', 'r')

str1Old = f1.read()
str2Old = f2.read()

f1.close()
f2.close()

str1New = ''.join([f'{x[0]}{"" if x[1] == 1 else x[1] and x[0] if x[1] == 2 else x[1]}'
            for x in [(i, len(list(j))) for i, j in groupby(str1Old)]])

print(str1Old)
print(str1New)

str2New = ''
count = ''
d = ''
for i in str2Old:
   index = str2Old.find(i)
   if index == len(str2Old) - 1 and not (i.isdigit()):
      str2New += i
   if not (d.isdigit()) and not (i.isdigit()):
      str2New += d
   if not (i.isdigit()):
      count = i
   else:
      str2New += int(i) * count
   d = i

print()
print(str2Old)
print(str2New)
