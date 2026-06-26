# 35. Write a program to count frequency of each character in a string.
s = input("Enter string: ")
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Frequencies:", freq)\n