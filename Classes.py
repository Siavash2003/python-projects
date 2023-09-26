class MyClass:
    x= 5
    y=10

obj1= MyClass()
obj2= MyClass()


print(obj1.x) # .x is the  objects propertie
print(obj2.y)


# class syntax

# class ExampleClass(object):
#   class_attr = 0

#   def __init__(self, instance_attr):
#     self.instance_attr = instance_attr






class NameClass:
    def __init__(self, name,lname): #self stands for every object made in the class
         self.myname= name
         self.mylname= lname
         

person1= NameClass('siavash','salmani')
person2= NameClass('amir','dini')



print(person1.myname,person1.mylname)
print(person2.myname,person2.mylname)






#create a person with class __init__ func and object method functions

# Name=input("whats your name : ")
# Lname=input("whats your last name : ")
# Age=int(input("how old are you : "))


# class MyInfo:
#     def __init__(self,name,lname,age) :
#         self.my_name= name
#         self.my_lname= lname
#         self.my_age= age
        
#     def fullname(self):          #function for objects are called method
#         print(f'Hello my name is {self.my_name} and my lastname is {self.my_lname} and im {self.my_age} years old') 
 
        
# Me=MyInfo(Name,Lname,Age)

# Me.fullname()      #calling a method

# print(Me.my_name)
# print(Me.my_lname)
# print(Me.my_age)





class Car:
    def __init__(self, model,color,year):
        self.car_model= model
        self.car_color= color
        self.car_year= year
        
    def myCar(self):
        print(f'the car model is {self.car_model} and its color is {self.car_color} and it has been built in {self.car_year}')
        
        
car1=Car('corrola','brown','2008')

car1.myCar()

car1.car_model= 'supra mk4' # this is how to change an objects propertie

#del car1.car_color         # this is how delete a propertie

# del car1                  #  delete an bject

car1.myCar()











class Car:
    cars_count= 0
    def __init__(self,name,model,price):
        
        Car.cars_count +=1  # This is a method for counting the number of objects created in a class
        self.CarName= name
        self.CarModel= model
        self.CarPrice= price
        self.status = False

        
        
    def start(self):
        
        if self.status == False:
            print(f'the {self.CarName} Engine Turned ON')
            self.status= True
            
        else:
            print("your car is already on")
            
    def off(self):
        
        if self.status: #if ==True
            print(f' the {self.CarName}  turned off')
            self.status = False
            
        else:
            print('your car is already off!')
        
        
myCar1= Car('benz','2008','200')
myCar2= Car('BMW','2019','350')
myCar3= Car('pride','1991','50')

myCar1.start()
myCar1.start()
myCar1.off()
myCar1.off()





print(Car.cars_count)

myCar1.cars_count= 10   # if you  change a propertie from an onject its just aplly to that object
print(myCar1.cars_count)


print(myCar2.cars_count)

Car.cars_count= 15 # if you change a propertie from a class it will be apliied to all objects 
print(Car.cars_count)
print(myCar1.cars_count)
print(myCar2.cars_count)
print(myCar3.cars_count)