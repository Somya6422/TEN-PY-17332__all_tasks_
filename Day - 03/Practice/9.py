correct_password = "python123"
for i in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
else:
    print("Account Locked")
