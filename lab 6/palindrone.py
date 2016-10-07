def IsPalindrome(list1):
    list2 = []

    # Add all the elements of list1 to list2 starting from the end of list 1
    for i in range(len(list1) - 1, -1, -1):
        list2.append(list1[i])

    # Return True if the elements are equal otherwise return false
    if (list1 == list2):
        return True
    return False


print(IsPalindrome([-10, -1, -1, -10]))
print(IsPalindrome(['pizza', 14, 'corn', 14, 'pizza']))
print(IsPalindrome(['pizza', 'pie', 'corn', 'pizza']))
print(IsPalindrome([10]))
