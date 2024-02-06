from math import cos, sin, radians

m = float(input("Введите массу в килограммах: "))
degree = float(input("Введите угол: "))
f = float(input("Введите силу тяги: "))
k = float(input("Коэффицент трения: "))

# m = 100
# degree = 20
# f = 1000
# k = 0.1
g = 9.81

a = (f / m) - g * (k * cos(radians(degree)) + sin(radians(degree)))

print(f"Ускоение = {a} м/c**2")
