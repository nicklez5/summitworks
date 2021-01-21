dict_1 = {"a" : 1, "b" : 2 , "c" : 3 , "d" : 4, "e" : 5}
def get_key_value_dict(dict_2):
    index = 1
    for k,v in dict_2.items():
        print("Key:",k," Value:",v," Index:", index)
        index += 1

get_key_value_dict(dict_1)
