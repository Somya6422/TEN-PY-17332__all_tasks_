# 28. Write a program to count digits in a number.
n = int(input("Enter number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits:", count)\n