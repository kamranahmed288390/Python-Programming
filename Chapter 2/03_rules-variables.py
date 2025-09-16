name = "Alice"      # ✅ Valid
_name = "Bob"       # ✅ Valid
# 1name = "Charlie"   # ❌ Invalid (starts with a number)

user1 = "Tom"           # ✅ Valid
user_name = "Jerry"     # ✅ Valid
# user-name = "Spike"     # ❌ Invalid (dash is not allowed)

age = 20 # age, Age, and AGE are all different variables.
Age = 25
AGE = 30
print(age, Age, AGE)  # Output: 20 25 30

# def = 5        # ❌ Invalid (def is a keyword)
my_def = 5     # ✅ Valid (custom name)

x = 5             # ✅ Valid but not descriptive
number_of_apples = 5  # ✅ Better and more readable

x, y, z = 1, 2, 3     # ✅ Multiple assignment
a = b = c = 0         # ✅ All assigned to 0
