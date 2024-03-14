#Example 7 :variables
#
# class A:
#     a,b=10,30
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)  #local variable
#         print(self.i+self.j) #class variable
#         print(self.a+self.b)
#
# objb=B()
# objb.m(1000,2000)   #o/p - 3000 ,300, 40

#Example 8 : Varibale overriding

class parent:
    name="scott"
class child(parent):
    name="John"       #overriding the variable

cobj=child()
print(cobj.name)   #John

#Ex:8 -Overriding methods

class Bank:
    def ROI(self):
        return 0
class XBank(Bank):
    def ROI(self):
        return 10
class YBank(Bank):
    def ROI(self):
        return 12
obj=XBank()
print(obj.ROI()) #10

obj2=YBank()
print(obj2.ROI()) #12

