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



"""
We will take a second example and


Assuming you own an Ice cream shop and you are currently running a discount for your customers as follows

1. Normal Discount  (10% discount)
2. Customers at age 50  (20 % discount)
3. Customer above 70 years  (40% discount)
"""


class Discount:
    def __init__(self, age, price):
        self.age = age
        self.price = price
    
    def get_discount(self):
        if self.age == 50:
            return self.price * 0.1 * 2
            
        if self.age > 70:
            return self.price * 0.1 * 4 
            
"""
Assuming you decided to add to your discount list of customers that are less than 15 years (60% discount) of age

We will need to add to the conditions of get_discount and this will make it longer and defiles the law of OCP


"""


"""
The above has been redefined below inorder to conform to OCP 
"""


class Discount:
    def __init__(self, price):
        self.price = price
        
    def get_discount(self):
        return self.price * 0.1

class Age50Discount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

class Age70Discount(Discount):
    def get_discount(self):
        return super().get_discount() * 4

class Below15Discount(Discount):
    def get_discount(self):
        return super().get_discount() * 6
