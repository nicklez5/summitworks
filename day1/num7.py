lottery_num = 741
string_lottery = str(lottery_num)
list_lottery = [int(i) for i in string_lottery]

while(True):
    counter = 0
    num = eval(input("Enter a three digit number\n"))
    if(num == lottery_num):
        print("You won $10,000!")
    else:
        string_me = str(num)
        list_xyz = [int(i) for i in string_me]
        for i in range(0,len(list_xyz)):
            if(list_xyz[i] in list_lottery):
                counter += 1
                list_lottery.remove(list_xyz[i])
        if(counter == 3):
            print("You won $3,000!")
        elif(counter != 0):
            print("You won $1,000!")
    list_lottery = [int(i) for i in string_lottery]
                
            

