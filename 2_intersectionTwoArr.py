list=[1,2,3,4,5,6]
list2=[2,4,6,8,10,12]
lst=[]
for i in range(0,6):
    for j in range(0,6):
        if i==j: 
            continue
        if list[i]==list2[j]:
            lst.append(list[i])
        
print(lst)
