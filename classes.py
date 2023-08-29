#----------------------------------------------------------|
#                   Unit - 9  | File 7                     |
#                     "Classes"                            |
#     (This is file 7 containing notes of pydocs unit-9)   |
#----------------------------------------------------------|

# The 'global' statement can be used to indicate that 
# particular variables live in the global scope 
# and should be rebound there; 

# the 'nonlocal' statement indicates that 
# particular variables live in an enclosing scope 
# and should be rebound there.

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():
        nonlocal spam
        spam = 'non-local-spam'
    
    def do_global():
        global spam
        spam = 'global-spam'    
        
    spam = 'test spam'
    
    do_local()
    print('after local assignment, spam = ',spam)
    
    do_nonlocal()
    print('after nonlocal assignment , spam = ',spam)
    
    do_global()
    print('after global assignment spam = ',spam)
    
scope_test()
print('In global space spam = ',spam)

# after local assignment, spam =  test spam
# after nonlocal assignment , spam =  non-local-spam
# after global assignment spam =  non-local-spam
# In global space spam =  global-spam

'''
NOTE: how the local assignment (which is default) didn't change 
scope_test's binding of spam. 

The nonlocal assignment changed scope_test's binding 
of spam, and 
the global assignment changed the module-level binding.

You can also see that there was no previous binding 
for spam before the global assignment.

'''

# --------------------self in python class--------------------
'class is blueprint to to make the objects'
'self ka mtlb wo object jis par ye method call ho rha hai'

class employee:
    emp_name = 'default_name'
    emp_id = 'default id'
    emp_salry = 'default salary'
    
    def info(self):
        print(f'Emplyee name = {self.emp_name}')
        print(f'{self.emp_name} id = {self.emp_id}')
        print(f'{self.emp_name} salry = {self.emp_salry}')
        
'creating objects'

obj1 = employee()
obj2 = employee()

'calling info methods for each object'
obj1.info()            
# Emplyee name = default_name
# default_name id = default id
# default_name salry = default salary

obj2.info()
# Emplyee name = default_name
# default_name id = default id
# default_name salry = default salary

'changing values of objects'
obj1.emp_name, obj1.emp_id, obj1.emp_salry = 'Alice',1,10_000

obj2.emp_name= 'Bob'
obj2.emp_id = 2
obj2.emp_salry = 12_000

# ---------------
'calling info again for new objects'
obj1.info()
# Emplyee name = Alice
# Alice id = 1
# Alice salry = 10000

obj2.info()
# Emplyee name = Bob
# Bob id = 2
# Bob salry = 12000

# ----------------Constructors in Python __init__()-------------------------

'constructors in python are made'
'they are made using __init__()'

class demo:
    
    def __init__(self):
        print('I am a default constrcutor')
        
d1 = demo()
d2 = demo()
# I am a default constrcutor
# I am a default constrcutor

class Point:
    
    def __init__(self , x=0,y=0):
        self.x = x
        self.y = y
    
    def info(self):
        print('x = ',self.x ,'||','y = ',self.y)

p1 = Point()
p2 = Point(10)
p3 = Point(10,20)

p1.info()  #x =  0 || y =  0
p2.info()  #x =  10 || y =  0
p3.info()  #x =  10 || y =  20

# ------------------WARNING----using two __init__------
'''
In Python, a class can have multiple methods with the same name,
but only the last one defined will be used. 
However, Python doesn't have the concept 
of multiple constructors like some 
other programming languages (e.g., Java).

A constructor in Python is the __init__ method, 
and 
#####a class can have only one __init__ method. ####imp####

If you define two __init__ methods in a class, 
the second one will overwrite the first one, 
and only the second one will be used 
as the constructor for that class.

Here's an example to illustrate this:
'''      

class using_two_init:
    
    def __init__(self):
        print('constructor 1 executed')
    
    def __init__(self):
        print('constructor 2 executed')
        
u1 = using_two_init()
# constructor 2 executed     

# ------------------------------------------
class Cat:
    
    def __init__(self,name):
        self.name = name
        self.favfood = []
    # this __init__ constructor 
    # states that each dog object will have 
    # a name and 
    # an empty favfood list   
    
    def addfavfood(self,item):
        self.favfood.append(item)
        
    def info(self):
        print('Hi i am',self.name , 'and i like',self.favfood)

cat1 = Cat('snowbell')
cat1.addfavfood('fish')
cat1.addfavfood('mouse')

cat1.info() # Hi i am snowbell and i like ['fish', 'mouse']


# ----------------------
'if we import data from __main__.py' 
'we will not get the main items'
'we will only get items before the main condition'

import script1
print(f'{script1.__name__}')
# script1
