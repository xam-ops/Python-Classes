#%%

myinput = input("Enter a string: ")

result = myinput.replace(" ", "")

print("String without spaces:", result)

# %%

for i in range(5):
    myinput = input("Enter a string: ")

    result = myinput.replace(" ", "")

print("String without spaces:", result)

# %%

myvar = int(input("Enter a non-negative integer: "))
fact = 1
n = myvar
while n > 0:
    fact = fact * n 
    n = n - 1
print(f"The factorial of {myvar} is: {fact}")

# %%

myvar = int(input("Enter a non-negative integer: "))
fact = 1

for n in range(myvar, 0, -1):
    fact = fact * n

print(f"The factorial of {myvar} is: {fact}")

# %%
