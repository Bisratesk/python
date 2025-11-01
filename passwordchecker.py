
age = int (input('enter age: ') ) #by defalit everything you enter in the input is considered a string
if(age > 18):      #when forming loops follow indentaction
    print('adult')
    
elif(age==18):
    print('pass')
else:
    print('under age')


password=input('enter password: ')
if(password.isupper()):
    print('false')

elif(password.islower()):
    print('false')
elif(password.isdigit()):
    print('false')
elif(password.isalpha()):
    print('false')
else:
    print('pass')


