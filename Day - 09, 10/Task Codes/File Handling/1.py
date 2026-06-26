# 1. Create a file student.txt and store 5 student names entered by the user.
f = open("student.txt", "w")
for i in range(5):
    name = input("Enter name: ")
    f.write(name + "\n")
f.close()\n