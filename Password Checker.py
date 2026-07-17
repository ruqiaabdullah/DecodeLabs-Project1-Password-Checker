# Password Strength Checker
# DecodeLabs Cyber Security Internship - Project 1 (Batch 2026)

common_passwords = ["password", "123456", "qwerty", "abc123", "password123"]

def check_password_strength(password):
    # Check 1: Commonly leaked passwords
    if password.lower() in common_passwords:
        return "WEAK (This is a commonly leaked password!)"

    # Check 2: Length verification (Gatekeeper rule: < 8 = immediate fail)
    if len(password) < 8:
        return "WEAK (Password must be at least 8 characters)"

    # Check 3-5: Pythonic checks using any()
    has_upper  = any(char.isupper() for char in password)
    has_digit  = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Score-based risk classification
    score = sum([has_upper, has_digit, has_symbol])

    if score == 3:
        return "STRONG"
    elif score == 2:
        return "MEDIUM"
    else:
        return "WEAK"

# Main program
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)

# Improvement tips
if "WEAK" in result or "MEDIUM" in result:
    print("\nTips to improve:")
    if not any(c.isupper() for c in password):
        print("- Add an uppercase letter (A-Z)")
    if not any(c.isdigit() for c in password):
        print("- Add a number (0-9)")
    if not any(not c.isalnum() for c in password):
        print("- Add a symbol (!, @, #, etc.)")
