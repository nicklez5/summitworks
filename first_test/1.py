def find_largest(tmp_set):
    largest = 0
    for i in tmp_set:
        if(i > largest):
            largest = i
    return largest

def find_smallest(tmp_set):
    smallest = 10000
    for i in tmp_set:
        if(i < smallest):
            smallest = i
    return smallest

set_intervals = ([2,4],[3,6],[1,3],[6,8])
list_frozen_sets = []
for i in set_intervals:
    start_index = i[0]
    end_index = i[1]
    xyz = start_index
    list_xyz = []
    while(xyz < end_index+1):
        list_xyz.append(xyz)
        xyz += 1
    temp_frozen_set = frozenset(list_xyz)
    list_frozen_sets.append(temp_frozen_set)
appended_frozen_sets = []
i = 0
total_time = 0
while(i < len(list_frozen_sets)):
    if(len(appended_frozen_sets) == 0):
        first_frozen_set = list_frozen_sets[i]
        second_frozen_set = list_frozen_sets[i+1]
        if(first_frozen_set.intersection(second_frozen_set)):
            keepers_weepers = first_frozen_set.union(second_frozen_set)
            lrg = find_largest(keepers_weepers)
            sml = find_smallest(keepers_weepers)
            print("Large: ", lrg)
            print("Small: ", sml)
            total_time = lrg - sml
            appended_frozen_sets.append(first_frozen_set)
            appended_frozen_sets.append(second_frozen_set)
            i += 2
    else:
        new_frozen_set = list_frozen_sets[i]
        random_set = set()
        for j in appended_frozen_sets:
            random_set = random_set.union(j)
        print(random_set)
        if(new_frozen_set.intersection(random_set)):
            keepers_weepers = new_frozen_set.union(random_set)
            lrg = find_largest(keepers_weepers)
            sml = find_smallest(keepers_weepers)
            total_time = lrg-sml
            appended_frozen_sets.append(new_frozen_set)
            print("Total Time: ", total_time)
            i += 1
    
        
    


