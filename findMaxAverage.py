#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:43:15 2017

@author: smsxgz
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        numsum = 0
        for i in range(k):
            numsum += nums[i]
        average = numsum / k
        MaxAverage = average
        for i in range(k, len(nums)):
            average += (nums[i] - nums[i - k]) / k
            if average > MaxAverage:
                MaxAverage = average
        return MaxAverage


nums = [8,9,3,1,8,3,0,6,9,2]
k = 9

s = Solution()
print(s.findMaxAverage(nums, k))
