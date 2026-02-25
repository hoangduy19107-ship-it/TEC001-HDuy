cities = []

for i in range(5):
    city = input(f"Enter city {i + 1}: ")
    cities.append(city)

print("Your cities:")
for city in cities:
    print(city)
