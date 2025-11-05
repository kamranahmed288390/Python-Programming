with open("log.txt") as f:
    lines = f.readlines()  # Read all lines

lineno = 1
for line in lines:
    if "python" in line.lower():  # .lower() makes it case-insensitive
        print(f"Yes, 'python' is present on line {lineno}.")
        break
    lineno += 1
else:
    print("Python is not present.")

   