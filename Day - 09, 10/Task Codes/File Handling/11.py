# 11. Find the longest line in a text file.
f = open("student.txt", "r")
lines = f.readlines()
longest = ""
for line in lines:
    if len(line) > len(longest):
        longest = line
print("Longest line:", longest.strip())
f.close()\n