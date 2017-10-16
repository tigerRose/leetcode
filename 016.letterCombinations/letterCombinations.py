

import unittest

class Solution(object):

    def letterCombinations(self, digits):
        maps = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            if digits[0] in maps:
                return [x for x in maps[digits[0]]]
            else:
                return []

        if digits[0] in maps:
            lst = []
            for s in maps[digits[0]]:
                for t in self.letterCombinations(digits[1:]):
                    lst.append(s + t)
            return lst

    def letterCombinations2(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])

    def letterCombinations3(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        arrays = [x for x in kvmaps[digits[0]]]
        for i in xrange(1, len(digits)):
            temp_arrays = []
            for j in kvmaps[digits[i]]:
                for k in arrays:
                    temp_arrays.append(k+j)
            arrays = temp_arrays

        return arrays



class letterCombinationsTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_letterCombinations1(self):
        print self.s.letterCombinations('23') 
        print self.s.letterCombinations2('23') 
        print self.s.letterCombinations3('23') 


if __name__ == '__main__':
    unittest.main()

