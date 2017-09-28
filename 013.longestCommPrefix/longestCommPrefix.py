

import unittest

class Solution(object):

    def longestCommPrefix(self, strs):
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        base_len = len(min(strs))
        max_prefix = ""
        while base_len > 0:
            curr_prefix = strs[0][:base_len]
            same_flag = True
            for s in strs:
                if s[:base_len] != curr_prefix:
                    same_flag = False
                    break
            if same_flag:
                max_prefix = curr_prefix
                break
            base_len -= 1

        print max_prefix
        return max_prefix

class longestCommPrefixTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_longestCommPrefix1(self):
        assert self.s.longestCommPrefix([]) == ""
        assert self.s.longestCommPrefix(["a"]) == "a"

    def test_longestCommPrefix2(self):
        assert self.s.longestCommPrefix(["abc", "abd"]) == "ab"

if __name__ == '__main__':
    unittest.main()

