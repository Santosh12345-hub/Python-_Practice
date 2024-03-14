class A:
    def m1(self):
        print("This is method from the class A")

class B(A):
    def m2(self):
        print("This is the method from class B")


obj=B()
obj.m1()  #This is method from the class A
obj.m2()  #This is method from the class B

#Example 2: Single Inheritance

class C:
    x,y=10,30
    def m3(self):
        print(self.x+self.y)
class D(C):
    a,b=200,100
    def m4(self):
        print(self.a-self.b)

bobj=D()
bobj.m3()  #40
bobj.m4()  #100

#Example 3 :Multil level inheritance

class E:
    x,y=10,30
    def m5(self):
        print(self.x+self.y)
class F(E):
    a,b=200,100
    def m6(self):
        print(self.a-self.b)

class G(F):
    d,g=400,100
    def m7(self):
        print(self.d-self.g)

bobj=G()
bobj.m5()  #40
bobj.m6() #100
bobj.m7() #300

#Example 4 :Heirarchy   inheritance

class E:
    x,y=10,30
    def m5(self):
        print(self.x+self.y)
class F(E):
    a,b=200,100
    def m6(self):
        print(self.a-self.b)

class G(F):    #G is the grand child and it conatins all methods
    d,g=400,100
    def m7(self):
        print(self.d-self.g)

bobj=G()
bobj.m5()  #40
bobj.m6() #100
bobj.m7() #300

#Example 4 :heirarchy inheritance : here mwthod will not have access  from F when G obj is created

class E1:
    x,y=10,30
    def m5(self):
        print(self.x+self.y)
class F(E1):
    a,b=200,100
    def m6(self):
        print(self.a-self.b)

class G(E1):
    d,g=400,100
    def m7(self):
        print(self.d*self.g)

bobj=G()
bobj.m5()  #40
bobj.m7() #40000

bobj=F()
bobj.m6() #100

#Example 5 :Multiple  inheritance : multple parent and single child

class P1:
    x,y=10,30
    def m5(self):
        print(self.x+self.y)
class P2:
    a,b=200,100
    def m6(self):
        print(self.a-self.b)

class C(P1,P2):
    d,g=400,100
    def m7(self):
        print(self.d*self.g)

bobj=C()
bobj.m5()  #40
bobj.m7() #40000
bobj.m6() #100

#Note: So c class will have all the methods from other class

#Example 5: super() : Calling parent class method using child class

class I:
    def Md(self):
        print("This is the method comes from class I")

class J(I):
    def Md(self):
        print("This is the method comes from class J")
        super().Md()   #it will give method from class I 

objc=J()
objc.Md()