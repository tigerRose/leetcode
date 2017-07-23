#!/usr/bin/env python
# -*- coding: utf-8 -*-

def twoSum1(nums, target):
    for i in xrange(len(nums)):
        for j in xrange(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]

def twoSum2(nums, target):
    maps = {}
    for i in xrange(len(nums)):
        if nums[i] in maps:
            return [i, maps[nums[i]]]
        else:
            maps[target-nums[i]] = i

