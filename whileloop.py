#while loop 
count = 1

while count < 5:
    print(count)
    count = count + 1


while count < 5:
    if count==4:
        break
    print(count)
    count=count+1


#for x in collection (list,dic,set)

for x in range(0,10,2): #start, stop ,besnt lechemer
    print(x)

total=0

for x in range(1,10,2):
    total += x
    #total = total + x   
    
print('sum =', total)
