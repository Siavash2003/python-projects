Name= ' Siavash'

LastName=' Salmani'

City=' FooladShahr'

Age= 20

Me= Name + LastName + City + str(Age)  #you should convert anything to str to concatenate them

print(Me)


myAge= f'My Age is : {Age}'  # use this format method to merge an int with an str without converting it

print(myAge)

myInfo= f'My name is{Name} And my Last name is{LastName} And i live in{City} And Im {Age} Years Old' 

print(myInfo)