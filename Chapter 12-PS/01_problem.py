try:
    with open("1.txt", "r") as f:
     print(f.read())
except Exception as e:
    print("File not found", e)

try:
    with open("2.txt", "r") as f:
     print(f.read())
except Exception as e:
    print("File not found", e)
 
try:
    with open("3.txt", "r") as f:
     print(f.read())
except Exception as e:
    print("File not found", e)


print("Thank you!")