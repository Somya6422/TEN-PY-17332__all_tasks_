# 33. Write a program to count vowels in a string.
s = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowels:", count)\n