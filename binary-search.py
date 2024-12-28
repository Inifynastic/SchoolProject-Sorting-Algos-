# This is broken so use the other one.(I need to fix it)
List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
maxvalue = len(List)
minvalue = 0
findvalue = 5

def BinarySearch(number):
    global minvalue
    global maxvalue
    while(minvalue <= maxvalue):
        midvalue = (List[0] + List[9])//2
        if(number == List[midvalue]):
            return True
        elif(number > List[midvalue]):
            minvalue = midvalue + 1
        else:
            maxvalue = midvalue - 1
    return False

Bool = BinarySearch(findvalue)
if(Bool):
    print("Value was Found!")
else:
    print("Value was not Found!")
