tmp_list = [87,45,41,65,94,41,99,94]
def func1(list1):
    new_list = []
    for i in list1:
        if(i not in new_list):
            new_list.append(i)
    print("Unique items:", new_list)
    random_tuple = tuple(new_list)
    print("tuple:", random_tuple)
    print("Max:", max(random_tuple))
    print("Min:", min(random_tuple))

func1(tmp_list)

