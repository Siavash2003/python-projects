def my_function():  # parameter
    print('hello,im Siavash')


my_function()  # this is how to call a function
my_function()  # argument


def my_name(name, lastname):
    print(f'hello {name} {lastname}')


# my_name(name=input('what is your name: ') ,lastname=input("what is your last name :") )


def sum(a, b):
    print(a + b)


sum(2, 2)


# Arbitrary Arguments, *args

def greet(*args):  # we use *args wen we want to add inlimited amount of args
    print(f'hello {args}')


greet('sia', 'ali', 'reza', 'mamad')


def hello(*names2):
    for name in names2:
        print(f'hello {name}')


hello('sia', 'ali', 'reza', 'mamad')


def welcome(fname, lname, *args):
    print(f'hello {fname}')
    print(f'hello {lname}')

    for name in args:
        print(f'hello {args}')


welcome('siavash', 'salmani', 'reza', 'amir', 'hadi')


# keyword args
def info(lname, fname, **kwargs):
    print(fname)
    print(lname)
    print(kwargs)  # dict

    # This way the order of the arguments does not matter. and its key=valu


info(lname='Siavash', fname='Salmani', age=23, city='fooladshahr')


# default parameter function
def default(name='Siavash', lname='Salmani'):
    # in this function setting an arg is not necessary because its already given
    print(f'hello {name} {lname}')


default()


# passing a list or dict or tuple as an arg

def eatable(foods):
    for food in foods:
        print(f'my favorite food is  {food}')


fruits = ['apple', 'banana', 'peach']

eatable(fruits)


# return Value

def sum(a, b):
    a += 5
    b *= 2
    c = 5
    return a, b, +c
    


result = sum(12, 2)
for item in result:
    print(item)


# this machine counts upper and lowerCase letters in a str

def counter(name):
    upps = 0
    lows = 0
    num = 0
    for char in name:
        if char.islower():
            upps += 1
        elif char.isupper():
             lows += 1
        elif char.isnumeric():
            num += 1
        else:
            pass

    print(f'upper : {upps}')
    print(f'lower : {lows}')
    print(f'number : {num}')


while True:
    name = input('enter :')

    counter(name)

    # this machine checks  that a number is even or odd

    number = int(input('enter the number'))

    def num(number):
        answer = number % 2
        if answer == 0:
            print("Even")  # zoj
        else:
            print("odd")  # fard

    num(number)




def num(n):
    def num2(a):
        return a*n
    
    return num2
    
mydoubler = num(2)
mytripler = num(3)

print(mydoubler(2))
print(mytripler(5))
