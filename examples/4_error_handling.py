try:
    # Write your operations here
    print(numbers)
except:
    # If there is an error, the code in this block will be executed
    # For example, here you can log the error details
    print("An exception occured")
print("-----------------------------------")




try:
    print(numbers)
except NameError:
    print("An NameError occured")
print("-----------------------------------")


#a = "one"
try:
    print(int(a))
except NameError:
    print("A NameError occured")
except TypeError:
    print("A TypeError occured")
except ValueError:
    print("A ValueError occured")
except:
    print("Another type of error occured")
print("-----------------------------------")
