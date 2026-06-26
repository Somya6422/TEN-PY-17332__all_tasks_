# 12. Copy content of one file to another.
f1 = open("student.txt", "r")
f2 = open("student_copy.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()\n