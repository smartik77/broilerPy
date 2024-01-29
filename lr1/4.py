# C + D
from math import pi, fabs
from random import uniform

def sIsTrue(r1, r2):
    s = pi * r2**2
    s -= pi * r1**2
    s /= 2  #  D + C справа
    s += r2**2
    s -= (pi * r1**2) / 4  #  + D слева
    return s

def monteCarlo(r1, r2, n):
    pointIsHit = 0

    for i in range(n):
        x = uniform(-r2, r2)
        y = uniform(-r2, r2)
        
        if (x**2 + y**2 > r1**2 and x**2 + y**2 < r2**2 and x > 0 and y > 0):  #  D справа
            pointIsHit += 1
        elif (x**2 + y**2 > r1**2 and x**2 + y**2 < r2**2 and x > 0 and y < 0):  #  С
            pointIsHit += 1
        elif (x**2 + y**2 > r1**2 and x < 0 and y < 0 and fabs(x) < r2 and fabs(y) < r2):  #  D слева
            pointIsHit += 1

    pointIsHit += 1
    sSquare = r2**2 * 4

    return (pointIsHit / n) * sSquare

r1 = 10
r2 = r1 * 2

s = sIsTrue(r1, r2)

while (True):
    n = int(input("Введите количество точек N: "))
    print(f"Метод Монте-Карло: {monteCarlo(r1, r2, n)} кв. ед.")
    print(f"Точное значение: {s} кв. ед.\n")
