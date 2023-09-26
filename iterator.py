mylist=['apple','banana','peach','mango']

myiter= iter(mylist)

print(next(myiter)) #next() method will go to the next item in an iterable
print(next(myiter))
print(next(myiter))
print(next(myiter))


for iter in mylist:
    print(len(iter))
    
    
