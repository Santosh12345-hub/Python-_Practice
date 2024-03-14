#Exampl 1:

class myClass:
    def myFun(self):
        pass    #pass  becz empty body
    def display(self):
        print("John")
    def display2(self,name):     #method with passing argumnet
        print(name)

mc1=myClass()
mc1.myFun()   #so output will be nothing
mc1.display() #John
mc1.display2("Scott")  #Scott

#Example 2
class myClass2:
    def m1(self):    #Self is representing class
        print("This is the instance method..")
    @staticmethod
    def m2(self,num):    #Hence its staic method need to pass argumnet for self as well
        print(self,num)
mc2=myClass2()
mc2.m1()
mc2.m2(100,200)

myClass2.m2(10,20) #10 20 : Here calling static method directly using class not through object


#Example 3:
class myClass3:
    a=10
    b=20  #Class variable
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
mc3=myClass3()
mc3.add()  #30
mc3.mul()  #200

#Example 5 : Combination of global,class and locan variables with different variable name

i,j=15,25  #Global variables
class myClass4:
    a,b=10,20  # class variables
    def add(self,x,y):
        print(x+y)     #local variables
        print(self.a+self.b)  # a,b are class variables
        print(i+j)       #global variables

mc4=myClass4()
mc4.add(100,200)

#output - 300  30 40

#Example 5: same like example 4 but here variable names are same
a,b=15,25  #Global variables
class myClass5:
    a,b=10,20  # class variables
    def add2(self,a,b):
        print(a+b)     #local variables
        print(self.a+self.b)  # a,b are class variables
        print(globals()['a']+globals()['b'])       #global variables

mc5=myClass5()
mc5.add2(100,200)

#Example 6: One class can have multiple objects

class myClass6:
    def display(self,name):
        print("This is display method..")
        print(name)

obj1=myClass6()
obj1.display("scott")

obj2=myClass6()
obj2.display("John")


#Example 7: Constructor example

class myclass7:
    def __init__(self):  #define constructor /default constructor as its not taking any arguments
        print("This is a constructor..")

    def med(self):
        print("This is a method...")
    def med2(self,x,y):
        return (x+y)

mc7=myclass7()  #invoke construtor automaticall
mc7.med()       #Method we have call explicitly by using object
print(mc7.med2(10,20)) #30


#Exampale 8:

class myClass8:
    name="john"
    def __init__(self,name):  #Constructor expecting one argument
        print(name)      #pAIK
        print(self.name) #john
mc8=myClass8("pAIK")    #passing parameter to the constructor

#Example 9:
#Req: Emp
   # constructor : eid , name , sal
   #display() : print eid , ename & sal

class Emp:
    def __init__(self,eid,name,sal):
        self.eid=eid       ##making the variable as class label
        self.name=name
        self.sal=sal

    def display(self):
        print(self.eid,self.name,self.sal)


mc9=Emp("10","john","1000")
mc9.display() #10 john 1000

#Example 10:
#Req: Emp
   # constructor : eid , name , sal
   #display() : print eid , ename & sal

class Emp:
    def __init__(self,eid,name,sal):
        self.eid=eid       ##making the variable as class label
        self.name=name
        self.sal=sal

    def __str__(self):  # Invalid becaoze  __stry()__ returns only string data
        print(self.name)


mc9=Emp("10","john","1000")

print(mc9)




