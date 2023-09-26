a = 12
b = 30
c= 40
 
 #nested if
 
if a > b:
    # you should use indentation to print something under a condition
    print('a is greater than b')
if a<b:
    print("a is not greater than b")
else:
    print("a is not greater than b")


if a != b:
    print('a is not equal b')
elif a < b:
    # only one condition raise in elif method even if another is True
    print("a is less than b")
elif a == b:
    print('a and b are equal')
else:
    print('Error!')


if a < b:
    print('a is greater than b')  # this is short hand if


print('true') if a>b else print('false') # short hand if..else



#logical operators

if b>a and c>b: 
    print('both conditions are true')
    
if b>a or c>b: 
    print('one condition is true')
    
if not c<b: 
    print('condition is false')
    
if a<b or a==b and b<c :
    print('hello!')
    

if a>b :
    pass #this is pass statement and does nothing and passes if the condition is true