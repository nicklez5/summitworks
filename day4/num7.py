import re
str1 = "coffee.,is,an,essential,to, programming"
while(True):
    user_input = input("Please enter a delimited char string: ")
    xyz = re.split(r'\W+',user_input)
    for i in xyz:
        print(i)
    


