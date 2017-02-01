def edit_distance(str1, str2):
    if len(str1) == 0:
        distance = 0
    else:
        distance = edit_distance(str1[1:], str2[1:])
        if str1[0] != str2[0]:
            distance += 1
    return d


def subsequence(str1, str2):
    if len(str1) != 0 and len(str2) == 0:
        return False
    if len(str1) == 0 or str2 == str1:
        return True
    else:
        if str1[-1] == str2[-1]:
            return subsequence(str1[:-1], str2[:-1])
        else:
            return subsequence(str1, str2[:-1])


def perms(s, node=0, goal=None, set_of_perms=set()):
    if goal is None:
        goal = len(s) - 1
    if node == goal:
        set_of_perms.add(s)
    else:
        counter = node
        while counter <= goal:
            perm1 = swap(s, node, counter)
            set_of_perms.add(perm1)
            perm(perm1, node + 1, goal, set_of_perms)
            perm2 = swap(perm1, node, counter)
            counter += 1
    return set_of_perms


def swap(s, index1, index2):
    string_list = list(s)
    string_list[index1], string_list[
        index2] = string_list[index2], string_list[index1]
    new_string = ''.join(string_list)
    return new_string
