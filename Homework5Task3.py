def convert_mph_to_kmh(mph):
    return mph * 1.60934


def convert_kmh_to_mph(kmh):
    return kmh / 1.60934


def compare_speeds(speed1, unit1, speed2, unit2):
    if unit1 == "kmh":
        speed1_kmh = speed1
        speed2_kmh = convert_mph_to_kmh(speed2) if unit2 == "mph" else speed2
    elif unit1 == "mph":
        speed1_kmh = convert_mph_to_kmh(speed1)
        speed2_kmh = convert_mph_to_kmh(speed2) if unit2 == "mph" else speed2
    else:
        raise ValueError("Invalid unit")

    if speed1_kmh > speed2_kmh:
        return f"{speed1} {unit1} is faster than {speed2} {unit2}"
    elif speed1_kmh < speed2_kmh:
        return f"{speed2} {unit2} is faster than {speed1} {unit1}"
    else:
        return f"{speed1} {unit1} and {speed2} {unit2} are the same speed"


def main():
    speed1 = float(input("Enter the first speed: "))
    unit1 = input("Enter the unit of the first speed (kmh or mph): ")
    speed2 = float(input("Enter the second speed: "))
    unit2 = input("Enter the unit of the second speed (kmh or mph): ")

    result = compare_speeds(speed1, unit1, speed2, unit2)
    print(result)


if __name__ == "__main__":
    main()
