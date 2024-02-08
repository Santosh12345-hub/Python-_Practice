#Example 1 : How to create list

myList1=[10,20,30,40,50]
myList2=["orange","apple","cherry"]
mylist3=["apple",10,"bannana",20]
myList=list()  #empty list

print(myList1)
print(myList2)
print(mylist3)
print(myList)

#Example 2: Accesssing items from the list
myList=["apple","banana","cherry"]  #index starts from 0

print(myList[0])
print(myList[2])
print(myList[-1]) #cherry - last value of the list
print(myList[-2]) #banana -print 2nd last value of the list

#Example 3: Range of indexs

myList=["apple","banana","cherry","kiwi","melon","mango"]
print(myList[2:5]) #['cherry', 'kiwi', 'melon']
print(myList[-4:-1]) #['cherry', 'kiwi', 'melon']

#Example 4: change item value
myList=["apple","banana","cherry"]
print(myList) #['apple', 'banana', 'cherry']

#changing value by index

myList[0]="orange"
print(myList) #['orange', 'banana', 'cherry']

#Example5 : Read the list items using loop - instead of print one by one
myList=["apple","banana","cherry"]
for i in myList:
    print(i)

#Example 6:Check the apple itme is in present in the list or not
myList=["apple","banana","cherry"]
if "apple" in myList:
    print("Item is present")
else:
    print("item is not present")

#Example 7: List length(Counting the number of item in list)
myList=["apple","banana","cherry"]
print(len(myList)) # 3

#Example 8: Adding new items in the list : append() , insert()
myList=["apple","banana","cherry"]
myList.append("orange") #adding new items in the end of the list
print(myList)
myList.insert(1,"mango")  # add item any place of the list based on index
print(myList)

#Example 9: removing single  item using pop() based on the index or using del- keyword
myList=["apple","banana","cherry"]
myList.pop(0)
print(myList) #['banana', 'cherry']  Note only through index we can delete

#del - keyword
#clear() - it will clear all the items and makes list empty
myList.clear()
print(myList)

#Example10: Copy List
#List()
myList1=["apple","banana","cherry"]
myList2=list(myList1)
print(myList1,myList2)

#copy()
myList1=["apple","banana","cherry"]
myList2=myList1.copy()
print(myList1,myList2)

#Example 11: combine/join lists
#->Using + opertaor
list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)  #['a', 'b', 'c', 1, 2, 3]

#->using for loop
list1=['a','b','c']
list2=[1,2,3]
for i in list2:
    list1.append(i)
print(list1)      #['a', 'b', 'c', 1, 2, 3]

#-> using extend()
list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)  #['a', 'b', 'c', 1, 2, 3]











