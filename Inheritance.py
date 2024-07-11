'''
A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Create three methods in each class, 2 methods are specific to each class and third'''

class Car: #super class
  def start(self):
      print(str('Car started'))
  
  def stop(self):
        print(str('Car stopped'))

  def drive(self): #override method
      print(str('Driving a regular car'))

class ElectricCar(Car): #sub class of Car
  def charge(self):
        print(str('Electric car is charging'))

  def drive(self): #override method
        print(str('Driving an electric car'))

class Tesla(ElectricCar): #sub class of ElectricCar
  def autopilot(self):
        print(str('Tesla in autopilot mode'))

  def drive(self): #override method
        print(str('Driving a Tesla'))
#Create a class with main method.
class Main:
#Create an object for each class A, B and C in main

 car = Car()
 electric_car = ElectricCar()
 tesla = Tesla()

#call every method of each class using its own object/instance.
#Call an overridden method with super class reference to B and C class’s objects
#Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members
 car.start()
 car.stop()
 car.drive()
 electric_car.start()
 electric_car.stop()
 electric_car.drive()
 electric_car.charge()
 tesla.start()
 tesla.stop()
 tesla.drive()
 tesla.charge()
 tesla.autopilot()
