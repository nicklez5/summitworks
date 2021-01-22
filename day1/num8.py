highest_val = 0
list_num = []
count = 0
while(True):
    input_value = input("Enter a list of numbers\n")
    int_value = int(input_value)
    if(int_value != 0):
        list_num.append(int_value)
    else:
        for i in list_num:
            if(i > highest_val):
                highest_val =  i
        for e in list_num:
            if(e == highest_val):
                count += 1
        print("The largest number is", highest_val)
        print("The occurrence count of the largest number is ", count)

