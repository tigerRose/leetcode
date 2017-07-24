#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from add_two_numbers import ListNode, addTwoNumbers, print_list
from add_two_numbers import addTwoNumbers2

class AddTwoNumTestCast(unittest.TestCase):

    def create_list(self, l):
        # l = [1, 4, 3, 2, 3]
        curr = ListNode(l[0])
        root = curr
        for i in xrange(1, len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next
        # print_list(root)
        return root

    def test_sameLengthNoGroth(self):
        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([5, 6, 4])
        rl = addTwoNumbers(l1, l2)
        assert rl.val == 7
        assert rl.next.val == 0
        assert rl.next.next.val == 8

        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([5, 6, 4])
        rl = addTwoNumbers2(l1, l2)
        assert rl.val == 7
        assert rl.next.val == 0
        assert rl.next.next.val == 8

    # @unittest.skip('skip')
    def test_sameLengthWithGroth(self):
        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([5, 6, 8])
        rl = addTwoNumbers(l1, l2)
        assert rl.val == 7
        assert rl.next.val == 0
        assert rl.next.next.val == 2
        assert rl.next.next.next.val == 1

        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([5, 6, 8])
        rl = addTwoNumbers2(l1, l2)
        assert rl.val == 7
        assert rl.next.val == 0
        assert rl.next.next.val == 2
        assert rl.next.next.next.val == 1

    def test_diffLength(self):
        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([0])
        rl = addTwoNumbers(l1, l2)
        assert rl.val == 2
        assert rl.next.val == 4
        assert rl.next.next.val == 3

        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([0])
        rl = addTwoNumbers2(l1, l2)
        assert rl.val == 2
        assert rl.next.val == 4
        assert rl.next.next.val == 3

    def test_sameLengthWithGroth2(self):
        l1 = self.create_list([1])
        l2 = self.create_list([9, 9])
        rl = addTwoNumbers(l1, l2)
        assert rl.val == 0
        assert rl.next.val == 0
        assert rl.next.next.val == 1

        l1 = self.create_list([1])
        l2 = self.create_list([9, 9])
        rl = addTwoNumbers2(l1, l2)
        assert rl.val == 0
        assert rl.next.val == 0
        assert rl.next.next.val == 1

if __name__ == "__main__":
    unittest.main()
