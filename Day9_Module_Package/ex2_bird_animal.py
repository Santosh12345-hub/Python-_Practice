# Module 3 : here we can import and call the functions from both module 1 and 2

#Approach 1 (This is best approach)

# import ex2_Animal
# import ex2_bird
#
# ex2_Animal.fly()
# ex2_Animal.color()
#
# ex2_bird.fly()
# ex2_bird.color()

#Approach 1

from ex2_Animal import *
fly()
color()

from ex2_bird import *
fly()
color()
