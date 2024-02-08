#Example1:
global_var=10

def func():
    local_var=20
    print(local_var)  #20
    print(global_var) #10

func()

#print(local_var)  #NameError: name 'local_var' is not defined. Did you mean: 'global_var'?
print(global_var) #10

#Example 2:
xy =100

def fun():
    xy=200    #consider as a local variable only
    print(xy)
fun()   #200

#Example 3: using Global variable in Local variable and update value
xy =500
def cool():

    # global xy=440 - invalid statement in python

    global xy   # here we haVE CHANGED the value  of glabl variable
    xy=400
    print(xy)
cool()  # 400, similarly wwe can call out side of the fucntion as its global
print(xy) #400

#Example 4:
xy =100
def cool():
    global xy   # here we haVE CHANGED the value  of glabl variable
    xy=400
    print(xy)
#cool()  # 400, similarly wwe can call out side of the fucntion as its global
print(xy) #100

#Example 5:
#There is no need to declare global varibale outside of the function
#yoo can declare them global inside the function
def cool():
    global x
    x=20
    print(x)
cool()   #20
print(x) #20 - able to access x becoz its global varibale with out declaring outside of the func


