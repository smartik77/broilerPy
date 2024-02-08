from math import fabs

# левая часть равенства
def f(x):
    return (x + 2) / (x**2 - 2 * x - 3)
    
while (True):
    x = float(input("Введите значение х в интервале (-1; 1): "))
    
    if (fabs(x) >= 1):
        print("\nНеверное значение х\n")
        continue
     
    eps = float(input("Введите погрешность е: "))

    n = 0
    resultSum = 0
    
    # правая часть неравенства
    while (eps <= (fabs(f(x) - resultSum))):

        resultSum += (((-1)**(n + 1) - (5 / 3**(n + 1))) * x**n) / 4

        n += 1

    print(f"\nЛевая часть равенства = {f(x)}")
    print(f"Правая часть равенства = {resultSum}\n")
