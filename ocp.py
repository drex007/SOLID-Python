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

def make_sound(animals:list):
    for animal in animals:
        if animal.name ==  "LEOPARD":
            print("ROAR")
        elif animal.name == "BIRD":
            print("SQUEAK")
            
            
make_sound()



""""
If we are to add another Animal class to t he List of animals
We will need to edit the make_sound method to accomdate the new animal class
E.g 
"""

animals = [
    Animal("LEOPARD"),
    Animal("BIRD"),
    Animal("MOUSE")
]


def make_sound(animals:list):
    for animal in animals:
        if animal.name ==  "LEOPARD":
            print("ROAR")
        if animal.name == "BIRD":
            print("SQUEAK")
            
        if animal.name == "MOUSE":
            print("MOUSE")

"""
So the above design is wrong, the best we should do is to 
"""