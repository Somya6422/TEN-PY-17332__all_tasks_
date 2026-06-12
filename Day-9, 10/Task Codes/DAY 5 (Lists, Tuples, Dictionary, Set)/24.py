# 24. Write a program to count even numbers in a list.
lst = [1, 2, 3, 4, 5, 6]
count = 0
for x in lst:
    if x % 2 == 0:
        count += 1
print("Even count:", count)\n