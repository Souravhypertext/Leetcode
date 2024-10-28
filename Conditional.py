a = int(input("Enter your Age : "))

if a>18:
    print("you are above the age of consent ")
    print("you are fine:")

elif a<0:
    print("you are entering invalid age ")

elif a==0:
    print("Enter a valid age ")

else:
    print("you are below the age of consent ")