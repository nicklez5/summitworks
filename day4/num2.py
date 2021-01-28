import re
f = open("1.txt","r")
tmp_dict = {}
for x in f:
    result = re.split(r'[:,\s]\s*',x)
    for i in result:
        i = i.replace(',',' ')
        if i in tmp_dict:
            tmp_dict[i] += 1
        else:
            tmp_dict[i] = 1

for key,value in tmp_dict.items():
    print(key,'->', value)

