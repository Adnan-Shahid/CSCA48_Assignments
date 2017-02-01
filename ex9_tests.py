import unittest
from ex9_code import *


class TestEx9(unittest.TestCase):

    def test_init(self):
        a = Heap([1, 3, 5, 7, 9])
        self.assertEqual(a._heap, [9, 7, 3, 1, 5],
                         "Heap.__init__ fails in adding elements"
                         "in the appropriate order using insert")

    def test_init2(self):
        a = Heap([1, -4, 8, 7, 3])
        self.assertEqual(a._heap, [8, 7, 1, -4, 3],
                         "Heap.__init__ fails in adding elements"
                         "in the appropriate order using insert")

    def test_is_empty_heap_empty(self):
        a = Heap([])
        self.assertEqual(a.is_empty(), True,
                         "Heap.is_empty states that an empty list has items")

    def test_is_empty_heap_not_empty(self):
        a = Heap([13])
        self.assertEqual(a.is_empty(), False,
                         "Heap.is_empty states that a non empty list is empty")

    def test_insert_in_empty(self):
        a = Heap([])
        a.insert(13)
        self.assertEqual(a._heap, [13],
                         "Heap.insert doesn't insert a value")

    def test_insert_smallest_val(self):
        a = Heap([8, 7, 1, -4, 3])
        a.insert(-10)
        self.assertEqual(a._heap, [8, 7, 1, -4, 3, -10],
                         "Heap.insert doesn't properly order the values with "
                         "entering a new smallest value")

    def test_insert_biggest_val(self):
        a = Heap([])
        a._heap = [8, 7, 1, -4, 3]
        a.insert(10)
        self.assertEqual(a._heap, [10, 7, 8, -4, 3, 1],
                         "Heap.insert doesn't properly order the values with "
                         "entering a new biggest value")

    def test_bubble_up_checker(self):
        a = Heap([])
        a._heap = [8, 7, 1, -4, 3]
        a._bubble_up(3)

        self.assertEqual(a._heap, [8, 7, 1, -4, 3],
                         "Heap._bubble_up modified the heap incorrectly"
                         "even though no change was necessary")

    def test_bubble_up_checker_2(self):
        a = Heap([])
        a._heap = [10, 2, 4, 6]
        a._bubble_up(3)

        self.assertEqual(a._heap, [10, 6, 4, 2],
                         "Heap._bubble_up failed to bubble up properly")

    def test_bubble_up_highest(self):
        a = Heap([])
        a._heap = [6, 2, 4, 10]
        a._bubble_up(3)

        self.assertEqual(a._heap, [10, 6, 4, 2],
                         "Heap._bubble_up failed to bubble up the "
                         "biggest element to the top of the heap.")

    def test_remove_top_empty(self):
        a = Heap([])
        self.assertRaises(HeapEmptyException, a.remove_top)

    def test_remove_top_end_of_heap(self):
        a = Heap([13])
        self.assertEqual(a.remove_top(), 13,
                         "Heap.remove_top doesnt return the right element"
                         " with only one element in the heap")
        self.assertEqual(a._heap, [],
                         "Heap.remove_top doesn't remove the element "
                         "from the heap")

    def test_remove_top(self):
        a = Heap([])
        a._heap = [50, 40, 30, 6, 4, 3, 6, 2]
        self.assertEqual(a.remove_top(), 50,
                         "Heap.remove_top doesn't return highest element")
        self.assertEqual(a._heap, [40, 6, 30, 2, 4, 3, 6],
                         "After removal, the heap is not reordered properly")

    def test_violates(self):
        a = Heap([])
        a._heap = [9, 7, 3, 1, 5]

        self.assertEqual(a._violates(0), False,
                         "Heap._violates stated there was a violation"
                         " even if there was no violation")

    def test_violates2_violation(self):
        a = Heap([])
        a._heap = [4, 5, 2, 1, 3]

        self.assertEqual(a._violates(0), True,
                         "Heap._violates stated there was a violation"
                         " even if there was one")

    def test_violates3_no_element(self):
        a = Heap([])
        a._heap = [20, 16, 8, 4, 12]

        self.assertEqual(a._violates(3), False,
                         "Heap._violates stated there was a violation but"
                         "the element had no children - no violation")

    def test_bubble_down(self):
        h = Heap([])
        h._heap = [5, 4, 2, 1, 3]
        h._bubble_down(0)

        self.assertEqual(h._heap, [5, 4, 2, 1, 3],
                         "Heap._bubble_down edited the heap when no change"
                         " was needed")

    def test_bubble_down_2(self):
        h = Heap([])
        h._heap = [6, 20, 4, 2]
        h._bubble_down(0)

        self.assertEqual(h._heap, [20, 6, 4, 2],
                         "Heap._bubble_up didn't bubble down despite"
                         " violations in the heap")

    def test_bubble_down_final(self):
        h = Heap([])
        h._heap = [4, 13, 5, 6]
        h._bubble_down(0)

        self.assertEqual(h._heap, [13, 6, 5, 4],
                         "Heap._bubble_up failed to bubble down the smallest"
                         " element to the bottom of the heap")


if(__name__ == "__main__"):
    unittest.main(exit=False)
