with open("read_one.txt") as f1, open("read_two.txt") as f2:
    for x, y in zip(f1,f2):
        print("{0}\t{1}".format(y.strip(),x.strip()))
