def bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100*1.5 + (units-100)*2.5
    else:
        return 100*1.5 + 100*2.5 + (units-200)*4
units = int(input("Enter units: "))
print("Bill:", bill(units))
