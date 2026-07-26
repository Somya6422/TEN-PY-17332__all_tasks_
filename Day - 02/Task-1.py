print("===== LOAN ELIGIBILITY CHECKER =====")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: ₹"))
employment = input("Enter employment type (salaried/self-employed): ").strip().lower()

if age < 21 or age > 60:
    print("❌ Loan Rejected: Age should be between 21 and 60.")
elif salary < 25000:
    print("❌ Loan Rejected: Minimum salary required is ₹25,000.")
elif employment not in ["salaried", "self-employed"]:
    print("❌ Invalid employment type entered.")
elif 21 <= age <= 30 and salary < 30000:
    print("⚠ Loan Status: Needs Guarantor")
elif age > 55 and employment == "self-employed":
    print("⚠ Loan Status: High Risk — Senior Review Needed")
else:
    print("✅ Loan Approved")
