animals = [{'type':'penguin', 'name':'Stephanie','age':8}, {'type':'elephant', 'name':'Devon', 'age':3}, {'type':'puma','name':'Moe','age':5}]
def func1(animals):
    list1 = sorted(animals, key = lambda i: i['age'])
    print(list1)
func1(animals)
