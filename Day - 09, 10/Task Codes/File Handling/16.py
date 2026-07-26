# 16. Count Blank Lines
f = open("student.txt", "r")
blank = 0
for line in f:
    if line.strip() == "":
        blank += 1
print("Blank lines:", blank)
f.close()\n