#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:41:10 2017

@author: smsxgz
"""


def removeElement(nums, val):
    j = 0
    m = len(nums) - 1
    while (j <= m):
        if nums[j] == val:
            nums[j] = nums[m]
            m = m - 1
        else:
            j += 1
    nums = nums[:j]
    return j


removeElement([3, 2, 2, 3], 3)
