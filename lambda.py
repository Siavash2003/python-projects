# x = int(input('enter number : '))


# mylam= lambda num: num + 10  #lambda arguments : expression
 

# print(mylam(x))  
   
   
   
   
   
# lam2= lambda x,y,z : x*y+z # lambda can take any number of argument

# print(lam2(x=2,y=10,z=5))




# # def num(n):
# #     def num2(a):
# #         return a*n
    
# #     return num2
    
# # mydoubler = num(2)
# # mytripler = num(3)

# # print(mydoubler(2))
# # print(mytripler(5))



# #you can do this with lambda like this:



# def my_func(n):
#         return lambda a : a*n



# mydoubler= my_func(2)
# mytripler= my_func(3)

# print(mydoubler(2))
# print(mytripler(2))
    






# string=input('enter word : ')

# upper= lambda string : string.upper()
# print(upper(string))






#map function

my_num=[12,23,2,432,42,3,43]

def my_map(number):
        return number*10

x= map(my_map,(my_num)) #syntax= map(function,(iterable))

print(list(x)) # to make the map visible, we cast it to a list



def my_str(string):
        return len(string)
        
a= map(my_str,('sia','reza','mamad'))

print(list(a))


#using lambda for map function

list2=[12,32,4,23,3]
list3=[34,54,2,43,2]

lam_func= list(map(lambda a,b: a*b ,list2,list3)) # lambda arg : expression, iterable

print(lam_func)