

import unittest

class Solution(object):

    def zigZagConvert(self, s, numRows):
        if len(s) <= 1 or numRows <= 1 or numRows >= len(s):
            return s

        cols = int(len(s) / (numRows-1))

        new_str = ''
        index = -1
        for row in xrange(numRows):
            index += 1
            for col in xrange(0, cols+2, 2):
                if row == 0 or row == numRows-1:
                    idx = col*(numRows-1)+index
                    if idx >= 0 and idx < len(s):
                        new_str += s[idx]
                else:
                    for i in [-index, index]:
                        idx = col*(numRows-1)+i
                        if idx >= 0 and idx < len(s):
                            new_str += s[idx]

        # print new_str
        return new_str

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

class zigZagConvertTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_zigZagConvert1(self):
        s = 'PAYPALISHIRING'
        numRows = 3
        assert self.s.zigZagConvert(s, numRows) == 'PAHNAPLSIIGYIR'
        assert self.s.convert(s, numRows) == 'PAHNAPLSIIGYIR'

    def test_zigZagConvert3(self):
        s = 'AB'
        numRows = 1
        assert self.s.zigZagConvert(s, numRows) == 'AB'
        assert self.s.convert(s, numRows) == 'AB'

    def test_zigZagConvert4(self):
        s = 'ABCD'
        numRows = 3
        assert self.s.zigZagConvert(s, numRows) == 'ABDC'
        assert self.s.convert(s, numRows) == 'ABDC'

    @unittest.skip("not use")
    def test_zigZagConvert2(self):
        assert self.s.zigZagConvert() == 0

if __name__ == '__main__':
    unittest.main()

