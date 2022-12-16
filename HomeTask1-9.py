v = int(input('Введите четверть на плоскости V: '))
if v == 1:
    print("x > 0; y > 0")
elif v == 2:
    print("x < 0; y > 0")
elif v == 3:
    print("x < 0; y < 0")
else:
     print("x > 0; y < 0")