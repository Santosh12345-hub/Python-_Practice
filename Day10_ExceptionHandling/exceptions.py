#Example1

# print("Hello...........")
# print("Hello 2")
#
# try:
#     print(x)
# except:
#     print("Exception occured")
#
#
# print(" Hello......after exception.....")
# print("Hello 2")


#Example 2: Multiple except blocks - try ,except else ,finally
try:
    num1,num2=10,0
    result=num1/num2
    print("Result is:", result)

except ZeroDivisionError:
    print("Throw ZeroDivisionError exception")

except SyntaxError:
    print("Throw SyntaxError exception")

except:
    print("Exception handled...")
else:
    print("No Exception occured")
finally:
    print("Always execute..")

#Example 3: Raising our own exception(User defined exception) using raise -keyword and ValueError

def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("Even")
    else:
        print("Odd")

print("checking number is even or odd by calling functions..")
num=-1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled")
print("program completed")











