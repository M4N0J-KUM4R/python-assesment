#Write a class with a default constructor, one argument constructor and two argument constructors
#Apply private, public, protected and default access modifiers to the constructor

class Animal:
    def __init__(self, *args): #constructor
        if len(args) == 1: 
            self.name = args[0] #public Variable
        elif len(args) == 2: 
            self.name = args[0] #public Variable
            self._species = args[1] #protected Variable
        elif len(args) == 3:
            self.name = args[0] #public Variable
            self._species = args[1] #protected Variable
            self.__age = args[2] #private Variable

    def species(self): # accessing protected variable
      return self._species

    def age(self): # accessing private variable
      return self.__age

# Instantiate the class to call all the constructors of that class from a main class

class Main(Animal):

    def __init__(self, *args):
       super().__init__(*args) # Calling superclass constructor

    def main(self): #Call the constructors(both default and argument constructors) of super class from a child class
      print(f'the animal is {self.name}') #calling Default constructor
      print(f'the animal {self.name}, is a species of {self.species()}') #calling One-argument constructor
      print(f'the animal {self.name}, is a species of {self.species()} and it lives upto {self.age()} years.') #calling Two-argument constructor

#instance of Main with different constructor arguments
main = Main('dog','Mammel', 12)
main.main()
