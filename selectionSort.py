import random

listThatSorting = [random.randint(1, 1000) for _ in range(10)]

def selectionSort(list):
    for i in range(len(list)-1):
        minNumber = i

        for j in range (i+1, len(list)):
            if list[j] < list[minNumber]:
                minNumber = j

        if minNumber != i:
            list[minNumber], list[i] = list[i], list[minNumber]

    return list

print(selectionSort(listThatSorting))
