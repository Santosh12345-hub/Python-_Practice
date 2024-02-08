## Break     continue

for i in range(1,10):
    if i==5:         #this will break when condition match
        break
    print(i)         #1..4

for i in range(1,10):
    if i==2 or i==4 or i==6:   #this will skip
        continue
    print(i)  # 1, 3, 5, 7,8,9