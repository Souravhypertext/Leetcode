mark1 = int(input("Enter your marks in subject1 : "))
mark2 = int(input("Enter your marks in subject2 : "))
mark3 = int(input("Enter your marks in subject3 : "))

total_percentage = (100*(mark1+mark2+mark3))/300

if total_percentage>=40 and mark1 >=33 and mark2>=33 and mark3>=33:
    print("you are passed ", total_percentage)
else:
    print("you are failed, try next year again! ", total_percentage)