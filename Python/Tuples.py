Name = ('sia', 'ali', 'reza')

print(Name)

#this is a method to add or change a tuple items by casting

Update = list(Name)

Update[1]= "hadi"

Name2= tuple(Update)

print(Name2)


tuple1= ('sia','reza',12,43)
tuple2= (12,343,23,234,2)

tuple3=tuple1+tuple2

print(tuple3)


Test=('sia')
Test2=("sia",) # to make a single item tuple you should put a , after that
print(type(Test))
print(type(Test2))
