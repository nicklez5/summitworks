list_xyz = []
gross_pay = []
list_names = ["Connie Cobol", "Mary Apl", "Frank Fortran" , "Jeff Ada", "Anton Pascal"]
id_names = {"Connie Cobol" : 98401 , "Mary Apl" : 526488, "Frank Fortran": 765349, "Jeff Ada" : 34645 , "Anton Pascal" :127615}
wage_names = {"Connie Cobol" : 10.60 , "Mary Apl" : 9.75 , "Frank Fortran" : 10.50 , "Jeff Ada" : 12.25, "Anton Pascal" : 10.00}
while(True):
    i = 0
    while(i < 5):
        user_input = eval(input("Please enter the hours %s worked: " % list_names[i]))
        list_xyz.append(user_input)
        i += 1
    i = 0
    for j in list_names:
        tmp_gross_pay = 0
        wage_price = wage_names[j]
        if(list_xyz[i] > 40):
            tmp_gross_pay = float(40 * wage_price)
            remainder_hours = list_xyz[i] - 40
            tmp_gross_pay += float(remainder_hours * float((wage_price*1.5)))
            gross_pay.append(tmp_gross_pay)
        else:
            tmp_gross_pay += float(list_xyz[i] * wage_price)
            gross_pay.append(tmp_gross_pay)
            remainder_hours = 0
    
        print("Name: %s | Clock Num: %d | Wage: %.2f | Hours: %.2f | OT: %.2f | Gross Pay: %.2f" % (j,id_names[j],wage_price,list_xyz[i],remainder_hours,gross_pay[i]))
        i += 1


    

    
