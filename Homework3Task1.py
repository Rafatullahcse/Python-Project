def check_triangle(length1, length2, length3):
    if length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1:
        print("The side lengths can form a triangle.")

        if length1 == length2 == length3:
            print("The triangle is equilateral.")
        elif length1 == length2 or length1 == length3 or length2 == length3:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
    else:
        print("The side lengths cannot form a triangle.")


a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

check_triangle(a, b, c)
