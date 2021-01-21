while(True):
    answer = input("Enter a hyphen-separated sequence of words\n")
    items = [n for n in answer.split('-')]
    items.sort()
    print('-'.join(items))
    break

