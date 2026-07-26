def salary(basic):
    hra = 0.2 * basic
    da = 0.1 * basic
    return basic + hra + da
basic = float(input("Enter basic salary: "))
print("Total Salary:", salary(basic))
