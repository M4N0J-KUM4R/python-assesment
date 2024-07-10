#Define a static variable and access that through a class

class Student:
    present = int(7)
print(f'The total number of presenties now are: {Student.present}')

#Define a static variable and access that through a instance

Attandance = Student()
print(f'The attendance count is: {Attandance.present}')

#Define a static variable and change within the instance

Attandance.present = (8)
print(f'The total attendance until the day is: {Attandance.present}')

#Define a static variable and change within the class

Student.present = int(6)
print(f'The total number of presenties for the full day is: {Student.present}')
