with open("This.txt") as f:
    content1 = f.read()

with open("This_copy.txt") as f:
    content2 = f.read()


if content1 == content2:
    print("Yes this files are identical! ")

else:
    print("No this files are not identical! ")