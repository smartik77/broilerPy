import random
from math import log, sin, fabs, tan

def f1(x):
    return log(x) + sin(x)

def f2(x):
    return fabs(tan(0.2 * x)) + x

while (True):
    variant = int(input("Для выбора метода интегрирования введите число(1 - метод прямоугольников, 2 - метод трапеций, 0 - выход): "))
    a = float(input("Введите нижний предел интегрирования а: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    dx = float(input("Введите шаг интегрирования dx: \n"))
    # n = int(input("Введите количество точек N: "))

    x = a
    result = None

    if (variant == 1):  #  метод прямоугольников
        s = 0
        while (x <= b):
            y1 = f1(x)
            y2 = f2(x)
            y = fabs(y1 - y2)

            ds = y * dx
            s += ds
            x += dx

        result = s
        print(result)

    elif (variant == 2):  #  метод трапеций
        s = (fabs(f1(a) - f2(a)) + fabs(f1(b) - f2(b))) / 2

        n = 10  #  количество разрезов

        h = (b - a) / n

        while (n != 0):
            y1 = f1(x)
            y2 = f2(x)
            y = fabs(y1 - y2)

            ds = y * slices
            s += ds
            x += slices

        s *= slices
        result = s
        print(result)

    elif (variant == 0):
        break
    else:
        continue



