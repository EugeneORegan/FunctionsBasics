import Other
#Simple function to print hello … notice the : and indentation
def Hello():
    print("Hello")

def add(a, b):
    return a+b

Hello() # Invoking, Calling Hello function
c = add(2,3) #Invoking add() and writing the return value to c
print("Addition ...", c)
Other.x() # Invoking x function from Other class ... Ability to share functionality between classes
Other.y("Today")# Invoking y function from Other class and feeding in a value
c = Other.add(1,2) # Invoking add function from Other class, feeding in values and returning a value
print(c)