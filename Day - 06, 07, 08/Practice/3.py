try:
    user_input = input("Please enter a number: ")
    number = float(user_input) 
    print(f"Success! You entered the number: {number}")
except ValueError:
    print("Error: Invalid input! You entered text instead of a number.")
