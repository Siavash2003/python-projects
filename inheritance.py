class person: #parent
    def __init__(self,name,lastname):
        self.my_name=name
        self.my_lastname=lastname
        
    def info(self): 
        print(self.my_name,self.my_lastname)
        


class student(person):   # child
        pass

student1=student('saeid','azizi')
student2=student('hadi','rezaei')

student1.info()
student2.info()

    

    
class own(person): 
    def __init__(self, name, lastname,age):
     super().__init__(name, lastname)  # super acts like parent class
     
     self.my_age=age
     self.graduationYear= 2020
     
    
    def printAge(self):
        print(f'age is {self.my_age}')
        
owner=own('hamed','razavi',32)

owner.info()
owner.printAge()
print(owner.graduationYear)
