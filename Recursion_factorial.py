def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)


n = int(input("Enter your number : "))
print(f"the factorial of number is {factorial(n)}")
