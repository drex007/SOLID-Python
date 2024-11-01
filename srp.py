"""
Single Responsibility Pattern

A class should have only one responsibility
If starts becoming more than one, it becomes coupled.

A change to on responsibility result to a change in another

"""


"""
This violates the SRP principle in the sense that the class does two function
1. Returns animal name 
2. Saves animal name to the DB 

So basically it does two funcs

"""
class Animal:
    def __init__(self,name:str):
        self.name = name
        
    def get_name(self) ->str:
        pass
    
    def save(self) -> str:
        pass
    
    


#Inorder to make this conform to the SRP Principle 
#We need to rewrite the classes and prolly ad and extra
#So the two classes does two separate function
#1. Returning Animal Name 
#2. Saving Animal to the DB


class Animal:
    def __init__(self, name:str):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
    
    
class AnimalRepository:
    def save(self, animal:Animal):
        pass