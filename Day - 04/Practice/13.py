def can_vote(age):
    return "Eligible" if age >= 18 else "Not Eligible"
age = int(input("Enter age: "))
print(can_vote(age))
