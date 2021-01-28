import re
list_input = ["example  (.com)","summitworks","github  (.com)", "stackoverflow(.com)"]
for x in list_input:
    m = re.search('[(][a-zA-Z+,.]*[)]',x)
    if(m != None):
        result_index = x.find('(')
        result_end_index = x.find(')')
        y = x[0:result_index] + x[result_end_index+1::]
        print(y)
    else:
        print(x)
