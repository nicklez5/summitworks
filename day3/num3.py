import random
class obj_gen:
    def __init__(self,n,low,high):
        self.n = n
        self.low = low
        self.high = high
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.i < self.n):
            i = random.randint(self.low,self.high)
            self.i += 1
            return i
        else:
            raise StopIteration()
while(True):
    user_input = eval(input("Please enter n random numbers: "))
    user_input_low = eval(input("Please enter low number: "))
    user_input_high = eval(input("Please enter high number: "))
    if(user_input == 0):
        break
    else:
        xyz = obj_gen(user_input,user_input_low,user_input_high)
        for i in xyz:
            print(i)


