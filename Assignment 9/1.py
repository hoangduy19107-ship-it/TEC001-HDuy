def count_non_blank_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.strip(): 
                    count += 1
            return count
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    result = count_non_blank_lines(file_path)
    print(f"Number of non-blank lines: {result}")
