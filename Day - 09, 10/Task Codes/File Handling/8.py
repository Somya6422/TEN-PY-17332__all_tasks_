# 8. Check whether a given word exists in a file.
word = input("Enter word to search: ")
f = open("student.txt", "r")
data = f.read()
if word in data:
    print("Word exists")
else:
    print("Word does not exist")
f.close()\n