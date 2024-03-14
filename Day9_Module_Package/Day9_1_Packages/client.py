##This  is not part of the Pack1 , its an extranal]

##sys comes from python and need to pass the Pack1 path and use forward slash beacuse python can not recognize backword slash
import sys
sys.path.append("C:/Users/santo/PycharmProjects/pythonProject/Day9_Module_Package/Day9_1_Packages/Pmack1")

#Approach 1
# import module1
# import module2
#
# module1.display()
# module2.show()

#Approach 2

from module1 import *
from module2 import *

show()
display()




