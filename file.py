f = open("file.txt")
content = f.read()
if "twinkle" in content:
    print("This word twinkle is present in content ")
else:
    print("this word twinkle is not present is content ")

f.close()
