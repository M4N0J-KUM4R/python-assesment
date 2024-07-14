#Write a program to generate Arithmetic Exception without exception handling

a:int = 10
print(a/0)
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Handle the Arithmetic exception using try-catch block

try:
    a:int = 10
    print(a/0)
except ZeroDivisionError:
       print("Can't divide by zero")
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method which throws exception, Call that method in main class without try block

class Main():
    
 def method():
     raise Exception('This is an exception')
 method()
a = Main()
a.method()
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program with multiple catch blocks

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as z:
        print("Can't do", z)
    except TypeError as t:
        print('Error: Input is not a number', t)

print(divide('10', 0))
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to throw exception with your own message

 def method():
    raise Exception('This is  own exception')

 method()
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to create your own exception

class Custom_exception(Exception):
    pass
    
def method():
    raise Custom_exception('This is my own exception')
method() #comment this to bypass the Error.
try:
    method()
except Custom_exception as e:
    print(f'custom exception: {e}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program with finally block

def method():
    try:
        a = 2 / 0
    except ZeroDivisionError:
        print('ZeroDivisionError Exceptioned')
    finally:
        print('sucessfully executed')
        
method()
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to generate Arithmetic Exception
try:
    a = 2 / 0
except ArithmeticError as e:
    print(f'ArithmeticError Exceptioned: {e}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to generate FileNotFoundException

try:
    with open('Book.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f'FileNotFound Exceptioned: {e}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to generate ClassNotFoundException

class Main(Exception):
    pass

try:
    raise Main('Class not found')
except Main as e:
    print(f'Main Exceptioned: {e}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to generate IOException

try:
    raise OSError('This is an IO error')
except OSError as e:
    print(f'OsError Exceptioned: {e}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to generate NoSuchFieldException
#skipping: There is no exception on python as 'NoSuchFieldException'.
#only way is creating own custom exception. created by a class with defined function which mimics it.
