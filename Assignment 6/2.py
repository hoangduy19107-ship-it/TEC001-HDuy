seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")

month = int(input("Enter the number of the month (1-12): "))

if 1 <= month <= 12:
    print(f"The season for month {month} is {seasons[month-1]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
