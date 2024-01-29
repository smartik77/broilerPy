from math import fabs

r1 = 10
r2 = r1 * 2

while (True):
    x = float(input("Введите координату по х: "))
    y = float(input("Введите координату по y: "))

    # одиночные точки
    if (x**2 + y**2 < r1**2):
        print("Точка принадлежит области А\n")
    elif (x**2 + y**2 > r1**2 and x**2 + y**2 < r2**2 and x > 0 and y > 0):
        print("Точка принадлежит области D\n")
    elif (x**2 + y**2 > r1**2 and x**2 + y**2 < r2**2 and x > 0 and y < 0):
        print("Точка принадлежит области C\n")
    elif (x**2 + y**2 > r1**2 and x < 0 and y > 0 and fabs(x) < r2 and y < r2):
        print("Точка принадлежит области B\n")
    elif (x**2 + y**2 > r1**2 and x < 0 and y < 0 and fabs(x) < r2 and fabs(y) < r2):
        print("Точка принадлежит области D\n")
    # двойные точки на круге
    elif (x**2 + y**2 == r1**2 and x > 0 and y > 0):
        print("Точка принадлежит областям A и D\n")
    elif (x**2 + y**2 == r2**2 and x > 0 and y > 0):
        print("Точка принадлежит областям D и E\n")
    elif (x**2 + y**2 == r2**2 and x > 0 and y < 0):
        print("Точка принадлежит областям C и E\n")
    elif (x**2 + y**2 == r1**2 and x > 0 and y < 0):
        print("Точка принадлежит областям A и C\n")
    elif (x**2 + y**2 == r1**2 and x < 0 and y < 0 and x < r2 and y < r2):
        print("Точка принадлежит областям A и D\n")
    elif (x**2 + y**2 == r1**2 and x < 0 and y > 0 and x < r2 and y < r2):
        print("Точка принадлежит областям A и В\n")
    # двойные зоны вне круга
    elif (x == 0 and y > r1 and y < r2):
        print("Точка принадлежит областям B и D\n")
    elif (x == 0 and y < 0 and fabs(y) > r1 and fabs(y) < r2):
        print("Точка принадлежит областям D и C\n")
    elif (x < 0 and fabs(x) < r2 and fabs(x) > r1 and y == 0):
        print("Точка принадлежит областям B и D\n")
    elif (x > 0 and x < r2 and x > r1 and y == 0):
        print("Точка принадлежит областям D и C\n")
    # Тройные на круге
    elif (x == 0 and y == r1):
        print("Точка принадлежит областям A, B, D\n")
    elif (x == 0 and fabs(y) == r1 and y < 0):
        print("Точка принадлежит областям A, D, C\n")
    elif (y == 0 and x == r1):
        print("Точка принадлежит областям A, D, C\n")
    elif (y == 0 and fabs(x) == r1 and x < 0):
        print("Точка принадлежит областям A, B, D\n")
    # Тройные вне круга
    elif (x == 0 and y == r2):
        print("Точка принадлежит областям B, D, E\n")
    elif (x == 0 and fabs(y) == r2 and y < 0):
        print("Точка принадлежит областям D, C, E\n")
    elif (y == 0 and x == r2):
        print("Точка принадлежит областям D, C, E\n")
    elif (y == 0 and fabs(x) == r2 and x < 0):
        print("Точка принадлежит областям B, D, E\n")
    # двойные с Е
    elif (x**2 + y**2 == r2**2 and x > 0 and y > 0):
        print("Точка принадлежит областям D, E\n")
    elif (x**2 + y**2 == r2**2 and x > 0 and y < 0):
        print("Точка принадлежит областям C, E\n")
    elif (fabs(y) == r2 and x < 0 and y > 0 ):
        print("Точка принадлежит областям B, E\n")
    elif (fabs(x) == r2 and x < 0 and y > 0 ):
        print("Точка принадлежит областям B, E\n")
    elif (fabs(x) == r2 and x < 0 and y < 0 ):
        print("Точка принадлежит областям D, E\n")
    elif (fabs(y) == r2 and x < 0 and y < 0 ):
        print("Точка принадлежит областям D, E\n")
    else:
        print("Точка принадлежит области E\n")
