# C + D

from math import pi

def sIsTrue(r1, r2):
    s = pi * r2**2
    s -= pi * r1**2
    s /= 2  #  D + C справа
    s += r2**2
    s -= (pi * r1**2) / 4  #  + D слева
    return s

def monteCarlo(r2, n):
    points_inside = 0
    total_points = 0

    for i in range(n):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        if is_point_inside_circle(x, y, radius):
            points_inside += 1

        total_points += 1

    return (points_inside / total_points) * (4 * radius * radius)

r1 = 10
r2 = r1 * 2

s = sIsTrue(r1, r2)

