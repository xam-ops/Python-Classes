#%%
mylist1 = [1,2,3,4]
mylist2 = mylist1*3
print(mylist2)
# %%
import numpy as np
# %%

# mylist3 = list (np.array(mylist1)*2)
# print(mylist3)
# %%

mylist3 = (np.array(mylist1)*2).tolist()
print(mylist3)
# %%
def c_to_f(temp_c):
    temp_f = temp_c * 1.8 + 32
    return temp_f

mytemp = 30
print(f"{mytemp} in Fahrenheit is {c_to_f(mytemp)}")
# %%

def c_to_f(temp_c):
    temp_f = temp_c * 1.8 + 32
    return temp_f

mytemp = input()
print(f"{mytemp} in Fahrenheit is {c_to_f(mytemp)}")

# %%
