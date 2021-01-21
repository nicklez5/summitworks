def takeSecond(elem):
    return elem[1]

random = [(2,2),(3,4),(4,1),(1,3)]
random.sort(key=takeSecond)
print('Sorted list:', random)
