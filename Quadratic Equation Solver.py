import math


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Real and distinct roots: x1 = {root1:.2f}, x2 = {root2:.2f}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Real and equal roots: x = {root:.2f}"
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        return f"Complex roots: x1 = {real_part:.2f} + {imag_part:.2f}i, x2 = {real_part:.2f} - {imag_part:.2f}i"


def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    result = solve_quadratic(a, b, c)
    print(result)


if __name__ == "__main__":
    main()
