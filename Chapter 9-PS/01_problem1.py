f = open("poem.txt")

c = f.read()

if ("twinkle" in c):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()