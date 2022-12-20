s = input('Введите число: ')
sum = 0
for i in range(len(s)):
    if s[i] != '.' and s[i] != ',':
        sum = sum + int(s[i])
print('Сумма его цифр равна ',sum)