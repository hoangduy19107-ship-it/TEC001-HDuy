numb = int(input("Enter an integer: "))

if numb < 2:
    print(f"{numb} is not a prime number.")
else:
    is_prime = True
    for i in range(2, numb):
        if numb % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{numb} is a prime number.")
    else:
        print(f"{numb} is not a prime number.")
