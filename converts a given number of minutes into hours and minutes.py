minutes = int(input("Enter the number of minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("{} minutes is equal to {} hours and {} minutes".format(minutes, hours, remaining_minutes))
