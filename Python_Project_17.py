#%%
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The Dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")
    
my_dog = Dog()
my_cat = Cat()

my_dog.sound()
my_cat.sound()
# %%

class Shape:
    def area(self): 
        pass

class Circle(Shape):
    def __init__(self, radius):  # Fixed __init__
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):  # Fixed __init__
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Polymorphism
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f'Area: {shape.area()}')
#%%

file = open('example.txt', 'w')
file.write('Hello\nworld!')
file.close()
for file in range (1,11):
    print(file)

# %%
file = open ('example.txt', 'w')
for  i in range (1,11):
    file.write('Hello, world\n')
file.close()

# %%