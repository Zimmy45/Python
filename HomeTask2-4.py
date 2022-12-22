import sys
N = int(input('Сколько элементов будет в списке? '))
list = []
count  = 0 # счетчик для ввода элементов списка
for i in range(-N, N+1): # формирование списка
    list.insert(count, i)
    count = count + 1
print(list) # вывод списка для визуализации
p = 1 # начальное произведение
data = open('positions.txt', 'r') # читаем данные из файла
for line in data:
    if int(line) < -N or int(line) > N:
        sys.exit("Следующей позиции из файла нет в этом списке")
    print(line)
    p = p*int(line)
data.close()
print('Произведение элементов списка в позициях из файла составляет ', p)