#Example 1: Creating set

mySet={"appple","banana","cherry"}
print(mySet)  #{'cherry', 'banana', 'appple'} -unordered output

#Example 2: Access items from set : this only possible thorugh for loop
mySet={"appple","banana","cherry"}
for i in mySet:
    print(i)

#Example 3: Value exists in set or not
mySet={"appple","banana","cherry"}
print("appple" in mySet) #True
print("mango" in mySet)  #False

#Expale 4: Adding items in set
 #add() -single item   update() - multiple items can be add -also ([]) need this when updates

mySet={"appple","banana","cherry"}
mySet.add("orange")
print(mySet)  #{'appple', 'banana', 'cherry', 'orange'}

mySet.update(["Grapes",2,"mango"])
print(mySet) #{2, 'cherry', 'appple', 'mango', 'Grapes', 'banana', 'orange'}

#Example 5; find number items in the set
mySet={"appple","banana","cherry"}
print(len(mySet)) #3

#Example 6:Remove items from the set - remove() , discard()
mySet={"appple","banana","cherry"}
mySet.remove("banana")
print(mySet)    #{'appple', 'cherry'}
# mySet.remove("xyz")
# print(mySet)    #key error as XYZ is not present

mySet.discard("banana")
print(mySet)    #{'appple', 'cherry'}
mySet.discard("xyz")
print(mySet)    # will not throw any error even though item is not present

#Example 7 : clear all items from set
mySet={"appple","banana","cherry"}
mySet.clear()   #clear function just clear the value from the set
print(mySet)    #set()

# del mySet      #del keyword will complete delete the set variable along with data
# print(mySet)   #NameError: name 'mySet' is not defined

#Example 8: join two sets -union()
set1={"a","b","c"}
set2={1,2,3}
print(set1.union(set2))  #{1, 2, 'c', 3, 'b', 'a'}

#update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1) #{1, 2, 'a', 3, 'c', 'b'}







