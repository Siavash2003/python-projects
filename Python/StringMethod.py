txt= '  hello im siavash and im from iran {} and im {}  '

print(txt.capitalize())    #this will make first Char UppersCase

print(txt.casefold())      #this will make first Char lowerCase

print(txt.count('m'))      # this will Count the number of times that a value repeated in a string

print(txt.find('iran'))    #this will find the posithion of a specific character or word

print(txt.format('country','20')) # this wil turns specific value to string

print(txt.strip())         #this will remove unneeded space 
    
print(txt.upper())         #this will turns all of characters into uppercase

print(txt.lower())         #this will turns all of characters into lowercase

print(txt.title())         #this will convert firts character of each word to UpperCase

print(txt.__len__())       #this will count the number of characters in a string

print(txt.replace('s','w')) # this method will replace a specific value with given value