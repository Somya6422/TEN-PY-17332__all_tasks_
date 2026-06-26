# 20. Create Student Result File
f = open("results.txt", "w")
for _ in range(3):
    record = input("Enter Name,Phy,Chem,Maths: ")
    f.write(record + "\n")
f.close()

f = open("results.txt", "r")
max_marks = -1
topper = ""
for line in f:
    parts = line.strip().split(",")
    name = parts[0]
    total = int(parts[1]) + int(parts[2]) + int(parts[3])
    if total > max_marks:
        max_marks = total
        topper = name
print("Topper is:", topper, "with", max_marks, "marks")
f.close()\n