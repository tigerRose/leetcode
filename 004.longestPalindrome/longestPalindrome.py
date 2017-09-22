

import unittest

class Solution(object):

    def longestPalindrome(self, s):
        l = len(s)
        if l <= 1:
            return s

        max_str = ''
        cur_str = ''

        for i in xrange(l):
            cur_str = max(compare_str(s,"",1,i), compare_str(s,s[i],0,i))

            if len(cur_str) > len(max_str):
                max_str = cur_str
        return max_str

def compare_str(s, cur_str, pos, i):
    l = len(s)
    for j in xrange(1, l/2+1):
        forward = i-j+pos
        backword = i+j
        if forward < 0 and backword > l-1:
            break

        if forward >= 0 and backword <= l-1 and s[forward] == s[backword]:
            cur_str = s[forward] + cur_str + s[backword]
        elif forward >= 0 and len(cur_str) == 1 and s[forward] == cur_str:
            cur_str += cur_str
            break
        elif backword <= l-1 and len(cur_str) == 1 and s[backword] == cur_str:
            cur_str += cur_str
            break
        else:
            break
    return cur_str

class longestPalindromeTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_longestPalindrome1(self):
        s = 'babad'
        assert self.s.longestPalindrome(s) == "bab"

    def test_longestPalindrome2(self):
        s = 'cbbd'
        assert self.s.longestPalindrome(s) == "bb"

    def test_longestPalindrome3(self):
        s = 'aaaa'
        assert self.s.longestPalindrome(s) == "aaaa"

if __name__ == '__main__':
    unittest.main()

