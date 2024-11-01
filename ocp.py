"""
Open Closed Principle

Software entities, classes, functions, modules should be opened to extension and not Modification

Always ensure to write your classes, function  and modules in such a away as to allow extension over modification

"""


class Animal:
    def __init__(self, name:str):
        self.name = name
    
    def get_name(self) ->str:
        return self.name
    
    
    
animals = [
    Animal("LEOPARD"),
    Animal("BIRD")
]

def animal_sound(animals:list):
    for animal in animals:
        if animal.name ==  "LEOPARD":
            print("ROAR")
        elif animal.name == "BIRD":
            print("SQUEAK")
            
            
animal_sound(animals)



""""
If we are to add another Animal class to t he List of animals
We will need to edit the animal_sound method to accomdate the new animal class
E.g 
"""

animals = [
    Animal("LEOPARD"),
    Animal("BIRD"),
    Animal("MOUSE")
]


def animal_sound(animals:list):
    for animal in animals:
        if animal.name ==  "LEOPARD":
            print("ROAR")
        if animal.name == "BIRD":
            print("SQUEAK")
            
        if animal.name == "MOUSE":
            print("MOUSE")

"""
So the above design allows for modification and at same time extenstion. 
The more animal classes we add the more we modify and extend our animal_sound function

We can redesign the above to allow extensions for the function and class
And make the animal_sound function conform to OCP
"""


class Animal:
    def __init__(self, name:str):
        self.name = name
    
    def get_name(self) -> str:
        pass
    
    def make_sound (self) -> str:
        pass
    
    

class Leopard(Animal):
    def make_sound(self):
        return "LEOPARD"
    
    
class Bird(Animal):
    def make_sound(self):
        return "SQUEAK"
    
    
class Mouse(Animal):
    def make_sound(self):
        return "MOUSE"
    
    
def animal_sound(animals:list):
    for animal in animals:
        print(animal.make_sound())
        
animal_sound(animals)


"""
What we did above is to defined a class for each animal 
Make each of the animal classes to inherit the parent Animal Class
Each of the animal classes overrides the parent Animal Class function -> make_sound


With the above the animal_sound function does not need to change even if we add a 1000 and 1 animal classes inheriting from the Animal Class
"""