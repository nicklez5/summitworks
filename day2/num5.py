list_queue = []
input_type1 = "1"
input_type2 = "2"
input_type3 = "3"

while(True):
    input_type = input("Enter 1 to insert ,  2 to pop , 3 to stop\n")
    if(input_type == input_type1):
        value = input("Enter number to push\n")
        num_value = int(value)
        list_queue.insert(0,num_value)
    elif(input_type == input_type2):
        list_queue.pop(len(list_queue)-1)
    elif(input_type == input_type3):
        for i in list_queue:
            print(i)
        break
    else:
        break


