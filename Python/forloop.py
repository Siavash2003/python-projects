fruits=['apple','banana','pear','mango']

for x in fruits:
    print(x)
    if x=='pear':
         break
    print(x)
    
          
for x in fruits:
    
    if x=='pear':
        continue #this will stop the loop and goes to the next iteration
    print(x)
           
           
           
for numbers in range(10): #10 not included and start from zero
    print (numbers)
    
    
for numbers in range(2,6): #from 2 to 5
    print (numbers)
    
    
for numbers in range(2,11,2): #from 2 to 10 increment 3
    print (numbers)
else:                          #else in for loops execute when loop is finished
    print('finished')
    
    
    
colors=['red','blue','black']
cloths=['shirt','jeans','shoes']

for color in colors:
    for cloth in cloths:
        print(color,cloth)




#in this loop we pour any names with starting letter 's' in the second list

names=['sia','sadegh', 'reza','amin','sina','sobhan','mamad']

selectad_names=[]
 
for name in names :
    if name[0]=='s':
        selectad_names.append(name)  
        
print(selectad_names)




#in this loop we collect any duplicate that common both lists

names=['sia','sadegh', 'reza','amin','sina','sobhan','mamad']

names2=['mahdi','farbod','sia','kamyar','amin','sobhan','mamad']

common=[]

for name in names:
    for name2 in names2:
        if name==name2:
          common.append(name) #or name2

print(common)

b=[]

for i in names:
    if i[-1]=='a': #-1 is last index
        b.append(i)
        
print(b)



#we have a  name letter counter machine down here


name=input('what is your name: ')

name=name.lower()

name=name.replace(' ','') #we use this method to remove all white spaces in a string
b=[] 

for n in name:
     if n not in b:
        print(f'your name has {name.count(n)} {n}')
        b.append(n)
      
