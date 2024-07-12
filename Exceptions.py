#Write a program to generate Arithmetic Exception without exception handling

a = 10/0
print(a)
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Handle the Arithmetic exception using try-catch block

try:
    a = 10/0
    print(a)
except ZeroDivisionError:
       print("Can't divide by zero")
