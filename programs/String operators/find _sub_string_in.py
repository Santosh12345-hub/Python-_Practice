#finding substring in string using in keywords  : case sensitive

S='Explore our curated guide of expert-led courses, such as How to improve your'

print('santosd' in S)
print('ouy' in S)
print(' su' in S)
print('how' in S)
print('TO' in S)

print("Cheking in buld methods here........")
print(S.isalnum())   #false
print(S.find("of")) #availabe on 26 index
print(S.replace('our','your'))
print(S.swapcase())
print(S.startswith("your"))  #false
print(S.endswith("your"))   #True

#slicing
print(S[1:3]) #xp
