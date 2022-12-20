n = int(input('Введите число N: '))
array = []
factorial = 1
for i in range(1, n+1):
    factorial *= i 
    array.append(str(factorial))
print('[ '+', '.join(array)+' ]')
