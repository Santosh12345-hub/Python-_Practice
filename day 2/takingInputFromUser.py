num1 = input("Enter 1st number")
num2 = input("Enter 1st number")

print(type(num1)) #str
print(type(num2)) #str
print(num1+num2) #op-100200 because it consider as string so concat happens

# approach 1
n1 = int(input("Enter 1st number"))  #type conversion
n2 = int(input("Enter 1st number"))

print(type(n1))   #int
print(type(n2))   #int
print(n1+n1)  #30

# approach 2

num1 = input("Enter 1st number")
num2 = input("Enter 1st number")
print(int(num1)+int(num2)) #300

#ex for decimal

s1 = input("Enter 1st decimal number")
s2 = input("Enter 1st decimal number")
print(float(s1)+float(s2)) #10.5

