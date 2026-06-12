# 14. Store marks of 10 students and display students scoring more than 75.
f = open("marks.txt", "w")
for _ in range(10):
    record = input("Enter Name,Marks: ")
    f.write(record + "\n")
f.close()

f = open("marks.txt", "r")
for line in f:
    name, marks = line.strip().split(",")
    if int(marks) > 75:
        print(name)
f.close()\n