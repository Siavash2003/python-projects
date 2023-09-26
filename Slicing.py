a= 'Hello World!'

print(a[2])      # this will print 'l' because first character position is '0'

b= 'Hello World!'

print(b[2:5])     #5th character wont be in output because it stops at 4th

c= 'Hello World!'

print(c[2:])      #this will print 2th char to end 

d= 'Hello World!'

print(d[:4])      #this will print from first to 4th char 

e= 'Hello World!' #this is negative index and will print chars opposite direction

print(e[-4:-2])   #last char position is always -1
