

import unittest

class Solution(object):

    def integerToRoman(self, num):
        """
        roman_num_table = {1:'I', 2:'II', 3:'III', 5:'V', 10:'X', 50:'L',\
                100:'C', 500:'D', 1000:'M'}

        if num in roman_num_table: return roman_num_table[num]

        sorted_keys = sorted(roman_num_table.keys())

        para_table = {}
        for v in reversed(sorted_keys):
            r = num / v
            if r != 0:
                para_table[v] = r
            num = num % v
                
        return ''.join([roman_num_table[v]*para_table[v] for v in reversed(sorted(para_table))])
        """

        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];

class integerToRomanTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_integerToRoman1(self):
        assert self.s.integerToRoman(1) == 'I'

    def test_integerToRoman2(self):
        assert self.s.integerToRoman(97) == 'XCVII'

if __name__ == '__main__':
    unittest.main()

