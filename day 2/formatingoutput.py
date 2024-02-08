# name='john'
# age=30
# sal=5000.50

name,age,sal = 'john',30,5000.50


#Approach 1 : to print some meaningfull data

# print(name)
# print(age)
# print(sal)
# print(name,age,sal)

#Approach 2: print op with some meaningfull message

# o/p -
# Name is: john
# Age is: 30
# Sal is: 5000.5

print("Name is:",name)
print("Age is:",age)
print("Sal is:",sal)

#Approach 3:
print("Name is:%s Age is:%d Sal is:%g" %(name,age,sal)) #op: Name is:john Age is:30 Sal is 5000.5

#Approach 4:
print("Name is:{} Age is:{} Sal is:{}".format(name,age,sal))#op-Name is:john Age is:30 Sal is 5000.5
print("Age is:{} Age is:{} Sal is:{}".format(age,name,sal)) #op: Age is:30 Age is:john Sal is:5000.5








