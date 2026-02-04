MAX_ATTEMPTS = 5
attempts = 0

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "python" and password == "rules":
        print("Welcome")
        break

    attempts = attempts + 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect credentials. {remaining} attempts remaining.")
    else:
        print("Access denied")
