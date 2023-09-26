def hi(name):
    print(f'hello {name}')
    
hi('siavash')


def sub(a,b):
    num= a*b
    print (num)
sub(10,10)


class Car:
    def __init__(self,model,color):
        self.model=model
        self.color=color
        
    def printcar(self):
        print(f"the model of car is {self.model} and its color is {self.color}")
        
        
mycar=Car("bmw","blue")



mycar.printcar()



info={
    'name':'siavash',
    "lname":'salmani'
}