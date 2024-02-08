#Example 1:

def myfun():     #def used to create the function
    print("hello")
myfun()   #call the function

#Example 2: argument passing
def myfun(name):
    print("Hello",name)
myfun("santosh")

#Example 3: 2 arguments with return the results

def cal(a,b):
    return (a+b)

s=cal(10,20)
print(s) #30    Note both way we can write
print(cal(100,200)) #300

#Example 4:

def func():
    return
print(func()) #none
def func2():
    i=10
print(func()) #none

#Note: Both returns none ,not even null as not mention anything not mention the return





