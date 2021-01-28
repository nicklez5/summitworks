import re
f = open("3.txt","r")
while(True):
    user_input = input("Please enter a url in a string: ")
    z = re.match("^(http|https?|ftp|smtp)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?",user_input)
    if z:
        print("URL: ",user_input)

