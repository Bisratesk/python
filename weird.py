
number=int(input('enter a number: '))

if(number%3==0):
    print('weird')
elif(number%2==0 and number>1 and number<6):
    print('NOT WEIRD')
elif(number%2==0 and number>6 and number<20):
    print('weird')
elif(number%2==0 and number>20):
    print('not weird')

