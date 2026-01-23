def check_zander_size():
    min_size = 42
    
    try:
        length = float(input("Enter the length of the zander in centimeters: "))
        
        if length >= min_size:
            print(f"The zander meets the size limit! Length: {length} cm")
        else:
            difference = min_size - length
            print(f"The zander does not meet the size limit.")
            print(f"Please release the fish back into the lake.")
            print(f"The caught fish is {difference} cm below the size limit.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    check_zander_size()
