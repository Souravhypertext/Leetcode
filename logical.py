income = int(input("Enter your income: "))
is_good = bool(input("Is your good Credit: "))
if income > 100000 and is_good == True:
    print("you are Eligible")
else:
    print("you are not Eligible ")