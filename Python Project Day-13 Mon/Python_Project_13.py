 #%%
import numpy as np
# %%
#%%
import numpy as np
# %%



# print(f"{mytemp} in Fahrenheit is {c_to_f(mytemp)}")
# %%

# def c_to_f(temp_c):
#     temp_f = temp_c * 1.8 + 32
#     return temp_f

# def f_to_c(temp_f):
#     temp_c = (temp_f + 32) / 1.8
#     return temp_c

# mytemp = float(input("Enter a temperature "))
# mychar = input("Enter either F or C to convert to: ")

# if mychar == "F":
    
#     print(f"{mytemp} in Fahrenheit is {c_to_f(mytemp)}")
#     # print("Conversion from F to something is done!")
# elif mychar == "C":
#     print(f"{mytemp} in Celsius is {f_to_c(mytemp)}")
# else:
#     print("You have made an invalid choice.")

# %%

mytemp = int(input("Enter a temperature "))
print(f"You Entered {mytemp}")
# %%

try:
    mytemp = int(input("Enter a temperature "))
    print(f"You Entered {mytemp}")
except ValueError:
    print("You did not enter an integer")
# %%

mytemp = 1
while(mytemp != 0):
    try:
        mytemp = int(input("Enter a temperature "))
        print(f"You Entered {mytemp}")
    except ValueError:
        print("You did not enter an integer")
#%%

# Temperature Conversion Functions
def c_to_f(temp_c):
    temp_f = temp_c * 1.8 + 32
    return temp_f

def f_to_c(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c



# User Input for Temperature Conversion
mytemp = float(input("Enter a temperature: "))
mychar = input("Enter either F or C to convert to: ").strip().upper()

if mychar == "F":
    print(f"{mytemp} in Fahrenheit is {c_to_f(mytemp)}")
elif mychar == "C":
    print(f"{mytemp} in Celsius is {f_to_c(mytemp)}")
else:
    print("You have made an invalid choice.")

# String Case Conversion
print("\nString Case Conversion!")
user_string = input("Enter a string to modify: ")
case_choice = input("Do you want to convert it to upper case (U) or lower case (L)? ").strip().upper()

if case_choice == "U":
    print(f"Your string in uppercase is: {user_string.upper()}")
elif case_choice == "L":
    print(f"Your string in lowercase is: {user_string.lower()}")
else:
    print("Invalid choice for case conversion.")

# %%

myvar = int(input("Enter a non-negative integer: "))
fact = 1
n = myvar
while n > 0:
    fact = fact * n 
    n = n - 1
print(f"The factorial of {myvar} is: {fact}")

# %%
