def SortList(list1):

    # for all the elements check if the value is less than the others switching them if they are
    for i in range(len(list1)):
        for j in range(len(list1)):
            if (list1[i] < list1[j]):
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp

    # return sorted list
    return list1

print(SortList([6, 4, 2, -1]))
print(SortList([6, 3, 9, 2, 3]))
print(SortList([5]))
print(SortList([ ]))
