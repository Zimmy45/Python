import math
n = int(input('Сколько чисел будет в последовательности? '))
list = []
for i in range(n):
    x = int(input('Введите элемент последовательности - '))
    list.append(x)
a = set(list)
print()
print('Список неповторяющихся элементов последовательности:')
print(a)