
import unittest

class Solution(object):

    def findMedianSortedArrays(self, num1, num2):
        i = j = 0
        num3 = []
        while True:
            if i >= len(num1) and j >= len(num2):
                break
            if i >= len(num1):
                num3.append(num2[j])
                j += 1
                continue
            if j >= len(num2):
                num3.append(num1[i])
                i += 1
                continue

            if num1[i] < num2[j]:
                num3.append(num1[i])
                i += 1
            else:
                num3.append(num2[j])
                j += 1
        
        # print num3
        if len(num3) % 2 == 0:
            return (num3[len(num3)/2 - 1] + num3[len(num3)/2]) / 2.0
        else:
            return num3[int(len(num3)/2)]



class MedianSortedArraysTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_a1(self):
        l1 = [1, 3]
        l2 = [2]
        assert self.s.findMedianSortedArrays(l1, l2) == 2

    def test_a2(self):
        l1 = [1, 2]
        l2 = [3, 4]
        assert self.s.findMedianSortedArrays(l1, l2) == 2.5

if __name__ == '__main__':
    unittest.main()
