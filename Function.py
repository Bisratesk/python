#creating a function
def greet():
    return 'hello'

print(greet()) #simple function

def greet(name,mid_name='alex',last_name='bisrat'):
    return 'hello ' + name + last_name + mid_name

print(greet('hanna',last_name='kebede'))
#three type of arguments: positional,default,keyword
#postional argument cannot appear after a keyword