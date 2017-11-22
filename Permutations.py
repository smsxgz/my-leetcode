#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:52:43 2017

@author: smsxgz
"""

class Solution(object):
    def permute(self, nums):
        '''
        distinct numbers
        '''
        n = nums[0]
        m = len(nums)
        if m == 1:
            return [[n]]
        
        new_perm = []
        perms = self.permute(nums[1:])
        for perm in perms:
            for i in range(m):
                new_perm.append(perm[:i] + [n] + perm[i:])
        return new_perm
    
    def permuteUnique(self, nums):
        '''
        might contain duplicates
        '''
        n = nums[0]
        m = len(nums)
        if m == 1:
            return [[n]]

        new_perm = []
        perms = self.permuteUnique(nums[1:])
        for perm in perms:
            for i in range(m):
                l = perm[:i] + [n] + perm[i:]
                new_perm.append(l)
                if i < m - 1 and perm[i] == n:
                    break
        return new_perm
    
    def nextPermutation(self, nums):
        '''
        next dict permutation
        '''
        m = len(nums)
        j = m - 1
        while j > 0 and nums[j] <= nums[j - 1]:
            j = j - 1
        if j == 0:
            return nums[::-1]
        n = nums[j - 1]
        left, right = j, m - 1
        while(left < right):
            middle = (left + right + 1) // 2
            if nums[middle] > n:
                left = middle
            else:
                right = middle - 1
        nums[j - 1] = nums[left]
        nums[left] = n
        return nums[:j] + nums[m - 1: j - 1: -1]
        
