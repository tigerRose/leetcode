#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from lengthOfLongestSubstring import Solution

class LongestSubstringTestCase(unittest.TestCase):

    def setUp(self):
        self.ss = ['abcabcbb', 'bbbbb', 'pwwkew', 'pwwken']

    def test_algorithm_1(self):
        solution = Solution()
        assert solution.lengthOfLongestSubstring(self.ss[0]) == 3
        assert solution.lengthOfLongestSubstring(self.ss[1]) == 1
        assert solution.lengthOfLongestSubstring(self.ss[2]) == 3
        assert solution.lengthOfLongestSubstring(self.ss[3]) == 4

if __name__ == '__main__':
    unittest.main()
