import random

listThatSorting = [random.randint(1, 1000) for _ in range(10)]

def mergeSort(list):
    if len(list) > 1:
        leftList = list[:len(list)//2]
        rightList = list[len(list)//2:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0 # leftList index
        j = 0 # rightList index
        k = 0 # List index

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                list[k] = leftList[i]
                i += 1
            else:
                list[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            list[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            list[k] = rightList[j]
            j += 1
            k += 1

    return list

print(mergeSort(listThatSorting))