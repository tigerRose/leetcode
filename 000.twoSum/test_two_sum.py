#!/usr/bin/env python
# -*- coding: utf-8 -*-

from two_sum import twoSum1, twoSum2

import unittest

class TwoSumTestCase(unittest.TestCase):

    def setUp(self):
        self.nums = [2, 7, 11, 15]
        self.target = 9
        self.results = [[0,1], [1,0]]

    def test_two_sum1(self):
        assert twoSum1(self.nums, self.target) in self.results

    def test_two_sum2(self):
        assert twoSum2(self.nums, self.target) in self.results

if __name__ == "__main__":
    unittest.main()

