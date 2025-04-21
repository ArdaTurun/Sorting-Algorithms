import random

listThatSorting = [random.randint(1, 1000) for _ in range(10)]

def sorting(list):
    indexingLenght = len(list) - 1
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(0, indexingLenght):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]

    return list

print(sorting(listThatSorting))