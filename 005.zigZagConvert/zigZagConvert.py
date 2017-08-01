

import unittest

class Solution(object):

    def zigZagConvert(self, s, numRows):
        if numRows >= len(s):
            return s

        new_s = ''
        new_s += s[0::numRows+1]
        new_s += s[1::numRows-1]
        new_s += s[2::numRows+1]

        # print new_s
        return new_s

class zigZagConvertTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_zigZagConvert1(self):
        s = 'PAYPALISHIRING'
        numRows = 3
        assert self.s.zigZagConvert(s, numRows) == 'PAHNAPLSIIGYIR'

    @unittest.skip("not use")
    def test_zigZagConvert2(self):
        assert self.s.zigZagConvert() == 0

if __name__ == '__main__':
    unittest.main()

