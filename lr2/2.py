import func

while (True):
    variant = int(input("\nДля выбора метода интегрирования введите число(1 - метод прямоугольников, 2 - метод трапеций): "))
    a = float(input("Введите нижний предел интегрирования а: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    dx = float(input("Введите шаг интегрирования dx: "))
    n = int(input("Введите количество точек N: "))

    x = a
    s = 0

    if (variant == 1):  #  метод прямоугольников
        print(f"\nМетод прямоугольников: {func.rectangleMethod(x, b, dx)}")

    elif (variant == 2):  #  метод трапеций
        print(f"\nМетод трапеций: {func.trapezoidMethod(x, b, dx)}")
        
    else:
        continue
    
    print(f"Метод монте-карло: {func.monteCarlo(a, b, n, dx)}\n")
