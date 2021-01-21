cowboy = {'age': 32 , 'horse' : 'mustang' , 'hat_size' : 'large'}
def func(random_dict):
    if 'name' not in random_dict:
        random_dict['name'] = 'The Man with No Name'
        return random_dict['name']
    else:
        return random_dict['name']
    
print(func(cowboy))

