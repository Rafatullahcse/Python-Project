length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is {:.2f}".format(area))
print("The perimeter of the rectangle is {:.2f}".format(perimeter))
