import math
nameinput=(input('enter name: '))
ageinput=int(input('enter age: '))
genderinput=(input('enter gender: '))
weightinput=float(input('enter weight: '))
heightinput=float(input('enter height: '))


bmr_male=10*weightinput +6.25*heightinput - 5* ageinput +5
bmr_female=10*weightinput +6.25*heightinput - 5* ageinput- 161
BMI=weightinput/heightinput
#whatif i wanted to calculate either individually

if genderinput== 'male':
    print(str(bmr_male))
    print(str(BMI))
else:
    print(str(bmr_female))
    print(str(BMI))

