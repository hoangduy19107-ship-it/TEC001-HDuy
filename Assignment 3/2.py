while True:
    try:
        inches = float(input("Enter value in inches: "))
        print(f"{inches} inches is {inches * 2.54} centimeters.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
    if inches < 0:
        print("Negative value entered. Stopping.")
        break
