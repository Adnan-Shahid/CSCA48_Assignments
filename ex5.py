def rsum(listA):
    result = 0
    leng = len(listA)
    if leng == 0:
        result = 0
    else:
        result = result + listA[0] + rsum(listA[1:])
    return result


def rmax(listA):
    leng = len(listA)
    if leng == 1:
        result = listA[0]
    else:
        if listA[0] <= listA[1]:
            result = rmax(listA[1:])
        else:
            result = rmax([listA[0]] + listA[2:])
    return result


def second_smallest(listA):
    # get the lenght of the list
    leng = len(listA)

    # base case
    if leng == 2:
        # return the larger of the two ie the second smallest
        result = max(listA[0], listA[1])
    else:
        # if the 3rd element is smaller than the first or second
        # make a new list in which the largest of the first or second element
        # is removed
        if (listA[2] <= listA[0] or listA[2] <= listA[1]):
            biggest = max(listA[0], listA[1])
            if biggest == listA[0]:
                result = second_smallest(listA[1:])
            else:
                result = second_smallest([listA[0]] + listA[2:])
        # if the 3rd element isn't smaller than the two, just continue
        else:
            result = second_smallest(listA[:2] + listA[3:])
    return result


def sum_max_min(listA):
    if (len(listA) == 2):
        return listA[0] + listA[1]
    else:
        result = aids(listA)
        return result


def aids(listassist):

    result = [min(listassist), max(listassist)]
    return sum_max_min(result)
