#Approach 1 : calling class method from another module

import ex3_class_m1
import  ex3_class_m2

obj1=ex3_class_m1.Animal()
obj1.display()      #I like cow
obj2=ex3_class_m2.Bird()
obj2.display()   #I like parrot


#Approach 2

from ex3_class_m1 import Animal
from ex3_class_m2 import Bird

obj1=Animal()
obj1.display()

abj2=Bird()
obj2.display()

