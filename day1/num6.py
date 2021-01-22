list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]

for i in range(0,len(list1)):
    power = list1[i]
    for j in range(1,list2[i]):
        power = power*list1[i]
    print(list1[i], " " , list2[i] , " " , power)
    
