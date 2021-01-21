sampleList= [11,45,8,23,14,12,78,45,89]
def split_list(list1):
    for i in range(0,len(list1),3):
        list_split = list1[i:i+3]
        list_split.reverse()
        print(list_split)
        
    

split_list(sampleList)
