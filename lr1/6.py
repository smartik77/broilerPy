from math import fabs

def f(x):
    return (x + 2) / (x**2 - 2 * x - 3)

def summ(x, eps):
    resultSum = 0
    n = 0
    while (eps >= fabs(resultSum)):

        resultSum += (((-1)**(n + 1) - (5 / 3**(n + 1))) * x**n) / 4

        n += 1
    return resultSum


while (True):
    x = float(input("Введите значение х в интервале (-1; 1): "))
    
    if (fabs(x) >= 1):
        print("\nНеверное значение х\n")
        continue
    
    eps = float(input("Введите погрешность е: "))

    print(f"Левая часть равенства = {f(x)}")
    print(f"Правая часть равенства = {summ(x, eps)}")

