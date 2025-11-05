import re

words = ["Animal", "bad", "smell"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = re.sub(word, "#" * len(word), content, flags=re.IGNORECASE)

with open("file.txt", "w") as f:
    f.write(content)
