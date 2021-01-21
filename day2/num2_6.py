temp_dict = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
def get_values(_dict):
    tmp_list = []
    for i in temp_dict.values():
        if(i not in tmp_list):
            tmp_list.append(i)

    print(tmp_list)

get_values(temp_dict)
