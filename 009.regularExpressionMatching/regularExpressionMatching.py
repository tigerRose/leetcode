

import unittest

class Solution(object):

    def isMatch(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # example: 'aab' 'c*a*b*' ignore the pattern of this part 
            # or
            # example: 'aaa' 'a*' deleting one character in text
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def bottom_up_is_match(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]



class regularExpressionMatchingTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_regularExpressionMatching1(self):
        assert self.s.isMatch("aa", "a") == False
        assert self.s.isMatch("aa", "aa") == True
        assert self.s.isMatch("aa", "a*") == True
        assert self.s.isMatch("aa", ".*") == True
        assert self.s.isMatch("aab", "c*a*b*") == True

    def test_regularExpressionMatching2(self):
        assert self.s.bottom_up_is_match("aa", "a") == False
        assert self.s.bottom_up_is_match("aa", "aa") == True
        assert self.s.bottom_up_is_match("aa", "a*") == True
        assert self.s.bottom_up_is_match("aa", ".*") == True
        assert self.s.bottom_up_is_match("aab", "c*a*b*") == True

if __name__ == '__main__':
    unittest.main()

