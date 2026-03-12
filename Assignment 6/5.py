def evennum(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlist = evennum(list)

print(f"Your list: {list}")
print(f"Even numbers: {evenlist}")