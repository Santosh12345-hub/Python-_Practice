#Overloading Concept

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello"+name)
        else:
            print("Hello")

obj=Human()
obj.sayhello("scott")  #Helloscott
obj.sayhello()         #  Hello

#overloading 2

class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
obj1=calculation()
obj1.add()  #0
obj1.add(10,20)  #30
obj1.add(1,2,3) #6
