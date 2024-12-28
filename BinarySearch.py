# This one is from the book

daslist = [11, 22, 33, 44, 55, 66, 77, 88 ,99, 110]
upperbound = len(daslist) - 1
lowerbound = 0
found = False

item = int(input("please input num to be found: "))

while (not found) and (upperbound >= lowerbound):
    index = int((upperbound + lowerbound) / 2)
    if(item == daslist[index]):
        found = True
    elif (item > daslist[index]):
        lowerbond = index + 1
    else:
        upperbound = index - 1

if(found):
    print("Item Found")
else:
    print("Item not found")
