# 26. Write a program to reverse a number.
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = (rev * 10) + (n % 10)
    n = n // 10
print("Reversed:", rev)\n