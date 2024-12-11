#%%
for i in range (0,11):
    print(f"i > 5 result in {i>5}")
    if (i > 5 == 0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
print("program execution has ended")
#%%
for i in range (0,11):
    print(f"{i>5 and i%3}")
    if (i>5 and i%3 == 0):
        print(f"{i} true")
    else:
        print(f"{i}")
print("program execution has ended")
#%%