def rsum(listA, total=0):
    leng = len(listA)
    if leng == 0:
        return total
    else:
        if (isinstance(listA[0], list)):
            total += rsum(listA[0])
            total = rsum(listA[1:], total)
        else:
            total = listA[0] + rsum(listA[1:], total)
    return total


def rmax(listB, damax=0):
    listA = listB[:]
    leng = len(listA)
    result = 0
    if (listA == []):
        result = -100000000000000000000000000
    elif ((leng == 1) and not (isinstance(listA[0], list))):
        result = listA[0]
    else:
        num1 = listA[0]
        num2 = listA[1]

        if (isinstance(num1, list)):
            listA[0] = rmax(num1)

        if (isinstance(num2, list)):
            listA[1] = rmax(num2)

        if listA[0] <= listA[1]:
            result = rmax(listA[1:])
        else:
            result = rmax([listA[0]] + listA[2:])

    return result


def second_smallest(listA):
    final = second_smallest_helper(listA)
    return final[0]


def second_smallest_helper(listA):
    if ((((len(listA) == 2) and isinstance(listA[0], int)) and
         isinstance(listA[1], int))):
        if listA[0] > listA[1]:
            result = (listA[0], listA[1])

        else:
            # (2nd smallest, smallest)
            result = (listA[1], listA[0])

    elif ((len(listA) == 1) and isinstance(listA[0], int)):
        result = (float("inf"), listA[0])

    elif ((len(listA) == 1) and isinstance(listA[0], list)):
        result = (float("inf"), float("inf"))

    elif len(listA) == 0:
        result = (float("inf"), float("inf"))

    elif (((len(listA) == 2) and isinstance(listA[0], int)) and
          isinstance(listA[1], list)):
        elem = second_smallest_helper(listA[1])
        if (listA[0] > elem[1]) and (listA[0] < elem[0]):
            result = (listA[0], elem[1])

        elif (listA[0] <= elem[1]):
            result = (elem[1], listA[0])

        else:
            # (2nd smallest, smallest)
            result = elem

    elif (((len(listA) == 2) and isinstance(listA[0], list)) and
          isinstance(listA[1], int)):
        elem = second_smallest_helper(listA[0])
        if (listA[1] > elem[1]) and (listA[1] < elem[0]):
            result = (listA[1], elem[1])

        elif (listA[1] <= elem[1]):
            result = (elem[1], listA[1])

        else:
            # (2nd smallest, smallest)
            result = elem

    elif (((len(listA) == 2) and isinstance(listA[0], list)) and
          isinstance(listA[1], list)):
        first_elem = second_smallest_helper(listA[0])
        last_elem = second_smallest_helper(listA[1])

        if (first_elem[0] <= last_elem[1]):
            result = first_elem

        elif (last_elem[0] <= first_elem[1]):
            result = last_elem

        elif ((first_elem[1] <= last_elem[0]) and
              (first_elem[1] >= last_elem[1])):
            result = (first_elem[1], last_elem[1])

        else:
            # (2nd smallest, smallest)
            result = (last_elem[1], first_elem[1])

    else:
        rest_of_list = second_smallest_helper(listA[1:])

        if isinstance(listA[0], int):
            if ((rest_of_list[0] > listA[0]
                 ) and (listA[0] > rest_of_list[1])):
                result = (listA[0], rest_of_list[1])
            elif (listA[0] <= rest_of_list[1]):
                result = (rest_of_list[1], listA[0])
            else:
                result = rest_of_list

        else:
            first_ele = second_smallest_helper(listA[0])

            if (first_ele[0] <= rest_of_list[1]):
                result = first_ele

            elif (rest_of_list[0] <= first_ele[1]):
                result = rest_of_list

            elif ((first_ele[1] <= rest_of_list[0]) and
                  (first_ele[1] >= rest_of_list[1])):
                result = (first_ele[1], rest_of_list[1])

            else:
                # (2nd smallest, smallest)
                result = (rest_of_list[1], first_ele[1])

    return result


def sum_max_min(L):
    max_min = find_max_min(L)
    return max_min[0] + max_min[1]


def find_max_min(L):
    if len(L) == 0:
        mx, mn = float("-inf"), float("inf")
    elif len(L) == 1:
        if isinstance(L[0], list):
            mx, mn = find_max_min(L[0])
        else:
            mx, mn = L[0], L[0]
    elif len(L) == 2:
        if isinstance(L[0], list) or isinstance(L[1], list):
            if isinstance(L[0], list) and isinstance(L[1], list):
                first = find_max_min(L[0])
                second = find_max_min(L[1])
                if first[0] >= second[0] and first[1] <= second[1]:
                    mx, mn = first
                elif second[0] >= first[0] and second[1] <= first[1]:
                    mx, mn = second
                elif first[1] <= second[0] and first[1] <= second[1]:
                    mx, mn = second[0], first[1]
                else:
                    mx, mn = first[0], second[1]
            elif isinstance(L[0], list):
                first = find_max_min(L[0])
                if L[1] <= first[0] and L[1] >= first[1]:
                    mx, mn = first
                elif L[1] > first[0]:
                    mx, mn = L[1], first[1]
                else:
                    mx, mn = first[0], L[1]
            else:
                second = find_max_min(L[1])
                if L[0] <= second[0] and L[0] >= second[1]:
                    mx, mn = second
                elif L[0] > second[0]:
                    mx, mn = L[0], second[1]
                else:
                    mx, mn = second[0], L[0]
        else:
            if L[0] > L[1]:
                mx, mn = L[0], L[1]
            else:
                mx, mn = L[1], L[0]
    else:
        mx, mn = find_max_min(L[1:])
        if isinstance(L[0], list):
            first = find_max_min(L[0])
            if first[0] >= mx and first[1] <= mn:
                mx, mn = first
            elif first[0] > mx:
                mx, mn = first[0], mn
            elif first[1] < mn:
                mx, mn = mx, first[1]
        else:
            if L[0] > mx:
                mx = L[0]
            elif L[0] < mn:
                mn = L[0]
    return mx, mn
