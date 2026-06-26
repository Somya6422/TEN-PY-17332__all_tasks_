# 3. Count total characters present in a file.
f = open("student.txt", "r")
data = f.read()
print("Total characters:", len(data))
f.close()\n