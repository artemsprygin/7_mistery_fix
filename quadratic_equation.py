import math


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    return (-b - math.sqrt(discriminant)) / 2 if discriminant >= 0 else None,\
           (-b + math.sqrt(discriminant)) / 2 if discriminant > 0 else None
