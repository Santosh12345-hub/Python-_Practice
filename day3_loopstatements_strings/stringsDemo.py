#Creating string variable

#Example 1:ways of creating string variable

s='welcome'
s="welcome"
s=str("welcome")
s=str('welcome')

#dont have any value - creating empty string variable
name=''
name=""
name=str()

#Example 1: how the memories gets change
#Mutable-  cannot  change the value of variable
#Imutable - can change the value of variable any time
#Strings are Imuatable

str1="welcome"
print(id(str1))   #id will get the id of the string i.g. 1908485045056

str1=str1+"to python"    #changed one
print(id(str1))  #2927600614256
#Note: here id's gets changed so string is imutable
#Note: if the value is changed after updation then it is imutable

#Example 3: how to use + and * with string
str="welcome"
print(str+"programming") #//concatenation/joining
print(str*2)  #welcomewelcome

#Example 4: Slicing [] : it will cut the string
#starting index=0
#ending index=1
s='welcome'
print(s[1:3]) #el
print(s[:6])  #welcom , here starting index is 0 by default
print(s[2:])  #lcome
print(s[1:-1]) #elcom ,last one char got removed
print(s[1:-2]) #elco , will remove last 2 chars

#Example 5: ord() and chr()
print(ord('A')) #65 -returns the ASCII code of the character
print(chr(65))  #A  -returns character represented by a ASCII number

#Example 6:max(),min() and len()

print(max("abc")) #c
print(max("abc")) #a
print(max("welcone")) #7

#Example 7: in , not in opertaors - return true/false
s="welcome"
print("come" in s)  #True
print("lome" in s)  #false

#not in is exctaly opposite of in operator

print("come" not in s)  #False
print("lome" not in s)  #True

#Example 8:String comparison returns true and false
#note: like in abc , c is the greater and a is the smaller

#Example 9: Testing strings True/false

s= "Welcome to Python"
print(s.isalnum()) #false - check whether string contains number or not
print("welcome".isalpha()) #True - check whether is contain aplha or not
print("1234".isdigit()) #true
print(s.isidentifier()) #fale - This will find some reserve words in python
print("WELCOME".isupper()) #True
print(" ".isspace()) #True

#Example 10:Searching for substrings

s= "Welcome to Python"
print(s.endswith("thon")) #True
print(s.startswith("good")) #false
print(s.find("come"))  #3
print(s.find("become")) #-1 : means not found
print(s.count("t"))  # 2 - Returns number of occurrences of substring the string

#Example 11: Converting String
s= "String in PYTHON"
s1=s.capitalize()  #String in python - 1st char of the sentence will be caps
print(s1)

s2=s.title()      ##String In Python - 1st letter of all words will be in caps
print(s2)

s3=s.lower() #string in python
print(s3)

s4=s.upper()  #STRING IN PYTHON
print(s4)

s5=s.swapcase()   #sTRING IN python
print(s5)

s6=s.replace("in","on")  #Strong on PYTHON
print(s6)

#Example 13: Reverse string
#method1:
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed string is:",rev_str)  #emoclew

#Method2: using slicing operator
s="welcome"
rev_str=s[::-1]  #[0:7:-1] [start:end:-1]
print(rev_str)                      #emoclew








