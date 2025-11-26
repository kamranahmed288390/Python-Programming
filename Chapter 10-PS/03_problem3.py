class demo:
    a = 4

o  = demo()
print(o.a) # Pronts the class attribute as the instance attribute is not present 
o.a = 0 # Instance attribute is set 
print(o.a) # Prints the instance attribute because instnace attribute is present 
print(demo.a) # Print the class attribute