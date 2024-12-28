
List = [9, 6, 2, 8, 5, 4, 1, 7, 3, 0]
maxvalue = len(List)

def bubblesort():
    for i in range(maxvalue):
        swapped = False

        for j in range(0, maxvalue-i-1):

            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                swapped = True
        if (swapped == False):
            break

bubblesort()

for i in range(0,10):
    print(List[i])
