#Write a program to read text file

file = open('book.txt', 'r')
contents = file.read()
print(str(contents))
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to write text to .txt file using InputStream

file = open('book.txt', 'w')
insert :str = 'Hello'
file.write(insert)
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to read a file stream

file_path = 'book.txt'
file = open(file_path, 'r')
for line in file:
 print(str(line, end=''))
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to read a file stream supports random access

file_path = 'book.txt'
file = open(file_path, 'r')
content = file.read(28)
print(str(content))
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to read a file a just to a particular index using seek()

file_path = 'book.txt'
file = open(file_path, 'r')
index:int = 28
file.seek(index)
content = file.read()
print(str(content))
----------------------------------------------------------------------------------------------------------------------------------------------------------
#Write a program to check whether a file is having read access and write access permissions

import os
file_path = 'book.txt'


if os.access(file_path, os.R_OK):
    print(f'{file_path} has read access')
else:
    print(f'{file_path} does not have read access.')

if os.access(file_path, os.W_OK):
    print(f'{file_path} has write access.')
else:
    print(f'{file_path} does not have write access.')
