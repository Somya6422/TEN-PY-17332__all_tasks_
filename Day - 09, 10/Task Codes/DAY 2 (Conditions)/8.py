# 8. Write a program to find the largest among three numbers.
x = float(input("Enter first: "))
y = float(input("Enter second: "))
z = float(input("Enter third: "))
if x >= y and x >= z:
    print(x, "is largest")
elif y >= x and y >= z:
    print(y, "is largest")
else:
    print(z, "is largest")\n