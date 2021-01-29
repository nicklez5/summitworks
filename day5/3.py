class Error(Exception):
    pass

class NonIntResultException(Error):
    pass

while(True):
    try:
        top_num = int(input("Enter a numerator: "))
        bot_num = int(input("Enter a denominator: "))
        result = top_num / bot_num
        if(result.is_integer()):
            print("Result: ", result)
        else:
            raise NonIntResultException
        break
    except NonIntResultException:
        print("Result is not a integer number")
        
