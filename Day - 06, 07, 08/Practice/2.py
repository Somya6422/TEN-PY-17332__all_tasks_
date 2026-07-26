filename = input("Enter the filename to open (e.g., data.txt): ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the spelling and try again.")
