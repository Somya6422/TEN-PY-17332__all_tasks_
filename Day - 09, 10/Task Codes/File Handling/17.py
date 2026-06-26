# 17. Count Digits, Alphabets and Special Characters
f = open("student.txt", "r")
data = f.read()
digits = alphas = specials = 0
for char in data:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphas += 1
    elif char != "\n" and char != " ":
        specials += 1
print(f"Digits: {digits}, Alphas: {alphas}, Specials: {specials}")
f.close()\n