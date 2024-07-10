def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average


def check_threshold(average, threshold):
    if average > threshold:
        print(f"The average {average:.2f} is greater than the threshold {threshold:.2f}.")
    else:
        print(f"The average {average:.2f} is less than or equal to the threshold {threshold:.2f}.")


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    threshold = float(input("Enter the threshold: "))

    average = calculate_average(num1, num2, num3)
    print(f"The average of the three numbers is {average:.2f}.")

    check_threshold(average, threshold)


if __name__ == "__main__":
    main()
