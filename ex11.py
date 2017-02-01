from container import *


def banana_game(s1, s2, c):

    if s1 == s2:
        res = True

    elif len(s2) == 0:
        res = s1 == s2

    elif (not c.is_empty()) and (c.peek() == s2[0]):
        c.get()
        res = banana_game(s1, s2[1:], c)

    elif len(s1) > 0 and s1[0] == s2[0]:
        res = banana_game(s1[1:], s2[1:], c)

    elif len(s1) > 0 and s1[0] != s2[0]:
        try:
            c.put(s1[0])
            res = banana_game(s1[1:], s2, c)

        except ContainerFullException:
            res = False

    else:
        res = False

    return res
