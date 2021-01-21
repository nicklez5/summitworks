neg_list = []
zero_list = []
pos_list = []

while True:
    value = input("Enter any number\n")
    if((value != "\n") and len(value) != 0):
        value2 = int(value)
        if(value2 == 0):
            zero_list.append(0)
        elif(value2 < 0):
            neg_list.append(value2)
        else:
            pos_list.append(value2)
    else:
        for i in neg_list:
            print(i)
        for j in zero_list:
            print(j)
        for k in pos_list:
            print(k)
        break


