#Example 1 : How to create tuple

myTuple=("orange","apple","cherry")
print(myTuple) #('orange', 'apple', 'cherry')
myTuple=() # empty tuple

#Example 2: Accesssing items from the tuple
myTuple=("orange","apple","cherry")
print(myTuple[1])  #apple
print(myTuple[-1]) #cherry


#Example 3: Range of indexs
myTuple=("apple","banana","cherry","kiwi","melon","mango")
print(myTuple[2:5]) #('cherry', 'kiwi', 'melon')
print(myTuple[-4:-1]) #('cherry', 'kiwi', 'melon')

#Example 4: change item value
#by default tuple does not allow you to change values because it is imutable
#but there is a work around
#tuple-->list(modify)--->tuple

myTuple=("orange","apple","cherry")
mylist=list(myTuple) #convert from tuple to list
mylist[0]="mango"    #modify

myTuple=tuple(mylist) # again convert from list to tuple after modify
print(myTuple)       #modified : ('mango', 'apple', 'cherry')

