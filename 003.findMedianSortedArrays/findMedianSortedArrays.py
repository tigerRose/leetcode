
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

    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0



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
