name='hanna'
print(name[0])

names=list()
names=['hanna','alex',1,3,4,5,6,True]
print(type(names))
print(len(names)) # len means length
print(names[1])

#negative indexing starts with -1



# list unpacking

names=['hanna','alex','abel','yakob','micky',]
first,second,*third,= names  
#first is for hanna and second is for alex and *third means print out the rest
print(names)


#slicing

new_list=names[2:4]
print(new_list)



#modifying

names[4]='alem'
print(names)


#checking element in a list

print('bisrat' in names)

#adding items to the list

names.append('bisrat')
print(names)

#instering items in specific index

names.insert(2,'one')
print(names)


# names.clear() clear all the elements

new_list=names.copy() #copying a list
print(new_list)

















