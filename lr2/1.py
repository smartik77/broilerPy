from random import uniform
from math import log, sin, fabs, tan

def f1(x):
    return log(x) + sin(x)

def f2(x):
    return fabs(tan(0.2 * x)) + x

def pointInFigure(x, y, a, b):
    return x >= a and y >= f1(x) and y <= f2(x) and x <= b

def monteCarlo(a, b, n):
    pointIsHit = 0

    width = b - a
    hight = findMaxY(dx, a, b) - findMinY(dx, a, b)
     
    for i in range(n):
        x = uniform(a, b)
        y = uniform(findMinY(dx, a, b), findMaxY(dx, a, b))
        
        if (pointInFigure(x, y, a, b)):
            pointIsHit += 1

    sSquare = width * hight

    return (pointIsHit / n) * sSquare

def findMinY(dx, a, b):
    minY = f1(a)
    y = a
    while (y <= b):
        if (minY > f1(y + dx)):
            minY = f1(y + dx)

        y += dx
    return minY

def findMaxY(dx, a, b):
    maxY = f2(a)
    y = a
    while (y <= b):
        if (maxY < f2(y + dx)):
            maxY = f2(y + dx)

        y += dx
    return maxY

def rectangleMethod(x, b, dx):
    s = 0
    while (x <= b):
        y1 = f1(x)
        y2 = f2(x)
        y = fabs(y1 - y2)

        ds = y * dx
        s += ds
        x += dx
    return s

def trapezoidMethod(x, b, dx):
    s = 0
    while (x <= b):
        y1 = f1(x)
        y1Next = f1(x + dx)
        
        y2 = f2(x)
        y2Next = f2(x + dx)
        
        ds1 = ((y1  + y1Next) / 2) * dx
        ds2 = ((y2 + y2Next) / 2) * dx
        s += fabs(ds1 - ds2)
        x += dx
    return s
    
while (True):
    variant = int(input("\nДля выбора метода интегрирования введите число(1 - метод прямоугольников, 2 - метод трапеций): "))
    a = float(input("Введите нижний предел интегрирования а: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    dx = float(input("Введите шаг интегрирования dx: "))
    n = int(input("Введите количество точек N: "))

    x = a
    s = 0

    if (variant == 1):  #  метод прямоугольников
        print(f"\nМетод прямоугольников: {rectangleMethod(x, b, dx)}")

    elif (variant == 2):  #  метод трапеций
        print(f"\nМетод трапеций: {trapezoidMethod(x, b, dx)}")
        
    else:
        continue
    
    print(f"Метод монте-карло: {monteCarlo(a, b, n)}\n")
