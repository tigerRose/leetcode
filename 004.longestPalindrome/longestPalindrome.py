

import unittest

class Solution(object):

    def longestPalindrome(self):

        return -1

class longestPalindromeTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_longestPalindrome1(self):
        assert self.s.longestPalindrome() == 0

    def test_longestPalindrome2(self):
        assert self.s.longestPalindrome() == 0

if __name__ == '__main__':
    unittest.main()

