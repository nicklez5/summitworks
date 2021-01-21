postfix_exp = ["4","5","7","2","+","-","*"]
def postfix_expfunc(list_exp):
    values = []
    for i in postfix_exp:
        if(i.isdigit()):
            x = int(i)
            values.append(x)
        else:
            right = values.pop()
            left = values.pop()
            if("+" in i):
                result = left + right
                values.append(result)
            elif("-" in i):
                result = left- right
                values.append(result)
            elif("*" in i):
                result = left * right
                values.append(result)
            elif("/" in i):
                result = left / right
                values.append(result)
            
                
        
    return values[0]

value2 = postfix_expfunc(postfix_exp)
print("Value: ",value2)

