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

mynum = int(input("enter a number to calculate factorial for : "))
temp_n = mynum
fact_product = 1
while temp_n != 1:
    fact_product = fact_product * temp_n
    temp_n = temp_n - 1
print(f"the factorial of {mynum} is {fact_product}")
# %%


mylist = ["abbas", "shop", "Asjad", "apple", "bed", "cricket", "bat", "zebra", "chair", "computer"]
result = []
for i in mylist:
    if i[0] == 'a' or i[0] == 'A':
        result.append(i)
print(f"words start's with 'a' & 'A' from the list are : {result}")
 # %%

mylist = ["madam", "hello", "racecar", "world", "level", "python", "radar"]
for i in mylist:
    if i == i[::-1]:
        print(i)
# %%
