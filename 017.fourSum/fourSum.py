

import unittest

class Solution(object):

    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        res = []
        nums.sort()
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        if (nums[i], nums[j], nums[l], nums[r]) not in res:
                            res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res
                

class fourSumTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_fourSum1(self):
        print self.s.fourSum([1,0,-1,0,-2,2], 0)

    def test_fourSum2(self):
        print self.s.fourSum([0,0,0,0], 0)

if __name__ == '__main__':
    unittest.main()

