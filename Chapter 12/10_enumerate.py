l = [1,45,6,78,988,56]

# index = 0
# for item in l:
#     print(f"The item number is at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function
for index,item in enumerate(l):
    print(f"The item number is at index {index} is {item}")