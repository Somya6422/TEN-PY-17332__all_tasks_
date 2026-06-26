def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
marks = int(input("Enter marks: "))
print("Grade:", grade(marks))
