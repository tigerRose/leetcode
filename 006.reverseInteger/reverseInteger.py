

import unittest

class Solution(object):

    def reverseInteger(self, i):
        raw_str = str(i)
        if len(raw_str) <= 1:
            return i

        new_str = ''
        if raw_str[0] == '-' or raw_str[0] == '+':
            new_str += raw_str[0]
            raw_str = raw_str[1:]
        else:
            new_str += '+'
        for pos in xrange(len(raw_str)-1,-1,-1):
            if len(new_str) == 1 and int(raw_str[pos]) == 0:
                continue
            new_str += raw_str[pos]

        # print new_str
        if int(new_str) >= -2**31 and int(new_str) <= 2**31:
            return int(new_str)
        else:
            return 0

    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)

class reverseIntegerTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_reverseInteger1(self):
        assert self.s.reverseInteger(0) == 0
        assert self.s.reverseInteger(100) == 1
        assert self.s.reverseInteger(101) == 101
        assert self.s.reverseInteger(-101) == -101

        assert self.s.reverse(0) == 0
        assert self.s.reverse(100) == 1
        assert self.s.reverse(101) == 101
        assert self.s.reverse(-101) == -101

    def test_reverseInteger2(self):
        assert self.s.reverseInteger(1000000003) == 0
        assert self.s.reverse(1000000003) == 0

if __name__ == '__main__':
    unittest.main()

