

import unittest

class Solution(object):

    def myAtoi(self, s):
        if len(s) <= 0:
            return 0

        begin_flag = False
        sign_flag = 1
        return_int = 0
        for i in xrange(len(s)):
            if begin_flag and s[i] >= '0' and s[i] <= '9':
                return_int = return_int * 10 + int(s[i])
            elif begin_flag:
                break

            if not begin_flag:
                if s[i] == '+':
                    begin_flag = True 
                elif s[i] == '-':
                    begin_flag = True
                    sign_flag = -1
                elif s[i] >= '0' and s[i] <= '9':
                    begin_flag = True
                    return_int = return_int * 10 + int(s[i])
                elif s[i] == ' ':
                    continue
                else:
                    break

        return_int *= sign_flag

        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if return_int >= INT_MAX:
            return_int = INT_MAX
        elif return_int <= INT_MIN:
            return_int = INT_MIN

        print return_int
        return return_int



class myAtoiTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_myAtoi1(self):
        raw_str = '123'
        assert self.s.myAtoi(raw_str) == 123
        raw_str = '-123'
        assert self.s.myAtoi(raw_str) == -123
        raw_str = '  -123'
        assert self.s.myAtoi(raw_str) == -123
        raw_str = '  -123abc'
        assert self.s.myAtoi(raw_str) == -123

    def test_myAtoi2(self):
        raw_str = ''
        assert self.s.myAtoi(raw_str) == 0
        raw_str = '  abc'
        assert self.s.myAtoi(raw_str) == 0
        raw_str = '  abc123'
        assert self.s.myAtoi(raw_str) == 0
        raw_str = '12345678910'
        assert self.s.myAtoi(raw_str) == 2**31-1
        raw_str = '-12345678910'
        assert self.s.myAtoi(raw_str) == -2**31

if __name__ == '__main__':
    unittest.main()

