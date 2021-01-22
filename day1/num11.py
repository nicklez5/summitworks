list_xyz = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
myMap = {}
myMap_index = 2
result_list = []
i = 0
k = 0
while(i < 26):
    tmp_list = []
    if(i +3 > 26):
        k = 26
    else:
        if(k >= 15 and k < 19):
            k = i + 4
        elif(k >= 22 and k < 26):
            k = i + 4
        else:
            k = i + 3
    for j in range(i,k):  
        tmp_list.append(list_xyz[j])
    set_list = frozenset(tmp_list)
    myMap_index_str = str(myMap_index)
    myMap[set_list] = myMap_index_str
    myMap_index += 1
    
    i = k
   

def num_there(s):
    return any(i.isdigit() for i in s)
def func(myMap):
    while(True):
        user_input = input("Please enter a string:  ")
        line_split = user_input.split("-")
        for i in line_split:
            if(num_there(i) == False):
                for j in i:
                    xyz = [j.lower()]
                    xyz_set = frozenset(xyz)
                    for key in myMap:
                        if(xyz_set.issubset(key)):
                            result_list.append(myMap[key])
                            break 
            else:
                
                result_list.append(i)
                result_list.append("-")
        result_me = ""
        for x in result_list:
            result_me = result_me + x
        print(result_me)
        
func(myMap)         
