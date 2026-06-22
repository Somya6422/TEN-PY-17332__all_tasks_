from datetime import datetime
from collections import Counter

class InvalidNumberError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass

class SecureCalculator:
    def __init__(self):
        self.history_file = "calculation_history.txt"
        self.error_file = "error_log.txt"

    def get_number(self, message):
        while True:
            try:
                value = input(message)
                if value.strip() == "":
                    raise InvalidNumberError("Input cannot be empty.")
                return float(value)
            except ValueError:
                print("Invalid input. Enter a valid number.")
            except InvalidNumberError as e:
                print(e)

    def save_history(self, record):
        with open(self.history_file, "a") as file:
            file.write(record + "\n")

    def log_error(self, error_message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.error_file, "a") as file:
            file.write(f"[{timestamp}] {error_message}\n")

    def calculate(self):
        try:
            print("Operations")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Choose operation: ")
            if choice not in ["1", "2", "3", "4"]:
                raise ValueError("Invalid operation selected.")

            num1 = self.get_number("Enter first number: ")
            num2 = self.get_number("Enter second number: ")

            if choice == "1":
                result = num1 + num2
                expression = f"{num1} + {num2} = {result}"
            elif choice == "2":
                result = num1 - num2
                expression = f"{num1} - {num2} = {result}"
            elif choice == "3":
                result = num1 * num2
                expression = f"{num1} * {num2} = {result}"
            else:
                if num2 == 0:
                    raise DivisionByZeroError("Division by zero is not allowed.")
                result = num1 / num2
                expression = f"{num1} / {num2} = {result}"

        except DivisionByZeroError as e:
            print("Error:", e)
            self.log_error(str(e))
        except ValueError as e:
            print("Error:", e)
            self.log_error(str(e))
        except Exception as e:
            print("Unexpected Error:", e)
            self.log_error(str(e))
        else:
            print("Result =", result)
            self.save_history(expression)
        finally:
            print("Calculation process completed.")

    def view_history(self):
        try:
            with open(self.history_file, "r") as file:
                data = file.read()
                print(data if data else "No history available.")
        except FileNotFoundError:
            print("History file not found.")

    def view_errors(self):
        try:
            with open(self.error_file, "r") as file:
                data = file.read()
                print(data if data else "No errors recorded.")
        except FileNotFoundError:
            print("Error log file not found.")

    def generate_report(self):
        total_calculations = 0
        total_errors = 0
        common_error = "No Errors"

        try:
            with open(self.history_file, "r") as file:
                total_calculations = len(file.readlines())
        except FileNotFoundError:
            pass

        try:
            with open(self.error_file, "r") as file:
                errors = file.readlines()
                total_errors = len(errors)
                if errors:
                    types = []
                    for e in errors:
                        if "Division by zero" in e:
                            types.append("Division By Zero")
                        elif "Invalid operation" in e:
                            types.append("Invalid Operation")
                        else:
                            types.append("Other Error")
                    common_error = Counter(types).most_common(1)[0][0]
        except FileNotFoundError:
            pass

        report = (
            "====================\n"
            "   SUMMARY REPORT\n"
            "====================\n"
            f"Total Calculations : {total_calculations}\n"
            f"Total Errors       : {total_errors}\n"
            f"Most Common Error  : {common_error}\n"
            "====================\n"
        )

        with open("summary_report.txt", "w") as file:
            file.write(report)

        print(report)
def main():
    calc = SecureCalculator()
    while True:
        print("===============================")
        print("|    SECURE CALCULATOR PRO    |")
        print("===============================")
        print("| 1. Perform Calculation      |")
        print("| 2. View Calculation History |")
        print("| 3. View Error Report        |")
        print("| 4. Generate Summary Report  |")
        print("| 5. Exit                     |")
        print("===============================")


        choice = input("Enter choice: ")

        if choice == "1":
            calc.calculate()
        elif choice == "2":
            calc.view_history()
        elif choice == "3":
            calc.view_errors()
        elif choice == "4":
            calc.generate_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
