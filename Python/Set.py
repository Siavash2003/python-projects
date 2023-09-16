this_set = {'sia','ali','sia',12,'mamad'}  

this_set2 = {12,32,2123,'sia',12,323,54} 

#sets are unordered which mean items will apear in random order

print(this_set)

#this will check if a value exist in a set

print('ali' in this_set) 

this_set.add('reza')

print(this_set)

#this will merge up two sets

this_set.update(this_set2) #you can also merge lists and tuples with sets

this_set.union(this_set2) #merge two sets

#both union and update will exclude any Duplicates

this_set.remove('reza')

this_set.discard('hadi') #use discard to not raise error if that item does not exist

print(this_set)

# this_set.clear() #clears out the whole set

print(this_set)

set={12,23,12,23,1,2334,5}
set2={12,23,45,34,5,435,56}

set.intersection_update(set2) #this will only keep items that are in both sets

print(set)

set3= set.intersection(set2)

print(set3)

set.symmetric_difference_update(set2) #keeps all but the duplicates common in both sets

print(set)

set4= set.symmetric_difference(set2)

print(set4)


name1={'sia','reza','ali'}
name2={'sia','majid','ali'}

print(name1 | name2) # pipe symbol merge up two sets
print(name1 & name2) #ampersand symbol print common duplicats
