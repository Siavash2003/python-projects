def my_password(password):
    if len(password)<8:
        print('your password must be at least 8 chars!')
    elif password.isnumeric(): 
        print('your password must contain at least one letter!') 
    elif password.isalpha():
        print('your password must contain at list one number!')
    else:
        print('this is a good password!')
        

while True :
    password= input('Enter your password : ')
    my_password(password)

