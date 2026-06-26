# 22. Write a program to find largest element in a list.
lst = [10, 45, 2, 99, 34]
max_val = lst[0]
for x in lst:
    if x > max_val:
        max_val = x
print("Largest:", max_val)\n