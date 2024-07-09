# Write a program to print your name.
print ("Manoj")

#Write a program for a Single line comment and multi-line comments

# adding "#" before any line of code make it as a single-line comment

"""
adding (""") at starting and ending of the muti line code makes it a multi-line comments
"""
#Define variables for different Data Types int, Boolean, char, float, double and print on the Console
#1.TEXT TYPE:
#a string or a char can be represented by adding inbetween to either ' or " . single or double quotes

a = 'Manoj'
print(a)

a = "Manoj"
print(a)

a = '''Manoj is kind!!
Manoj is cute!!             
Manoj is genious!! '''
print(a)

a = """Manoj is kind!!
Manoj is cute!!             
Manoj is genious!! """
print(a)
---------------------------------------------------------------------------------------------------------------------------------------------------------
#2.NUMERIC TYPES:	
#int:
a = 20
print(type(a))

#float:
a = 20.5
print(type(a))

#double: in python the double is also represnted in type float
a = 20.592653589793
print(type(a))

#complex: in python we use complex for presice calcutions like scientific calculations and memory saving complex tasks
a = 1j
print(type(a))
-----------------------------------------------------------------------------------------------------------------------------------------------------------
#3.BOOLEAN TYPE:	
#bool:
a = True
print(type(a))

a = False
print(type(a))

#NoneType:
a = None
print(type(a))
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Define the local and Global variables with the same name and print both variables and understand the scope of the variables

a = "Global Variable"
print('global Variable Id: ',id(a))
def fun():
  a = "Local Variable"
  print('Local Variable Id: ',id(a))
fun()

#by executing the above code you expected to see different memory ID of the same variable "a" saved as global and local variable, local variables can only called inside the function. but global variables can be called from everywhere
