number = [1,3,3,4,5,5,5,6,7]
unique = []
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)