#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:56:44 2017

@author: smsxgz
"""

from numpy import inf

class Solution(object):
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        l = m - 1
        
        for i in range(m - 1):
            j = m - 2 - i
            num = nums[j]
            if num != 0 and num + j >= l:
                l = j
        return l == 0
    
    
    def jump1(self, nums):
        m = len(nums)
        re = [inf] * m
        re[m - 1] = 0
        for i in range(m - 1):
            j = m - 2 - i
            
            l = inf
            up = j + nums[j] + 1
            if m <= up:
                l = 0
            else:
                l = min(re[j: up])
            re[j] = l + 1
        return re[0]
    
    
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step