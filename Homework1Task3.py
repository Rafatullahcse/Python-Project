# Get input from the user
minutes = int(input("Enter the number of minutes: "))

# Calculate the hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Print the results
print("{} minutes is equal to {} hours and {} minutes".format(minutes, hours, remaining_minutes))
