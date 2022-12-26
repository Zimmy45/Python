import sys
from random import randint
n = int(input("Из скольки чисел сгенерировать список? "))
if n == 1:
    sys.exit('Список слишком короткий - в нем только одна позиция и, соответсвенно, четная')
sum = 0
list_num = [randint(-100, 101) for i in range(n)]
print(list_num)
for i in range(1, n, 2):
    sum = sum + list_num[i]
print('Сумма элементов списка на нечетных позициях равна', sum)