# 18. Display Lines Starting with a Vowel
f = open("student.txt", "r")
for line in f:
    stripped = line.strip()
    if stripped and stripped[0] in "aeiouAEIOU":
        print(stripped)
f.close()\n