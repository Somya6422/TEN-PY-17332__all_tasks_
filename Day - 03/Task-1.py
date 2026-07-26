n = int(input("Enter a number: "))
# 1. Right Triangle of Stars
print("\n1. Right Triangle of Stars:\n")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Inverted Triangle of Numbers
print("\n2. Inverted Triangle of Numbers:\n")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3. Pascal Triangle
print("\n3. Pascal Triangle:\n")
for i in range(n):
    number = 1
    for space in range(n - i):
        print(" ", end="")
    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)
    print()

# 4. Prime Numbers up to n
print("\n4. Prime Numbers up to", n, ":\n")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
