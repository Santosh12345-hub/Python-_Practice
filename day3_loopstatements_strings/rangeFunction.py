#range() function : values between the range

print(range(10)) #range(0, 10)
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10))) #[5, 6, 7, 8, 9]

#print only odd number between 1-10
print(list(range(1,10,2)))  #[1, 3, 5, 7, 9]

#print only even number between 1-10
print(list(range(0,10,2))) #[0,2, 4, 6, 8]

#Negative statemenets
print(list(range(10,1,-1)))  #[10, 9, 8, 7, 6,5,4,3,2]

print(list(range(-10,-5)))   #[-10, -9, -8, -7, -6]
print(list(range(-10,-5,2))) #[-10, -8, -6]

a=list(range(10,1,-1))
print(a[-1])

