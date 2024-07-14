#Create a program to create two class.
#Create a constructor and a method for each class

#->project/packages/laptop.py
class Laptop:
    def __init__(self, brand, model, price): #constructor
        self.brand = brand
        self.model = model
        self.price = price

    def describe(self): #method for class Laptop
        print(f"{self.brand} {self.model} costs {self.price}")

#->project/packages/mobile.py
class Mobile:
    def __init__(self, brand, model, price): #constructor
        self.brand = brand
        self.model = model
        self.price = price

    def describe(self): #method for class Mobile
        print(f"{self.brand} {self.model} costs {self.price}")
      
#. Create a __init__.py for adding all packages

#->project/packages/__init__.py
from .laptop import Laptop
from .mobile import Mobile

#->project/main.py
from packages import Laptop, Mobile # Import the respective packages

#Call each class by creating an object to it 
laptop1 = Laptop("Dell", "XPS 13", 23,999)
mobile1 = Mobile("Samsung", "Galaxy S7", 19,000)

laptop1.describe()
mobile1.describe()

#Created a program by all the above
