# 10. Count uppercase and lowercase characters separately.
f = open("student.txt", "r")
data = f.read()
upper = 0
lower = 0
for char in data:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"Uppercase: {upper}, Lowercase: {lower}")
f.close()\n