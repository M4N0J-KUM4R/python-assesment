#Write a program to print “Bright IT Career” ten times using for loop.

a = str("Bright IT Career")
for i in range (10):
  print(a)
-------------------------------------------------------------------------------------------------------------------------------------------------------------  
#Write a python program to print 1 to 20 numbers using the while loop.

a = int(1)
while(a<=20):
  print(a)
  a+=1 
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Program to equal operator and not equal operators

a = int(input('enter your first number'))
b = int(input('enter your second number'))
print(a==b)#equal operator

a = int(input('enter your first number'))
b = int(input('enter your second number'))
print(a!=b)#not equal operators
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to print the odd and even numbers.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even Numbers: ")
for i in a:
    if i % 2 == 0:#print the even numbers
        print(i, end=" ")
print("\nOdd Numbers:")
for i in a:
    if i % 2 != 0:#print the odd numbers
        print(i, end=" ")
print()
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to print largest number among three numbers.

a = int(1)
b = int(3)
c = int(5)
largest = max(a, b, c)
print(f"The largest number among {a}, {b}, and {c} is {largest}")
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to print even number between 10 and 20 using while

a = int(10)
print("Even numbers between 10 and 20: ", end=" ")
while(a<=20):
  if(a %2 == 0): 
   print(f"{a}",end=" ")
  a+=1
print()
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to print 1 to 10 using the do-while loop statement.

a = int(1)
while True:
    print(f"{a}",end=" ")
    a += 1
    if a > 10:
        break
print()
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to find Armstrong number or no

a=int(153)
a_str = str(a) #convert the int to str
n = len(a_str) # check the len of new str
sum = 0 
for digit in a_str: #for loop to iterate every index
    sum += int(digit)**n #convert str digit to int for exponential '**' operation and adding everything together
if sum == a:
    print(f'the given {a} number is an armstrong number')
else:
    print(f'the given {a} number is not an armstrong number')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to find the prime or not.

a = int(input('Enter a number to check if it is a prime number or not: '))

if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print(f'The given number {a} is not a prime number')
            break
    else:
        print(f'The given number {a} is a prime number')
else:
    print(f'The given number {a} is not a prime number')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to palindrome or not
a = str(input('Enter a word to check palindrome or not:'))
l_a = a.lower()  # Convert to lowercase
reverse = ''.join(reversed(l_a))
if reverse == l_a:
  print(f'the given word {a} is a palindrome')
else:
  print(f'the given word {a} is not a palindrome')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Program to check whether a number is EVEN or ODD using switch
#Print gender (Male/Female) program according to given M/F using switch

#no function like switch in python only way is to create multiple function or a class so skipping these two for now.
