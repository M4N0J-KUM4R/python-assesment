#Create a Dictionary with at least 5 key value pairs of the Student ID and Name

students:str = {
    'S1': 'Manoj',
    'S2': 'Udaya',
    'S3': 'Bharath',
    'S4': 'Nivedha',
    'S5': 'Renu'
}
print(f'Sucessfully created the students list:, {students}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Adding the values in dictionary

students['S6'] = 'Easwar'
print(f'Sucessfully added {students["S6"]} to the students list:, {students}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Updating the values in dictionary

students['S2'] = 'Udhaya'
print(f'Sucessfully updated the {students["S2"]} in the students list:, {students}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Accessing the value in dictionary

student_id:str = 'S2'
print(f'Name of student with ID {student_id}:', students[student_id])
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Create a nested loop dictionary

student_lang:str = {
    'English':{
     'S1': 'Manoj',
     'S2': 'Udaya'   
    },
    'Tamil':{
     'S3': 'Bharath',
     'S4': 'Nivedha'
    },
    'Telugu':{
      'S5': 'Renu',
      'S6': 'Easwar'        
    }
}
print(f'student lang: {student_lang}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Access the values of nested loop dictionary

lang:str = 'Tamil'
student_id:str = 'S3'
print(f'Name of student with ID {student_id} speaks {lang}: {student_lang[lang][student_id]}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Print the keys present in a particular dictionary

print(f'Keys in the main dictionary: {students.keys()}')
print(f'Keys in the nested dictionary for {lang}: {student_lang[lang].keys()}')
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Delete a value from a dictionary

del students['S4']
print(f'Successfully deteted a student: {students}')

##Delete a value from a nested dictionary
del student_lang['Telugu']['S6']
print(f'Successfully deteted a student from Telugu: {student_lang}')
