

import unittest

class Solution(object):

    def longestPalindrome(self, s):
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return 1

        last_str = ''
        max_len = -1
        for idx in xrange(len(s)):
            if last_str != '':
                curr_len = 1
                s1 = s[idx-1::-1]
                s2 = s[idx+1::]
                for i in xrange(min(len(s1), len(s2))):
                    if s1[i] != s2[i]:
                        if max_len < curr_len:
                            max_len = curr_len
                        break
                    curr_len += 2

                if s[idx] == last_str:
                    curr_len = 0
                    s1 = s[idx-1::-1]
                    s2 = s[idx::]
                    for i in xrange(min(len(s1), len(s2))):
                        if s1[i] != s2[i]:
                            if max_len < curr_len:
                                max_len = curr_len
                            break
                        curr_len += 2
                last_str = s[idx]
            else:
                last_str = s[idx]
                
        # print max_len
        return max_len

class longestPalindromeTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_longestPalindrome1(self):
        s = 'babad'
        assert self.s.longestPalindrome(s) == 3

    def test_longestPalindrome2(self):
        s = 'cbbd'
        assert self.s.longestPalindrome(s) == 2

if __name__ == '__main__':
    unittest.main()

