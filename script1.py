# --------------__name__=='__main__'-----------------------

# if we import this file to some other file
# all the above code will be executed unnecessarily
'but if we not want all the above mess code print in'
'another code terminal also'
'we can use this name==main condition'


# print(__name__)    
# __main__

print('this data is of file main.py before the main condition')

if __name__ == "__main__":
    print('this code will not execute when we import it to other file') 
    print(f'the name from script1 is {__name__}')   