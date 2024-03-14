#This is considered as module 2
#Approach 1

# import Calculator_Module
# Calculator_Module.add(10,20) #30
# Calculator_Module.mul(2,4) #8


#Approach2 (best way to use no need to call module1 repeatedly)

from Calculator_Module import add,mul
add(2,1) #3
mul(1,1) #1

#Approach3 : if many functions are there (* is mathing all function)

from Calculator_Module import *
add(2,1) #3
mul(1,1) #1