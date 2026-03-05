import re

def a(text):

    text = re.sub(r'\+84\d+', '[REDACTED]', text)

    text = re.sub(r'\d{10}', '[REDACTED]', text)
    return text

if __name__ == "__main__":
    print("Redact Phone Numbers")
    text = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321."
    redacted = a(text)
    print(f"Before: '{text}'")
    print(f"After: '{redacted}'")
