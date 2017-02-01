class Queue():
    def __init__(self):
        self._contents = []
    
    def __str__(self):
        s = ''
        for item in self._contents:
            s = s + str(item) + ','
        return s[:-2]

    def g(self):
        return self._contents
    
    def enqueue(self, item):
        self._contents.append(item)
    
    def dequeue(self):
        return self._contents.pop(0)
    
    def is_empty(self):
        return (len(self._contents) == 0)
    
class EmptyQueueError(Exception):
    pass


def radix_sort(alist):
    main_bin = Queue()
    bin_list = []
    obj = Queue()
    digit = 10
    L = alist[:]
    # make a list of objects where the 0th element is 0th place
    for i in range(10):
        bin_list.append(obj)

    for i in alist:
        main_bin.enqueue(i)
            
    while digit <= 1000:
        digit_sort(digit, bin_list, main_bin)
        print(digit, bin_list, main_bin.g())
        for i in range(10):
            while not bin_list[i].is_empty():
                L[i] = bin_list[i].dequeue()
        digit = digit*10

    return L

def digit_sort(digit, bin_list, main_bin):
    while not main_bin.is_empty():
        val = main_bin.dequeue()
        place = val % digit
        if place == 0:
            bin_list[0].enqueue(place)
        elif place == 1:
            bin_list[1].enqueue(place)
        elif place == 2:
            bin_list[2].enqueue(place)
        elif place == 3:
            bin_list[3].enqueue(place)
        elif place == 4:
            bin_list[4].enqueue(place)
        elif place == 5:
            bin_list[5].enqueue(place)
        elif place == 6:
            bin_list[6].enqueue(place)
        elif place == 7:
            bin_list[7].enqueue(place)
        elif place == 8:
            bin_list[8].enqueue(place)
        elif place == 9:
            bin_list[9].enqueue(place)