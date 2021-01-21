orig_list = [11,45,8,11,23,45,23,45,89]
new_dict = {}
for i in orig_list:
    if(i in new_dict):
        new_dict[i] += 1
    else:
        new_dict[i] = 1

print(new_dict)
