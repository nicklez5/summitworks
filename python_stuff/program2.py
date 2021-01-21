list1 = [1,-2,3,4,5,6,7,8,9,10]
small_value = -1
large_value = 0
for i in list1:
    if(i > large_value):
        large_value = i
    if(small_value == -1):
        small_value = i
    else:
        if(i < small_value):
            small_value = i
    print("Item value:",i)

print("Large value:", large_value)
print("Small value:", small_value)

