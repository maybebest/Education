"""Opening and Closing Files"""

ZEN = open('the_Zen_of_Python')

print("Name of the file: ", ZEN.name)  # Name of the file:  the_Zen_of_Python
print("Closed or not : ", ZEN.closed)  # Closed or not :  False
print("Opening mode : ", ZEN.mode)  # Opening mode :  r

ZEN.close()

with open("the_Zen_of_Python", 'r', 2) as ZEN:
    print("Name of the file: ", ZEN.name)
    print("Closed or not : ", ZEN.closed)
    print("Opening mode : ", ZEN.mode)

print("Closed or not : ", ZEN.closed)  # Closed or not :  True
