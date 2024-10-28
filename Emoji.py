message = input("<")
words = message.split(' ')
emo = {
    ":)": "😊",
    ":(": "😔"
}
output = " "
for i in words:
     output += emo.get(i, i) + " "
print(output)