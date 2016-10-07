def ReverseList(list1):
    list2 = []

    # Add all the elements of list1 to list2 starting from the end of list 1
    for i in range(len(list1) - 1, -1, -1):
        list2.append(list1[i])

    # Return the new list
    return list2


print(ReverseList([1, 2, 3, 4]))
print(ReverseList(['hi', 1, 'seven', 3]))
print(ReverseList([5]))
print(ReverseList([ ]))
