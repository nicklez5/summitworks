import re
f = open("2.txt","r")
for x in f:
    for word in x.split():
        x = re.search("[a-yA-Y]+[z]+[a-yA-Y]+",word)
        if(x != None):
            print(word)
