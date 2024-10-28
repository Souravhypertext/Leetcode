weight=float(input("Enter your weight: "))
unit = input("(L)lbs ,(K)kg: ")
if unit.upper() == "K":
       converted = weight * 2.2046
       print(f"Your weight is {converted} Pounds")
else:
      converted = weight*0.45
      print(f"Your weight is {converted} kilos ")