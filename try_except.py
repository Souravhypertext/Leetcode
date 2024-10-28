try:
    age = int(input('Enter your age: '))
    income = int(input('Enter your income: '))
    risk = income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print('your age cannot be zero')
except ValueError:
    print('Enter an integer')