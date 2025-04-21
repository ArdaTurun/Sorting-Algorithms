import random

listThatSorting = [random.randint(1, 1000) for _ in range(10)]

def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while list[j] < list[j-1] and j > 0:
            list[j-1], list[j] = list[j], list[j-1]
            j -= 1
    
    return(list)

print(insertionSort(listThatSorting))
