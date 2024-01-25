from math import sqrt, tan, sin, cos, log, fabs

a = float(input("Введите а: "))
b = float(input("Введите b: "))

fx = None

while (True):
    x = float(input("Введите x: "))

    if (x <= a):
        if (x < 0):
            fx = sqrt(-x) * cos(x)
        else:
            print("Ошибка, коклюш")
            continue
    elif (a < x < b):
        fx = fabs(tan(0.2 * x)) + x
    else:
        fx = log(x) + sin(x)

    print(f"f(x) = {fx}\n")
