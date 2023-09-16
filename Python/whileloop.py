a= 10
b=20

while a<b:
    a+=1
    if a==15: #with break statement you can stop the loop even if the condition is true
     break 
    print(a)
    
while a<50:
    a+=5
    if a==30:
      print(a)
      continue #continue statemnt will stop current loop and go to the next one