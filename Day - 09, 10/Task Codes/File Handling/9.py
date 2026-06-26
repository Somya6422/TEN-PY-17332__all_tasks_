# 9. Count total vowels present in a file.
f = open("student.txt", "r")
data = f.read()
count = 0
for char in data:
    if char in "aeiouAEIOU":
        count += 1
print("Total vowels:", count)
f.close()\n