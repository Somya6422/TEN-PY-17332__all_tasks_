import json
import os
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'expenses.json')
def load_expenses():
    """Loads expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    description = input("Enter what the expense was for: ")
    try:
        amount = float(input("Enter the amount: $"))
        expenses.append({"description": description, "amount": amount})
        save_expenses(expenses)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for idx, exp in enumerate(expenses):
        print(f"[{idx + 1}] {exp['description']} - ${exp['amount']:.2f}")
    print("---------------------")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        choice = int(input("\nEnter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            deleted_item = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"✅ Deleted: {deleted_item['description']}")
        else:
            print("❌ Invalid expense number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def total_spending(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n💰 Total Spending: ${total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker CLI ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            total_spending(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
