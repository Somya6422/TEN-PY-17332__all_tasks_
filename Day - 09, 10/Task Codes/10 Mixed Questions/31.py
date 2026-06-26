# 31. Write a program to check whether a number is prime.
num = int(input("Enter number: "))
is_prime = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False
print("Prime" if is_prime else "Not Prime")\n