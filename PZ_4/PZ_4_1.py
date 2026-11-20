#Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...

a = float(input('a = '))
n = int(input('n = '))
e = 1.0
for _ in range(n):
    e *= a
print('a^n =', e)