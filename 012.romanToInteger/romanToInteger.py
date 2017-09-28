

import unittest

class Solution(object):

    def romanToInteger(self, s):
        M = ["M", "MM", "MMM"];
        C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        d = {}
        d.update({I[i]:i+1 for i in xrange(len(I))})
        d.update({X[i]:(i+1)*10 for i in xrange(len(X))})
        d.update({C[i]:(i+1)*100 for i in xrange(len(C))})
        d.update({M[i]:(i+1)*1000 for i in xrange(len(M))})


        r = 0
        while len(s)>0:
            for i in xrange(len(s), 0, -1):
                t = s[:i] 
                if t in d:
                    r += d[t]
                    break
            s = s[i:]
        print r
        return r

class romanToIntegerTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_romanToInteger1(self):
        assert self.s.romanToInteger('VI') == 6

    def test_romanToInteger2(self):
        assert self.s.romanToInteger('XCVII') == 97
        assert self.s.romanToInteger('MCMXCVI') == 1996

if __name__ == '__main__':
    unittest.main()

