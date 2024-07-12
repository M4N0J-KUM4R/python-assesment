#Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod

class Car(ABC):

  @abstractmethod #Create an object in the child class for the abstract class
  def move(self):
    pass

  @abstractmethod
  def stop(self):
    pass

  def speed(self): #Create an object in the child class for the non abstract class
    pass

class BMW(Car): #Create a sub class for an abstract class

  def move(self):
    print(str('BMW is moving.'))

  def stop(self):
    print(str('BMW has stopped'))


class Ford(Car):

  def move(self):
    print(str('Ford is moving.'))

  def stop(self):
    print(str('Ford has stopped'))


  def speed(self):
    print(str('Top speed 240mph'))


bmw = BMW() #Create an instance for the child class in child class and call abstract methods

bmw.move()
bmw.stop()

ford = Ford() #Create an instance for the child class in child class and call non-abstract methods


ford.move()
ford.stop()
ford.speed()
