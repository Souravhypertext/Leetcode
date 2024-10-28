number = int(input("Enter your number : "))

for i in range(2, number):
    if number%i == 0:
        print("Your number is not prime ")
        break

else:
    print("Your number is prime")