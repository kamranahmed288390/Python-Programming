

def rem(l ,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Kamran", "Ahmed","Ali","Khan","an"]

print(rem(l,"an"))