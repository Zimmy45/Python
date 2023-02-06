print("Введите два числа - А и B")
A = int(input("A = "))
B = int(input("B = "))
r=1
while B > 0:
    r*=A
    B-=1
print("A в степени B равно ",r)