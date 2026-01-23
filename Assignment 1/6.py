import math
x = float(input("Talent: "))
y = float(input("Pound: "))
z = float(input("Lot: "))

total_lots = (x * 20 * 32) + (y * 32) + z
total_grams = total_lots * 13.3

Kilograms = total_grams / 1000
Grams = total_grams % 1000

print("The weight in modern units:")
print(Kilograms,  "Kilograms and", Grams, "Grams")