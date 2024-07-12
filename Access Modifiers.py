#Create a class with PRIVATE fields.

class Private:
  def __init__(self):
    self.__var1 : str = 'this is private variable'
    
  # Create private method and a main method.
  def __private_method(self):
    print(str('I am a private method!'))

  def main_method(self):
    print(self.__var1) #Print the fields in main method.
    self.__private_method() #Call the private method in main method.

#Create a sub class and try to access the private fields and methods from sub class.   

class Subclass(Private):
  def see_private(self):

    # This will not work because ____var1 and __private_method are "private"
    #print(self.__var1)
    #self.__private_method()

    # This will work and it is the correct way to access
    self.main_method()

    # This will work and it is not the correct way to access
    #print(self._Private__var1)
    #self._Private__private_method()

py=Private()
py.main_method()

sub_py=Subclass()
sub_py.see_private()
----------------------------------------------------------------------------------------------------------------------------------------------------
'''
from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package'''

#Create a class with PROTECTED fields and methods.

class Protected:
  def __init__(self):
    self._var2 : str = 'This is protected variable'
    
  # Create private method and a main method.
  def _protected_method(self):
    print(str('I am a protected method!'))

  def main_method(self):
    print(self._var2) #Print the fields in main method.
    self._protected_method() #Call the private method in main method.

class Subclass(Protected): #If the parent class is removed we cannot access the methods in private
  def see_Protected(self):

    # This will work
    print(self._var2)
    self._protected_method()

    # This will work and it is the correct way to access
    self.main_method()

class Sepclass: # Access these fields and methods from any other class
    def access_protected(self, access): 
        print(access._var2)
        access._protected_method()

pr=Protected()
pr.main_method()

sub_pr=Subclass()
sub_pr.see_Protected()

sep_pr = Sepclass()
sep_pr.access_protected(pr)

#Access these fields and methods from any other class in the same package.
'''
Note: it can be done my simply importing the class from the same directory which should also contain the class code in the respective file name can be anything,
aslo the directory should also contain __init__.py and the class can be called to the new file with the below line of code.'''

from protected_class import Protected #in this case my protected class file name is saved as protected_class.py

class Otherclass:
    def __init__(self):
        self.access = Protected()

    def access_protected(self):
        print(self.access._var2)
        self.access._protected_method()

    def access_main_method(self):
        self.access.main_method()
        
otr_pr = Otherclass()
otr_pr.access_protected()
otr_pr.access_main_method()

'''
Note: it can be done my simply importing the class from the different directory which should also contain the class code in the respective file name can be anything,
aslo the directory should also contain __init__.py and the class can be called to the new file with the below line of code.'''
from protecteds.protected_class import Protected #in this case my protected class file name is saved as protected_class.py in a directory named protecteds

'''Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package'''

class Differentclass:
    def __init__(self):
        self.access = Protected()

    def access_protected(self):
        print(self.access._var2)
        self.access._protected_method()

    def access_main_method(self):
        self.access.main_method()
        
diff_pr = Differentclass()
diff_pr.access_protected()
diff_pr.access_main_method()
----------------------------------------------------------------------------------------------------------------------------------------------------
#Create a class with PUBLIC fields and methods.

class Public:
    def __init__(self):
        self.var3: str = 'This is a public variable'
    
    def public_method(self):
        print('This is a public method')

from public_class import Public #in this case my public class file name is saved as public_class.py

class Otherclass: #Access the public methods and fields from any class in the same package
    def __init__(self):
        self.access = Public()

    def access_public(self):
        print(self.access.var3) 
        self.access.public_method()

otr_pb = Otherclass() 
otr_pb.access_public()

from publics.public_class import Public #in this case my public class file name is saved as public_class.py in a directory named publics

class Differentclass: #Access the public methods and fields from any class in the different package
    def __init__(self):
        self.access = Public()

    def access_public(self):
        print(self.access.var3) 
        self.access.public_method()

diff_pb = Differentclass()
diff_pb.access_public()
