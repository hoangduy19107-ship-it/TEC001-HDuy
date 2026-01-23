import math


def calculate_unit_price(diameter_cm, price_usd):
    diameter_m = diameter_cm / 100
    radius_m = diameter_m / 2
    area_m2 = math.pi * radius_m ** 2
    unit_price = price_usd / area_m2
    
    return unit_price


def compare_pizzas():
    try:
        print("Pizza 1:")
        diameter1 = float(input("Enter the diameter of pizza 1 in centimeters: "))
        price1 = float(input("Enter the price of pizza 1 in USD: "))
        
        print("\nPizza 2:")
        diameter2 = float(input("Enter the diameter of pizza 2 in centimeters: "))
        price2 = float(input("Enter the price of pizza 2 in USD: "))
        
        unit_price1 = calculate_unit_price(diameter1, price1)
        unit_price2 = calculate_unit_price(diameter2, price2)
        
        print(f"\nPizza 1 unit price: ${unit_price1:.2f} per square meter")
        print(f"Pizza 2 unit price: ${unit_price2:.2f} per square meter")
        
        if unit_price1 < unit_price2:
            print(f"\nPizza 1 provides better value for money!")
        elif unit_price2 < unit_price1:
            print(f"\nPizza 2 provides better value for money!")
        else:
            print(f"\nBoth pizzas provide the same value for money!")
            
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    compare_pizzas()
