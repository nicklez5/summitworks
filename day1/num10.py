
tmp_string = "1 2 3 4 5 6 7"
list_xyz = [6,5,4,3,2,1]
reverse_bool = False
string_index = 0
list_index = 0
for i in range(0,13):
    if(reverse_bool == False):
        print(tmp_string)
        if(i == 6):
            reverse_bool = True
            string_index -= 1
        else:
            tmp_string = tmp_string[:string_index] + tmp_string[string_index+1:]
            string_index += 1
    else:
        tmp_string  = tmp_string[:string_index] + tmp_string[string_index+1:]
        tmp_string = tmp_string[:string_index] + str(list_xyz[list_index]) + " " + tmp_string[string_index:]
        list_index += 1
        string_index -= 1
        print(tmp_string)


