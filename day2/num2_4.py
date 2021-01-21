list1 = [2,3,4,5,6,7,8]
list2 = [4,9,16,25,36,49,64]
def func1(list1,list2):
    tmp_list = []
    for i in range(0,len(list1)):
        pair = (list1[i],list2[i])
        tmp_list.append(pair)
    tuple_life = tuple(tmp_list)
    print(tuple_life)

func1(list1,list2)


