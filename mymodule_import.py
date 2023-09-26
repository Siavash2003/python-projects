
import mymodule1 as mod # renaming module

from mymodule1 import hi,sub    # you can call a specefic code from a module

from mymodule1 import * # * imports all of the Codes

import platform # built in module

import random

hi
mod.hi('reza')


mod.sub(12,45)


st1= hi('sia') # creating an object from a modulde class

mycar.printcar


print(info['name'])



listname= dir(mod) # list all the function names in a module

print(listname)

print(platform.system())

print(random.randint(10,15)) # return a random int between a and b


mylist=['apple','mango','pear','grape']


choose=random.choice(mylist)

print(choose)