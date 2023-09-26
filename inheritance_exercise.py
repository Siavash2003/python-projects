
cs=[
    
    {
        'title':'python',
        'teacher':'Amiri'
    },
    
    {
        'title':'HTML',
        'teacher':'Dehyami'
    },
    
    {
        'title':"PHP",
        'teacher':'Enayati'
    }
    
]






class User:
    def __init__(self,name,lname):
        self.name=name
        self.lname=lname
        self.courses=[]
        
        
    def fullname(self):
        print(f'your fullname is {self.name} {self.lname}')
        
        
U1= User('amir','karimi')

U1.fullname()



class Student(User):
    def __init__(self, name, lname,age,grad_year):
        super().__init__(name, lname)
        
        self.age=age
        self.graduation=grad_year
        
        
    def fullname(self): #with super() func we can change the parents methods
         super().fullname()
         print(f'your age is {self.age} and you graduated in {self.graduation}')
    
    def printCourse(self):
        if self.courses:  #if be empty will raise False and below condition wont execute
            for course in self.courses:
                print(course.get('title'))
        else:
            print('you dont have any course')
St1=Student('siavash','salmani',20,2023)

St1.fullname()

St1.courses.append(cs[0])     # add baught course to the courses[] list

St1.printCourse()


class Teacher(User):
    def __init__(self, name, lname,email):
        super().__init__(name, lname)
        self.email=email
        
    def fullname(self):
        super().fullname()
        print(f'your email is {self.email}')
        
Tch1= Teacher('reza','mohamadi','reza@gmail.com')

St2= Student('ali','karami',23,2018)

St2.courses.append(cs[2])
St2.courses.append(cs[1])


Tch1.fullname()
St2.fullname()

St1.printCourse()
St2.printCourse()