import random
a = random.randint(1,100)
line = input("Guess the number between 1 and 100: ")
while True:
    guess = int(line)
    if guess < a:
        print("Too low!")
    elif guess > a:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
        break
    line = input("Try again: ") 