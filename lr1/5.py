from random import uniform
from math import log, sin, fabs, tan

def f1(x):
    return log(x) + sin(x)

def f2(x):
    return fabs(tan(0.2 * x)) + x

def monteCarlo(a, b, n):
    pointIsHit = 0
    side = b - a
    
    for i in range(n):
        x = uniform(-side / 2, side / 2)
        y = uniform(-side / 2, side / 2)
        
        if (x >= a and y >= f1(y) and y <= f2(y)):
            pointIsHit += 1

    sSquare = side**2

    return (pointIsHit / n) * sSquare


while (True):
    variant = int(input("Для выбора метода интегрирования введите число(1 - метод прямоугольников, 2 - метод трапеций, 0 - выход): "))
    a = float(input("Введите нижний предел интегрирования а: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    dx = float(input("Введите шаг интегрирования dx: "))
    n = int(input("Введите количество точек N: \n"))

    x = a
    s = 0

    if (variant == 1):  #  метод прямоугольников

        while (x <= b):
            y1 = f1(x)
            y2 = f2(x)
            y = fabs(y1 - y2)

            ds = y * dx
            s += ds
            x += dx
        print(s)

    elif (variant == 2):  #  метод трапеций

        while (x <= b):
            y1 = f1(x)
            y1Next = f1(x + dx)
            
            y2 = f2(x)
            y2Next = f2(x + dx)
            
            ds1 = ((y1  + y1Next) / 2) * dx
            ds2 = ((y2 + y2Next) / 2) * dx
            s += fabs(ds1 - ds2)
            x += dx
        print(s)

    elif (variant == 0):
        break
    else:
        continue
    
    print(monteCarlo(a, b, n))
    
    
