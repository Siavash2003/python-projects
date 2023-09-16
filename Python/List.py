list1= ["sia",23,"hello",543,True,4.3]  #lsits can contain any types of data

print(list1)


print(list1[1])  #lists Index is same as string index

print(len(list1))  #counts items in a list

list1[1] = "siavash" #changes items in a list

list1[1:3] = ["siavash" , "salmani"] #changes multiple items in a list

list1.insert (0,'reza') #inserts items in a list

list1.append ("mamad")  #adds an item to the end of the list


friends= ['sia','reza','ali']

newfriends=('mamad','amin')

print(list1)

friends.extend(newfriends) #combines two lists or tuple  together

print(friends)

  
                #these are methods for removing item from a list


friends.remove('sia')

friends.pop(2)  #pop removes item by index  if you leave () empty it will remove the last item


del friends[0]  #this will delete item and if you leave index empty it will delete the whole list

# friends.clear()   this will clears out the list items but the list remains

print(friends)


fruits= ['apple','banana','mango']

x,y,z= fruits   #this is called unpacking 

print(x)
print(y)
print(z)


Names=['sia','ali','reza' ,'Zahra'] #upperCase is in Priority
Names.sort()
print(Names)
Age=[12,43,23,21]
Age.sort()
print(Age)
Age.sort(reverse=True) #this will reverse the priority
print(Age)



family=['ahmad','reza','siavash'] #there are two methods to duplicate a list

friends=family.copy()

friends=list(family)

newfriend=input('new friend name : ')

friends.append(newfriend)

print(friends)
