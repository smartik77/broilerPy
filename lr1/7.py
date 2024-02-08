from math import fabs

def f(x):
    return (x + 2) / (x**2 - 2 * x - 3)
    
while (True):
    x1 = float(input("\nВведите значение х1: "))
    x2 = float(input("Введите значение х2: "))
   
    if (fabs(x1) >= 1 or fabs(x2) >= 1):
        print("\nУказаны неверные значения х\n")
        continue
    
    eps = float(input("Введите погрешность е: "))

    if (eps <= 0):
        print("\nУказано неверное значени е\n")
        continue
    
    dx = float(input("Введите шаг dx: "))
    
    if (dx <= 0):
        print("\nУказано неверное значение dx\n")
        continue
    
    n = 0
    resultSum = 0
    resultLeft = f(x1)
    
    print("dх    леваяЧасть    праваяЧасть")
    while (x1 <= x2):
        
        while (eps <= fabs(resultLeft - resultSum)):
            resultSum += (((-1)**(n + 1) - (5 / 3**(n + 1))) * x1**n) / 4
            n += 1

        print(f"{x1:g}    {f(x1):g}    {resultSum:g}")
        x1 += dx
