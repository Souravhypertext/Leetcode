with open("log.txt") as f:
    lines= f.readlines()

line_no = 1

for line in lines:
    if "python" in line:
        print(f"Yes python is present in line_no.{line_no}")
        break
    line_no += 1

else:
        print("No python is not present! ")