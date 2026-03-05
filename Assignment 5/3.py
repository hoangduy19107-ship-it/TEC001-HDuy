import re

def a(paragraph):

    numbers = re.findall(r'\d+', paragraph)
    total = sum(int(num) for num in numbers)
    return total

if __name__ == "__main__":
    print("Sum Numbers in Paragraph")
    paragraph = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
    result = a(paragraph)
    print(f"Input: '{paragraph}'")
    print(f"Output: {result}")
 