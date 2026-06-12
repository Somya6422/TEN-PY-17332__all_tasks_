# 6. Display file contents line by line using readline().
f = open("student.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()\n