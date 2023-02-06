import random
a = [random.randint(-10,11) for i in range(1,21)]
print("Исходный рандомный список из 20 чисел от -10 до 10:")
print(a)
b = []
min = int(input("Задайте нижнюю гарницу диапазона: "))
max = int(input("Задайте нижнюю гарницу диапазона: "))
for indx,val in enumerate(a):
    if val>=min and val<=max:
        b.append(indx)
print("Значения, соответсвующие Вашему критерию, находятся на позициях со следующими индексами:")
print(b)