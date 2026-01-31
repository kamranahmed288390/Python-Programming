name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your phone number: "))

s = "The name of the student is {}. The marks obtained by him are {}. His phone number is {}."

print(s.format(name, marks, phone))