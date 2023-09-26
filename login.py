users ={
    'sia':'sia12',
    'amir':'1232',
    'reza':'32we',
}

login_username=input('enter your username : ')
login_pass=input('enter your password : ')


while login_username not in users or users[login_username]!=login_pass:

    login_username=input('enter your username again : ')
    login_pass=input('enter your password again : ')

print('you successfully logged in!')



