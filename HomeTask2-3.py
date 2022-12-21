n = int(input('Из скольки чисел будет состоять список? _ '))
d = {a: round((1+1/a)**a, 2) for a in range(1,n+1)}
print(d)