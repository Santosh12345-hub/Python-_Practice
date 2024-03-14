list=[10,20,30,40,50]
#print without using for loop
print(list)

print()  #printing new line
#print using for loop
for l in list:
    print(l)

print()

#calculating sum of all elements using sum()

total = sum(list)
print(total)

#approach 2 : without using sum function
total2 =0
for i in list:
    total2 += i
    print(total)



