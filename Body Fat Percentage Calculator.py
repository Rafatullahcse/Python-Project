def calculate_body_fat_percentage(weight, body_fat_weight):
    body_fat_percentage = (body_fat_weight / weight) * 100
    return body_fat_percentage


def determine_health_range(body_fat_percentage):
    if body_fat_percentage < 10:
        return "Essential Fat (Athlete)"
    elif 10 <= body_fat_percentage < 15:
        return "Fitness"
    elif 15 <= body_fat_percentage < 20:
        return "Average"
    elif 20 <= body_fat_percentage < 25:
        return "Obese"
    else:
        return "Extremely Obese"


def main():
    weight = float(input("Enter your weight (in kg): "))
    body_fat_weight = float(input("Enter your body fat weight (in kg): "))

    body_fat_percentage = calculate_body_fat_percentage(weight, body_fat_weight)

    print(f"Your body fat percentage is: {body_fat_percentage:.2f}%")
    print(f"Your health range is: {determine_health_range(body_fat_percentage)}")


if __name__ == "__main__":
    main()
