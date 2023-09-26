userName=input('type your UserName : ')

def validate(userName):
        if len(userName)<8:
            return False
        else:
            return True
        # elif userName.isnumeric():
        #     return False
        # elif userName.isalpha():
        #     return False
if validate(userName):
    print('success!')
else:
    print("failed!")
        
        
        
        
validate(userName)







