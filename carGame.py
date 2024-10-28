command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Already started")
        else:
            started = True
            print("Car is Start! ")
    elif command == "stop":
        if not started:
            print("Already stopped")
        else:
            started = False
            print("Car is Stopped! ")
    elif command == "help":
        print("""
 Start -> To start the car 
 Stop -> To stop the car
 quit -> To quit the car
        """)
    elif command == "quit" :
        print("Car is Quitted! ")
        break
    else:
        print("Sorry, I didn't understand that. Please try again.")