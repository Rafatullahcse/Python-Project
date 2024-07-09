def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("The side lengths can form a triangle.")

        if a == b == c:
            print("The triangle is equilateral.")
        elif a == b or a == c or b == c:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
    else:
        print("The side lengths cannot form a triangle.")


a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

check_triangle(a, b, c)
