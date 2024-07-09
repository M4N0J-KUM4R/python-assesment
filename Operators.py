#calling a input function stores the input inside the variable
a = input('enter ur first number')
ASSIGNMENT OPERATOR: 
a = 5
print(a)
'''
Write a function for arithmetic operators(+,-,*,/)
1.ARITHMETIC OPERATORS:
SUM  / Addition:'''
a = float(input('enter your first number'))
b = float(input('enter your second number'))
sum = a + b
print('The addition of {0} and {1} is {2}'.format(a, b, sum)) 

#min/ Subraction:
a = float(input('enter your first number'))
b = float(input('enter your second number'))
min = a - b
print('The subtraction of {0} and {1} is {2}'.format(a, b, min))

#Multiplication:
a = float(input('enter your first number'))
b = float(input('enter your second number'))
max = a * b
print('The multiplication of {0} and {1} is {2}'.format(a, b, max))

#Divition:
a = float(input('enter your first number'))
b = float(input('enter your second number'))
div = a / b
print('The divition of {0} and {1} is {2}'.format(a, b, div))

#Modulus:
a = float(input('enter your first number'))
b = float(input('enter your second number'))
mod = a / b
print('The remainder of {0} and {1} is {2}'.format(a, b, mod))
-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a method for increment and decrement operators(++, --)

#icrementing by one 
a = int(1)
a += 1
print ('a new value of a is',a)

#decrementing by one
a = int(4)
a -= 1
print ('a new value of a is',a)
'''
#icrementing by range
'0' is the starting point (inclusive),
'6' is the ending point (exclusive)'''
for i in range(0, 6):
    print(i)
'''
#icrementing by range
'5' is the starting point (inclusive),
'-1' is the ending point (exclusive)
'-1' is the step size'''
for i in range(5, -1, -1):
    print(i)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the two numbers equal or not

a = int(input('enter your first number'))
b = int(input('enter your second number'))
if a==b:
    print("Both a and b are equal")
else:
    print("Both a and b are not equal")
#or 
a = int(input('enter your first number'))
b = int(input('enter your second number'))
if a!=b:
    print("Both a and b are not equal")
else:
    print("Both a and b are equal")
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Program for relational operators (<,<==, >, >==)
#3. COMPARISON OPERATORS:

#a is Equal to b: 
a = int(5) 
b = int(5) 
print(a == b)

#a is Not equal to b: 
a = int(5)
b = int(3) 
print(a != b)  

#a is Greater than b: 
a = int(5)
b = int(3) 
print(a > b)  

#a is Less than b: 
a = int(5) 
b = int(9) 
print(a < b)  

#a is Greater than or equal to b: 
a = int(5) 
b = int(4) 
print(a >= b)

#a is Less than or equal to b: 
a = int(5) 
b = int(6)
print(a <= b)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Print the smaller and larger number

a = int(input('enter your first number'))
b = int(input('enter your second number'))
def if_larger():
 if a>b:
    print(a, "is larger than ",b)
 else:
    print(b, "is larger than ",a)
if_larger()

def if_smaller():
 if a<b:
    print(a, "is smaller than ",b)
 else:
    print(b, "is smaller than ",a)
if_smaller()
