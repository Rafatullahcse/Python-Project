def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def compare_temperatures(temp1, unit1, temp2, unit2):
    if unit1 == "C" and unit2 == "F":
        temp1_f = celsius_to_fahrenheit(temp1)
        if temp1_f == temp2:
            return True
        else:
            return False
    elif unit1 == "F" and unit2 == "C":
        temp2_c = fahrenheit_to_celsius(temp2)
        if temp1 == temp2_c:
            return True
        else:
            return False
    else:
        if temp1 == temp2:
            return True
        else:
            return False


def main():
    temp1 = float(input("Enter the first temperature: "))
    unit1 = input("Enter the unit of the first temperature (C/F): ")
    temp2 = float(input("Enter the second temperature: "))
    unit2 = input("Enter the unit of the second temperature (C/F): ")

    if compare_temperatures(temp1, unit1, temp2, unit2):
        print("The two temperatures are the same.")
    else:
        print("The two temperatures are not the same.")


if __name__ == "__main__":
    main()
