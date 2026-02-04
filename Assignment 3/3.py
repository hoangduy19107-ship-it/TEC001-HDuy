largestnum = None
smallestnum = None
while True:
    s = input("Enter a number: ")
    if s == "":
        break
    try:
        num = float(s)
    except ValueError:
        print("Invalid input. Please enter a numeric value or press Enter to quit.")

    if smallestnum is None or num < smallestnum:
        smallestnum = num
    if largestnum is None or num > largestnum:
        largestnum = num

if smallestnum is None:
    print("No numbers were entered.")
else:
    print(f"Smallest: {smallestnum}")
    print(f"Largest: {largestnum}")