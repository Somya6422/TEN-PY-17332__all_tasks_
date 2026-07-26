# 7. Add 3 new records to an existing file without deleting old data.
f = open("student.txt", "a")
for i in range(3):
    name = input("Enter new record: ")
    f.write(name + "\n")
f.close()\n