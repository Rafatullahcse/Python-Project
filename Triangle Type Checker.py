import math


def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"


def angle_type(a, b, c):
    angles = [math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)),
              math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)),
              math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))]
    angles_deg = [math.degrees(angle) for angle in angles]
    if max(angles_deg) > 90:
        return "Obtuse"
    elif max(angles_deg) == 90:
        return "Right-angled"
    else:
        return "Acute"


def main():
    a = float(input("Enter the first side length: "))
    b = float(input("Enter the second side length: "))
    c = float(input("Enter the third side length: "))

    if is_valid_triangle(a, b, c):
        print("The sides form a valid triangle.")
        print(f"Triangle type: {triangle_type(a, b, c)}")
        print(f"Angle type: {angle_type(a, b, c)}")
    else:
        print("The sides do not form a valid triangle.")


if __name__ == "__main__":
    main()
