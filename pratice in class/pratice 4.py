fruit = 'banana'
print(fruit[0])
print(fruit[1])
print(fruit[2])


print(len(fruit))


index = 0 
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1


for letter in fruit :
    print(letter)