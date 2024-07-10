def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    min_interest = float(input("Enter the minimum interest amount: "))

    interest = calculate_simple_interest(principal, rate, time)

    print(f"The simple interest is: {interest:.2f}")

    if interest > min_interest:
        print(f"The interest is above the minimum amount of {min_interest:.2f}.")
    else:
        print(f"The interest is below the minimum amount of {min_interest:.2f}.")


if __name__ == "__main__":
    main()
