list1 = [3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]
def third_list(first, second):
    list3 = []
    for i in range(0,len(first)):
        if(i % 2 != 0):
            list3.append(first[i])
    for j in range(0,len(second)):
        if(j % 2 == 0):
            list3.append(second[j])
    for k in list3:
        print(k)

third_list(list1,list2)
