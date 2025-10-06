marks = {
    "Kamran": 23,
    "Ahmed": 89,
    "Taha": 78
}

# print(marks.items())
# print(marks.keys())

marks.update({"Kamran":98})
print(marks)

print(marks.get("Kamran2")) # Prints none
print(marks["Kamran2"]) # Return an error