# 13. Replace all occurrences of "Python" with "Programming".
f = open("student.txt", "r")
data = f.read()
f.close()
data = data.replace("Python", "Programming")
f = open("student.txt", "w")
f.write(data)
f.close()\n