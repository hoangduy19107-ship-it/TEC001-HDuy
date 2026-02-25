def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

list = [2, 4, 6, 8, 10]
a= sum_of_list(list)

print(f"The list: {list}")
print(f"The total: {a}")
