#Example 1 : creting dictinary

myDic={101:"x",102:"y",103:"z"}
print(myDic) #{101: 'x', 102: 'y', 103: 'z'}

#Example 2: Accesing items from dictinary
myDic={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }

print(myDic["brand"]) #Hundai
print(myDic["model"]) #i10

   #using get()
print(myDic.get("brand")) #Hundai

#Example 3:change values in dictinary
myDic={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }

print(myDic)        #{'brand': 'Hundai', 'model': 'i10', 'yesr': 2021}
myDic["yesr"]=2023
print(myDic)        #{'brand': 'Hundai', 'model': 'i10', 'yesr': 2021}

#Example 4: reading items from dictinary using loop
myDic={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }
for i in myDic:
    print(i)  #it will print only keys from the dictinary

for i in myDic:
    print(myDic[i]) #it will print only values from the dictinary

for i in myDic.values():
    print(i)       #it will print only values from the dictinary

for x,y in myDic.items():
    print(x,y)    # print keys along with value

#Example 5: check key is exist in dictinary or not
myDic={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }

if "model" in myDic:
    print("exsit")  #exsit
else:
    print("not exist")

#Also can write single statement

print("model" in myDic)  #True

#Example 6: fine number of items present in dictinary
myDic={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }
print(len(myDic)) #3

#Example 7 : Adding items to the dictinary
myDic["color"] = "red"
print(myDic)   #{'brand': 'Hundai', 'model': 'i10', 'yesr': 2021, 'color': 'red'}

#Example8: remove item from dictinary

myDic.pop("yesr")
print(myDic)  #{'brand': 'Hundai', 'model': 'i10', 'color': 'red'}

del myDic[2021]   # delete bases on item

#To delete the items of the dictinary
# del myDic  # this to delete complete dictinary
# print(myDic) #Name Error: name ' myDir' is not defined so go for clear()

myDic.clear()
print(myDic) #{}

#Example 9: Copying Dictinary
myDic1={ "brand": "Hundai",
       "model" : "i10",
       "yesr" :2021
        }

myDic2=myDic1
print(myDic2)

#Usingg copy()

myDic2=myDic1.copy()
print(myDic2)

#without using copy()
myDic2=myDic1
print(myDic2)










