# 5. Count total words in a file.
f = open("student.txt", "r")
data = f.read()
words = data.split()
print("Total words:", len(words))
f.close()\n