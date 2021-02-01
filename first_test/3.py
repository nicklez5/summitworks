cool_beans = ["Black", "Red", "Maroon", "Yellow"]
html_beans = ["#000000", "#FF0000", "#800000", "#FFFF00"]
j = 0
list_dict = []
for i in cool_beans:
    tmp_dict = {}
    tmp_dict["color_name"] = i
    tmp_dict["color_code"] = html_beans[j]
    j += 1
    list_dict.append(tmp_dict)

print(list_dict)

