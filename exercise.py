name = input("Enter your name: ")
character = len(name)
if character < 3:
    print("Your name is too short")
elif character > 50:
    print("Your name is too long")
else:
    print("Your name is good")