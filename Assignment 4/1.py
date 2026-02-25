numbers = []

while True:
    a = input("Enter a number: ")
    if a == "":
        break
    numbers.append(float(a))

numbers.sort(reverse=True)
greatest_five = numbers[:5]

print("\nThe five greatest numbers in descending order:")
for num in greatest_five:
    print(num)
