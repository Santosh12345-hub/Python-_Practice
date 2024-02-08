#Example 1:

def func(i,j):
    print(i,j)

func(10,20) #Positional arguments - based on position it takes the value

func(j=30,i=40) #keyword arguments - position is not matter here and jumble the parameters
#Example 2: default value assigned to positional arguments
def fun(i,j=10):   #default value can be assigned to both parameeters
    print(i,j)
fun(100,200) #100 200
fun(20)          #20 10

# note: both default value is assigned then no need to paas any value
def fun2(i=10,j=90):
    print(i,j)
fun2()

#Example 3: Keyword arguments
def greeting(name,greetings):
    print(greetings+ " " +name)
greeting(name="John",greetings="Hello")  # Hello John
greeting(greetings="Hi",name="Scott")    # Hi Scott

#Example 4: Combination of positional and keyword arguments
def myFun(a,b,c):
    print(a,b,c)
myFun(10,20,30)  #positional arguments
myFun(a=10,b=12,c=34)    #Keyword arguments
myFun(b=12,c=21,a=34)    #Keyword arguments

#combination
myFun(10,20,c=30) #valid
myFun(10,b=20,c=30) #valid
#myFun(10,b=20,30)   #invali - postional arg must appear before the keyword
#myFun(10,20,b=30)  # TypeError: myFun() got multiple values for argument 'b' -LOGICALLY INVALID

#Example 5:Function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

#Printing largest number
print(largest(100,200)) # (200, 100)
print(largest(10,20))  # (20, 10)
print(2,1)  #2 1





