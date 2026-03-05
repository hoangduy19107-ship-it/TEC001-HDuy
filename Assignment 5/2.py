import re

def validate_hex_color(color):

    pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.match(pattern, color):
        return True
    else:
        return False

if __name__ == "__main__":
    print("Hex Color Validation")
    test_colors = ['#AF3739', '#abc123', '#FF57', 'FF5733', '#GGGGGG']
    for color in test_colors:
        print(f"'{color}': {validate_hex_color(color)}")
