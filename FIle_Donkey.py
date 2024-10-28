words = ["Donkey", "is","work"]

with open("Donkey.txt", "r") as f:
    content = f.read()

for word in words:


    content = content.replace(word, "#"* len(words))

with open("Donkey.txt", "w") as f:
    f.write(content)