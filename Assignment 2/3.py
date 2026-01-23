def check_hemoglobin():
    try:
        sex = input("Enter your biological sex (Female/Male): ").strip().lower()
        hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
        
        if sex == "female":
            min_normal = 117
            max_normal = 155
        elif sex == "male":
            min_normal = 134
            max_normal = 167
        else:
            print("Invalid sex input. Please enter 'Female' or 'Male'.")
            return
        
        if hemoglobin < min_normal:
            print(f"Your hemoglobin value is LOW. (Normal range for {sex}s: {min_normal}-{max_normal} g/l)")
        elif hemoglobin > max_normal:
            print(f"Your hemoglobin value is HIGH. (Normal range for {sex}s: {min_normal}-{max_normal} g/l)")
        else:
            print(f"Your hemoglobin value is NORMAL. (Normal range for {sex}s: {min_normal}-{max_normal} g/l)")
    except ValueError:
        print("Invalid input. Please enter a valid number for hemoglobin.")


if __name__ == "__main__":
    check_hemoglobin()
