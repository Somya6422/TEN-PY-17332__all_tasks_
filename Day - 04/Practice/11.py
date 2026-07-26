def check_balance(balance):
    return balance
def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    return "Insufficient balance"
balance = 10000
amount = float(input("Enter amount to withdraw: "))
print("Remaining:", withdraw(balance, amount))
