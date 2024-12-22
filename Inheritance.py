#OOP
class first():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        print("The init method was created")
    def dispaly(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
    def __del__(self):
        print("Destructor called, object deleted") 
        
        
x = first("Ahmed", 20)
y = first("Nada", 16)

x.dispaly()
y.dispaly()

print(isinstance(x, first))  

del x 
 
# Inheritance 
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand,model)
        self.type = type
    def display_info(self):
        super().display_info()
        print("Type:", self.type) 
        
class Truck(Vehicle):
    def __init__(self, brand, model, max_load):
        super().__init__(brand, model)
        self.max_load = max_load
    def display_info(self):
        super().display_info()
        print("Max_load:", self.max_load) 
        

vec1=Vehicle("ford", "2020")
car1=Car("totyat", "2011", "xx")
truck1=Truck("audi", "2019", "13")

vec1.display_info()
car1.display_info()
truck1.display_info()
    
    
# Multilevel Inheritance 
class Grandparent:
    def __init__(self):
        print("from Grandparent class")

class Parent(Grandparent):
    def __init__(self):
        print("from Parent class")

class Child(Parent):
    def __init__(self):
        print("from Child class")

grandparent = Grandparent()
parent = Parent()
child = Child()
  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

         

