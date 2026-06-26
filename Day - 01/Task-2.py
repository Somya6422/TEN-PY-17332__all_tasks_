# Task 2

total_bill = float(input("Enter total bill amount: ₹"))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = (total_bill * tip_percent) / 100
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / people
remaining = total_bill % people
tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)
amount_per_person = round(amount_per_person, 2)
print("\n===== BILL SUMMARY =====")
print("Original Bill       : ₹",total_bill)
print("Tip Amount          : ₹",tip_amount)
print("Total with Tip      : ₹",total_with_tip)
print("Amount Per Person   : ₹",amount_per_person)
print("Bill Remainder (%)  : ₹",remaining)
print("========================")
