def display_me(n1,n2):
    isPrime = True
    for i in range(n1,n2):
        if(i == 1):
            print(i)
            continue
        if(check_prime(i) == True):
            print(i)


def check_prime(num):
    if(num > 1):
        for i in range(2,num):
            if((num % i) == 0):
                return False
    return True
def gen(n1,n2):

    while(True):
        if(n1 > n2):
            return
        if(check_prime(n1) == True):
            yield n1
        n1 += 1
user_input = eval(input("Please enter n1: "))
user_input2 = eval(input("Please enter n2: "))
print("Printing Iterator")
display_me(user_input,user_input2)
print("Printing Generator")
xyz = gen(user_input,user_input2)
for x in xyz:
    print(x)
