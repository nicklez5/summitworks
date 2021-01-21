values = []
while True:
    number = eval(input("Enter the number\n"))
    if number != 0:
        values.append(number)
    else:
        print("\n")
        values.sort()
        for i in values:
            print(i)
        break

