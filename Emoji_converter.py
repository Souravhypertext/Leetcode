def emoji_converter(message):
    words = message.split(' ')
    emo = {
        ":)": "😊",
        ":(": "😔"
    }
    output = " "
    for i in words:
        output += emo.get(i, i) + " "
    return output


message = input("<")
print(emoji_converter(message))