word = "Animal"

with open("file.txt","r") as f:
    contant = f.read()

contentNew = contant.replace("Animal","######")

with open("file.txt","w") as f:
    f.write(contentNew)