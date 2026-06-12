# 29. Write a program to find sum of digits of a number.
n = int(input("Enter number: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)\n