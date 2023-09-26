#global scope
# A variable created in the main body of the Python code is a global variable and available within all of the scopes

x= 100

def myglobal():
    print(x)
    

myglobal()






#local scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def mylocal():
    x=200
    print(x)
    
mylocal()





#The local variable can be accessed from a function within the function

def myfunc():
    x=150
    def myfunc2():
        print(x)
        
        
    myfunc2()
    
    
myfunc()





# the global variable  will not effected from the one wich is in the function and will be treated as two seprate vars


y=500


def num():
    y=1000
    print(y)

num()

print(y)






# use the global keyword to make a variable global from inside a function


def test():
    global a
    a=123
    
test()
print(a)



# Also, use the global keyword if you want to make a change to a global variable inside a function.

b=200

def test():
    global b
    b=400
    print(b)
    
test()
print(b)