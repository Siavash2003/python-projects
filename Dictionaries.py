thisdict={                #they are pairs of key:value 
    'Name':'Siavash', 
    'Lname':'Salmani',    #dicts cna carry any types of data
    'Age':20,
    'Age':21,              #an item cannot have two same keys and if does the second will overwrite the first
    'Friends':['ali','mamad','reza']
}

print(thisdict)
print(len(thisdict))
 
 
info=thisdict['Name']#accessing a value by its key in[]
info=thisdict.get('Name') # using .get method to hire a value


Key=thisdict.keys() #will get all keys in the dict


print(info)
print(thisdict)

print(Key)

info_add=thisdict['city']='FooladShahr'

print(thisdict)
print(Key)

values=thisdict.values() #return all of the values in dict
print(values)


items=thisdict.items() #wil show value pairs as a tuple in a list
print(items)

check='Name' in thisdict
print(check)


if 'Name' in thisdict :
  print('yes!name is included')
  
  
  
thisdict.update({'bestie':'Ashkan'}) #u can add or change items with update function
thisdict.update({'Name':'Mohammad'})


thisdict['country'] = 'iran'  #u can add or change items
thisdict['Age'] = '19'


thisdict.pop('bestie') #will delete item


thisdict.popitem() #will delete last item

del thisdict['Friends'] #if be empty will del whole dict

# thisdict.clear will empties the dict

print(thisdict)


thisdict2=thisdict  #if you changee anything in thisdict1 it will be made in thisdict2

thisdict2['pet']='dog'

print(thisdict2)
print(thisdict)


dict2=thisdict.copy()

dict2['Name']='reza'
print(dict2)
print(thisdict)


dict2=dict(thisdict)
dict2['state']='esfahan'
print(dict2)
print(thisdict)


#nested Dictionaries

family ={
  'child1':{
    'name':'ali',
    'age' :'12'
  },
  'child2':{
    'name':'reza',
    'age': '23'
  },
  'child3':{
    'name':'maryam',
    'age': '16'
  },
}

print(family['child1'])
print(family['child1']['name'])



#here is another method 

child1={
   'name':'ali',
    'age' :'12'
}


child2={
  
    'name':'reza',
    'age': '23'
}


myfamily={
  'child1':child1, # we call both child variables and dont need to type their values
  'child2':child2
  
}


#how to create a dict with fromkey method

x=('key1','key2','key3')
y=12

numbers=dict.fromkeys(x,y) #(keys,values)

print(numbers)