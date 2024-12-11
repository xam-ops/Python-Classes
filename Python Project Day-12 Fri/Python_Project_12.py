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
