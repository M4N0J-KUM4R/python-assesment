'''
Note: writing two methods with the same name is impossible in python since because the python compiler takes the recent method as a valid one.
but there are severel tricks and ways to bypass it. i go with the simple one.  
'''
#Write two methods with the same name but different number of parameters of same type

def add(*args):
    return sum(args)

print(add(1, 2))
print(add(1, 2, 3))
-------------------------------------------------------------------------------------------------------------------------------------------------------
#Write two methods with the same name but different number of parameters of different data type and call the methods 

def process(*args):
    if len(args) == 2:
        if isinstance(args[0], int) and isinstance(args[1], int):
            print(args[0] * args[1])
        elif isinstance(args[0], str) and isinstance(args[1], int):
           print(args[0] * args[1])
    else:
        print(sum(arg for arg in args if isinstance(arg, int)))

process(3, 4)           
process('a', 3)        
process(1, 2, 3)
process(5, 'b', 10) 
-------------------------------------------------------------------------------------------------------------------------------------------------------
#. Write two methods with the same name and same number of parameters of same type 

def multiply(a, b, do=None):
    if do == None:
        return a * b
    elif do == 'power':
        return a ** b

print(multiply(2, 3))            
print(multiply(2, 3, 'power'))
