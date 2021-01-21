list1 = [1,3,6,9,15,5,27,30,45,90,65,63]
def func(list1):
    new_list = []
    for i in range(0,len(list1)):
        if(isinstance(list1[i],str) == False):
            if(list1[i] % 3 == 0 and list1[i] % 5 == 0):
                list1[i] = "fizzbuzz"
            elif(list1[i] % 3 == 0):
                list1[i] = "fizz"
            elif(list1[i] % 5 == 0):
                list1[i] = "buzz"

    print(list1)
func(list1)
