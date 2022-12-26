from random import randint
n = int(input("Из скольки чисел сгенерировать список? "))
list_num = [randint(-100, 101) for i in range(n)]
list_result =[]
print(list_num)
for i in range(int(n/2)):
    list_result.append(list_num[i]*list_num[n-1-i])
if n%2 == 1:
    list_result.append(list_num[int(n/2)]*list_num[int(n/2)])
print('Произведение пар чисел будет выглядеть следующим образом')
print(list_result)