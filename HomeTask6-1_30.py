a1 = int(input("Введите первый элемент прогрессии a1: "))
d = int(input("Введите разность d: "))
n = int(input("введите количество элементов n: "))
a = [(a1+(i-1)*d) for i in range(1,n+1)]
print(" ".join(map(str,a)))