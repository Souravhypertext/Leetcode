def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Sourav","Ruchika","Adarsh","Gourav","Himanshu","shweta"]
print(rem(l,"a"))