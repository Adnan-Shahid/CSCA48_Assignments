def greeting(name):
    '''(string) -> string
    Returns a greeting message with the user's input name
    
    >>> greeting('banana')
    'Hello banana, how are you today?'
    '''

    greeting = 'Hello ' + name + ' how are you today?'
    return greeting


def mutate_list(listA):
    '''(list) -> NoneType
    Mutates a list with the given rules
    Any integer is multiplied by 2
    Booleans are reversed
    Strings have the first and last letter of the string removed
    The first element of the list will be changed to 'Hello'

    REQ: list contains at least one item
    REQ: strings must have a length of at least 2
    
    >>> x = [1,"Banana", True, 6]
    >>> mutate_list(x)
    >>> print(x)
    ['Hello', 'anan', False, 12]

     >>> x = [True,"QW", False, 3.14]
     >>> mutate_list(x)
     >>> print(x)
     ['Hello', '', True, 3.14]
    '''
    for i in range(len(listA)):
        if type(listA[i]) == int:
            listA[i] = listA[i]*2
        elif type(listA[i]) == bool:
            listA[i] = not listA[i]
        elif type(listA[i]) == str:
            listA[i] = listA[i][1:-1]
    listA[0] = 'Hello'


def merge_dicts(d1, d2):
    '''
    (dict, dict) -> dict

    REQ: dictionaries aren't empty

    Combines two dictionaries together, if the same key is in both,
    adds the values from the second dict to the first

    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}

    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}

    '''
    # list of keys
    d1_keys = []
    d2_keys = []

    # new dictionary
    final_dict = {}

    # keys to be removed
    remove_list = []

    # Creating a list of keys
    for key in d1:
        d1_keys.append(key)

    for key in d2:
        d2_keys.append(key)

    # appending the keys together
    for i in range(len(d1_keys)):
        for j in range(len(d2_keys)):
            # checks if the keys are the same
            if (d1_keys[i] == d2_keys[j]):
                list_d1 = []
                list_d2 = []
                # appends each to a new list
                for k in d1[d1_keys[i]]:
                    list_d1.append(k)
                for k in d2[d2_keys[j]]:
                    list_d2.append(k)

                # adds the list and key to the dictionary
                final_dict[d1_keys[i]] = list_d1 + list_d2
                remove_list.append(d2_keys[j])

    # remove copies
    for i in remove_list:
        d1_keys.remove(i)
        d2_keys.remove(i)

    # placing in the unique keys
    for i in d1_keys:
        final_dict[i] = d1[i]
    for i in d2_keys:
        final_dict[i] = d2[i]

    return final_dict
