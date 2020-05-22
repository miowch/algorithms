import unittest

"""
Suppose you’re digging through your grandma’s attic and come across a mysterious locked suitcase.
Grandma tells you that the key for the suitcase is probably in this other box.
This box contains more boxes, with more boxes inside those boxes. The key is in a box somewhere.

What’s your algorithm to search for the key?
"""


class Item:
    pass


class Key(Item):
    pass


class Box(Item):
    def __init__(self):
        Item.__init__(self)
        self.content = []

    def make_pile_of_boxes(self):
        pile = Pile()

        for item in self.content:
            pile.put(item)

        return pile

    def put(self, box):
        self.content.append(box)
        return self

    def put_boxes(self, n):
        for i in range(0, n):
            inner_box = Box()
            self.content.append(inner_box)

        return self

    def put_key(self):
        key = Key()
        self.content.append(key)
        return self

    def __len__(self):
        return len(self.content)


class Pile:
    def __init__(self):
        self.pile = []

    def put(self, item):
        self.pile.append(item)

    def grab_item(self):
        item = self.pile.pop()
        return item

    def __len__(self):
        return len(self.pile)


# 1st approach with while loop
def find_the_key_while_loop(box):
    pile_of_boxes = box.make_pile_of_boxes()

    while len(pile_of_boxes) > 0:
        box = pile_of_boxes.grab_item()

        for item in box.content:
            if isinstance(item, Box):
                pile_of_boxes.put(item)
            elif isinstance(item, Key):
                return "You're done!"

    return "There's no key in the box."


# 2nd approach with while loop
def find_the_key_recursion(box):

    def is_key(item):
        if isinstance(item, Key):  # base case
            return True

        for i in item.content:  # recursive case
            if is_key(i):
                return True

        return False

    if is_key(box):
        return "You're done!"
    else:
        return "There's no key in the box."


class TestWhileLoopApproach(unittest.TestCase):

    def test_box_with_key(self):
        box_with_key = Box().put_key()
        main_box = Box()

        # put a box with 2 nested boxes, where one of them also contains a box and the box with the key
        main_box.put(Box().put_boxes(1).put(Box().put_boxes(1).put(box_with_key)))

        # then put a box with 3 nested boxes, where one of them contains 3 more boxes
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(3)))

        # finally put a box with 3 nested boxes, where one of them contains 1 more box
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(1)))

        self.assertEqual("You\'re done!", find_the_key_while_loop(main_box))

    def test_box_without_key(self):
        main_box = Box()

        # put a box with 2 nested boxes, where one of them also contains 2 more boxes
        main_box.put(Box().put_boxes(1).put(Box().put_boxes(2)))

        # then put a box with 3 nested boxes, where one of them contains 3 more boxes
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(3)))

        # finally put a box with 3 nested boxes, where one of them contains 1 more box
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(1)))

        self.assertEqual("There\'s no key in the box.", find_the_key_while_loop(main_box))


class TestRecursionApproach(unittest.TestCase):

    def test_box_with_key(self):
        box_with_key = Box().put_key()
        main_box = Box()

        # put a box with 2 nested boxes, where one of them also contains a box and the box with the key
        main_box.put(Box().put_boxes(1).put(Box().put_boxes(1).put(box_with_key)))

        # then put a box with 3 nested boxes, where one of them contains 3 more boxes
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(3)))

        # finally put a box with 3 nested boxes, where one of them contains 1 more box
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(1)))

        self.assertEqual("You\'re done!", find_the_key_recursion(main_box))

    def test_box_without_key(self):
        main_box = Box()

        # put a box with 2 nested boxes, where one of them also contains 2 more boxes
        main_box.put(Box().put_boxes(1).put(Box().put_boxes(2)))

        # then put a box with 3 nested boxes, where one of them contains 3 more boxes
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(3)))

        # finally put a box with 3 nested boxes, where one of them contains 1 more box
        main_box.put(Box().put_boxes(2).put(Box().put_boxes(1)))

        self.assertEqual("There's no key in the box.", find_the_key_recursion(main_box))


if __name__ == '__main__':
    unittest.main()
