def validate(password):
    if len(password) < 6:
        return "Weak"
    elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
        return "Strong"
    return "Medium"
pwd = input("Enter password: ")
print(validate(pwd))
