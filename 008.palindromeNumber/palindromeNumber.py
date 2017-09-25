

import unittest

class Solution(object):

    def palindromeNumber(self, x):
        if x < 0:
            #x *= -1
            return False

        temp_lst = []
        rtx = True
        while x != 0:
            temp_lst.append(x % 10)
            x = x/10

        if len(temp_lst) <= 1:
            rtx = True
        else:
            for i in xrange(len(temp_lst)):
                j = len(temp_lst) - 1 -i
                if i > j:
                    break
                if temp_lst[i] != temp_lst[j]:
                    rtx = False
                    break
        print rtx, temp_lst
        return rtx

class palindromeNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_palindromeNumber1(self):
        x = 1221
        assert self.s.palindromeNumber(x) == True
        x = -1221
        assert self.s.palindromeNumber(x) == False
        x = 121221
        assert self.s.palindromeNumber(x) == False
        x = 0
        assert self.s.palindromeNumber(x) == True

if __name__ == '__main__':
    unittest.main()

