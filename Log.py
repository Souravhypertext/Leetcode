with open("log.txt") as f:
    content = f.read()

if "python" in content :
    print("Yes python is present in text! ")

else:
    print("No python is not present is text! ")
