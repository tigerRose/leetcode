#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        max_length = 0
        curr_length = 0
        max_str = ''
        curr_str = ''
        for v in s:
            if curr_str == '' or v not in curr_str:
                curr_str += v
                curr_length += 1
            else:
                curr_length = curr_length - curr_str.index(v)
                curr_str = curr_str[curr_str.index(v)+1:] + v

            if curr_length > max_length:
                max_str = curr_str
                max_length = curr_length
            # print curr_str, curr_length, max_str, max_length
        return max_length

