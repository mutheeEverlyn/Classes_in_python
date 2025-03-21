# Parent class Animal
class Animal:
    def make_sound(self):
        pass #used to define a null function

# Subclass Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Subclass Cow
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Function to test the make_sound method of each animal
def animal_sound(animal):
    print(animal.make_sound())

# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)  # Output: Woof! 
animal_sound(cat)  # Output: Meow! 
animal_sound(cow)  # Output: Moo! 
