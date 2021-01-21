roll_number = [47,64,69,37,76,83,95,97]
new_list = []
sample_dict = {'Jhon': 47 , 'Emma':69 , 'Kelly':76, 'Jason':97}
def func2(_list, _dict):
    for i in _list:
        if(i in sample_dict.values()):
            new_list.append(i)
    
    print(new_list)

func2(roll_number,sample_dict)
