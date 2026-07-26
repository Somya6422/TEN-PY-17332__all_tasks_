try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please provide a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter numerical values only.")
