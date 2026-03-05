import re

def a(code):
   
    pattern = r'^[A-Z]{2,3}\d{3}$'
    if re.match(pattern, code):
        return True
    else:
        return False

if __name__ == "__main__":
    print("Course Code Validation")
    test_codes = ['TEC001', 'AU006', 'TECD01', 'te001', 'CS101']
    for code in test_codes:
        print(f"'{code}': {a(code)}")
