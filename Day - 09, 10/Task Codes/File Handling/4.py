# 4. Count total number of lines in a file.
f = open("student.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
f.close()\n