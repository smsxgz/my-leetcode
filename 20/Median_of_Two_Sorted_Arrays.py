#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:07:32 2017

@author: smsxgz
"""


class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n) // 2
        while (imin <= imax):
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and A[i] < B[j - 1]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                if (m + n) % 2 == 1:
                    return min_of_right

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])
                return ((max_of_left + min_of_right) / 2.)
