

import math
import unittest

class Solution(object):

    def threeSumClosest(self, nums, target):
        res = ''
        nums.sort()
        for i in xrange(len(nums)-2):
            #if i > 0 and nums[i] == nums[i+1]:
            #    continue
            l, r = i+1, len(nums)-1
            while l < r:
                # r = int(math.fabs(nums[i]+nums[l]+nums[r]-target))
                #if res == '' or r < res:
                #    res = r
                s = nums[i]+nums[l]+nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res = target
                    break
                if res == '' or int(math.fabs(s-target)) < int(math.fabs(res-target)):
                    res = s
            
        print res
        return res


class threeSumClosestTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @unittest.skip('1')
    def test_threeSumClosest1(self):
        nums = [-1,2,1,-4]
        target = 1
        assert self.s.threeSumClosest(nums, target) == 2

    @unittest.skip('2')
    def test_threeSumClosest2(self):
        nums = [0,0,0]
        target = 1
        assert self.s.threeSumClosest(nums, target) == 0

    def test_threeSumClosest3(self):
        nums = [0,1,1,1]
        target = 100
        assert self.s.threeSumClosest(nums, target) == 3

if __name__ == '__main__':
    unittest.main()

