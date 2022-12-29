from random import randint
import sys
k = int(input('Введите степень многочлена k: '))
list_koeffic = [randint(0, 101) for i in range(k+1)]
if k == 0: sys.exit('Не существует такого многочлена')
print()
multi = str(' = 0')
for i in range(0,k+1):
    if i == 0 and list_koeffic[i] == 0: multi = '' + multi
    elif i == 0 and list_koeffic[i] != 0: multi = ' + ' + str(list_koeffic[i]) + multi
    elif i == 1 and list_koeffic[i] == 0: multi = ''+ multi
    elif i == 1 and list_koeffic[i] == 1: multi = 'x'+ multi
    elif i == 1 and list_koeffic[i] > 1: multi = str(list_koeffic[i]) +'x'+ multi
    elif i > 1 and list_koeffic[i] == 0: multi = '' + multi
    elif i > 1 and list_koeffic[i] == 1: multi = 'x**'+str(i) +' + ' + multi
    elif i > 1 and list_koeffic[i] > 1: multi = str(list_koeffic[i])+'x**'+str(i) +' + ' + multi
print(multi)
print('Этот же результат записан в файл mnogochlen.txt. Проверьте.')
f = open('mnogochlen.txt', 'w')
f.write(multi)
f.close()