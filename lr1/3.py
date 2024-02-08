from math import tan, fabs

def f(x):
    return fabs(tan(0.2 * x)) + x

while (True):
    a = float(input("Введите нижний предел интегрирования a: "))
    b = float(input("Введите верхний предел интегрирования b: "))
    dx = float(input("Введите шаг интегрирования dx: "))

    s = 0
    x = a

    # метод прямоугольников
    while x <= b:
        y = f(x)
        ds = y * dx
        s += ds
        x += dx

    print(f"Значение интеграла = {fabs(s)}\n")
