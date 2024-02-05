from math import sin, radians

a = radians(float(input("Введите угол(в градусах): ")))
u0 = float(input("Введите начальную скорость полёта(в м/c): "))
g = 9.81

xMax = (u0**2 / g) * (sin(2 * a))
yMax = ((u0**2) * (sin(a)**2)) / (2 * g)

print(f"Дальность полета тела = {xMax} (м)")
print(f"Наибольшая высота подъема = {yMax} (м)")
