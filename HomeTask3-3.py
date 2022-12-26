import random
n = int(input("Из скольки чисел сгенерировать список? "))
list_result = []
list_num = [round(random.uniform(0, 11), 3) for i in range(n)]
print(list_num)
for i in range(n):
    list_result.append(round((list_num[i] - int(list_num[i])), 3))
print('Разница между максимальным и минимальным значениями дробных частей равна ', round(max(list_result) - min(list_result), 3))