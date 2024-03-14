#declaring list of integer
list1=[10,20,30,40,50]

#printing list1
print("List elements are: ",list1)

#printing elements of list1 by index
print("Element @ 0 index:",list1[0])
print("Element @ 1 index:",list1[1])
print("Element @ 2 index:",list1[2])
print("Element @ 3 index:",list1[3])
print("Element @ 4 index:",list1[4])

# declaring list with string elements
list2 = ["New Delhi", "Mumbai", "Chennai", "calcutta"]
print("List2 elements are: ",list2)

#printing elements of list1 by index
print("Element @ 0 index:",list2[0])
print("Element @ 1 index:",list2[1])
print("Element @ 2 index:",list2[2])
print("Element @ 3 index:",list2[3])
#print new line
print()

# declaring list with mixed elements
list3 = ["Amit Shukla", 21, "New Delhi", 9876543210]

#printing list3
print("List elements are: ", list3)

# printing elements of list3 by index
print("Element @ 0 index (Name) :", list3[0])
print("Element @ 1 index (Age ) :", list3[1])
print("Element @ 2 index (City) :", list3[2])
print("Element @ 3 index (Mob.) :", list3[3])
print() # prints new line


# Iterating over the elements
for x in list1:
    print(x)

print(list1[3:]) #print all elemets from the 3rd index