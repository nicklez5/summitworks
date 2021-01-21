list_stack = []
while(True):
    value_type = input("Enter 1 to push | 2 to pop | 3 to stop\n")
    if(value_type == "1"):
        value = input("Enter value to push\n")
        num_value = int(value)
        list_stack.insert(0,num_value)
    elif(value_type == "2"):
        list_stack.pop(0)
    elif(value_type == "3"):
        for i in list_stack:
            print(i)
        break
    else:
        break
