#Write a function to add integer values of an array

array = [1, 2, 3, 4, 5]
j=0
for i in range(0, len(array)):
    j= j+array[i]
print(f'The total value of all integers in the arrays is: {j}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to calculate the average value of an array of integers

array = [1, 2, 3, 4, 5]
def average_value(array):
    i = 0
    for j in array:
        i += j
    average = i / len(array)
    return average
average_value(array)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to find the index of an array element

array = [1, 2, 3, 4, 5]
index = array.index(3)
print(f'the valuve in index of 3: {index}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to test if array contains a specific value

array = [1, 2, 3, 4, 5]
try:
  index = array.index(3)
  print(index)
except:
  print("Given element not found in the array.")
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to remove a specific element from an array
array = [1, 2, 3, 4, 3, 5]
element_to_remove = 3
for i in range(len(array) -1,-1,-1): #this loop iterate to check every element in reverse by -1 step until -1 for including index zero. 
    if array[i] == element_to_remove: #check the presnce of element_to_remove is present in each index.
        array.pop(i) #deletes the element in the current index
print(f"The array after removing {element_to_remove} is: {array}")
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to copy an array to another array
#Shallow copy:
array = [1, 2, 3, 4, 5]
array1 = array #creates a new lable and shares the memory of existing array 
print(array1)
print(id(array))
print(id(array1))

#Deep Copy:
array = [1, 2, 3, 4, 5]
array1 = []
array1 = array.copy() #creates a new lable and separate duplicate memory of existing array
print(array1)
print(id(array))
print(id(array1))
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to insert an element at a specific position in the array

array = [1, 2, 3, 4, 5]
array.insert(5,6) #inserts element 6 at index 5 in array
print(array)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to find the minimum and maximum value of an array

array = [1, 2, 3, 4, 5]
minimum = min(array)
maximum = max(array)
print(f'the minimum value of an array is: {minimum}')
print(f'the maximum value of an array is: {maximum}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to reverse an array of integer values

array = [1, 2, 3, 4, 5]
array = array[::-1]
print(array)
#(or)
array = [1, 2, 3, 4, 5]
array.reverse()
print(array)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to find the duplicate values of an array

array = [1, 2, 3, 4, 3, 5]
for i in range(0,len(array)):
  for j in range(i+1, len(array)):
    if array[i] == array[j]:
     print(f'the Duplicate number found in the array is: {array[j]} and found in index {j}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to find the common values between two arrays

array = [1, 2, 3, 4, 3, 5]
array1 = [3, 4]
common_values = set(array).intersection(array1)
print(f'The common values between two arrays: {list(common_values)}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method to remove duplicate elements from an array

array = [1, 2, 3, 4, 3, 5]
array1 = []
for i in array:
    if i not in array1:
        array1.append(i)
print(array1)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method to find the second largest number in an array

array = [1, 2, 3, 4, 3, 5]
array = sorted(array)
print(f'The second largest number in an array is: {array[-2]}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method to find the second smallest number in an array

array = [1, 2, 3, 4, 3, 5]
array = sorted(array)
print(f'The second largest number in an array is: {array[1]}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method to find number of even number and odd numbers in an array

array = [1, 2, 3, 4, 5]
even_count = 0
odd_count = 0
for num in array:
   if num % 2 == 0:
      even_count += 1
   else:
      odd_count += 1
print(f'The toatal number of odd number presentin array is : {odd_count}')
print(f'The toatal number of even number presentin array is : {even_count}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a function to get the difference of largest and smallest value

array = [1, 2, 3, 4, 5]
array = sorted(array)
print(f'Diffrence of largest and smallest value: {array[4]-array[0]}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a method to verify if the array contains two specified elements(12,23)

array = [1, 2, 3, 4, 5, 12]
for i in array:
    if i == 12:
        print('The element 12 exist in array')
    if i == 23:
        print('The element 23 exist in array')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to remove the duplicate elements and return the new array

array = [1, 2, 3, 4, 5, 3]
array1 = []
for i in array:
    if i not in array1:
        array1.append(i)
print(array1)
