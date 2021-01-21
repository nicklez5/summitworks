xyz_dict = {0:10, 1:20}

def add_key(dict_x, key,value):
    dict_x[key] = value
    for k,v in dict_x.items():
        print(k,v)

add_key(xyz_dict,2,20)
