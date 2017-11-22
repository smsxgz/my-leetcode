#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:37:28 2017

@author: smsxgz
"""

import numpy as np

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        #m, n = np.array(dungeon).shape
        m, n = len(dungeon), len(dungeon[0])
        HP = [[1] * n] * m
        
        for i in range(m - 1 , -1, -1):
            for j in range(n - 1, -1, -1):
                v = dungeon[i][j]
                if i == m - 1 and j == n - 1:
                    HP[i][j] = max(1 - v, 1)
                elif i == m - 1:
                    HP[i][j] = max(HP[i][j + 1] - v, 1)
                elif j == n - 1:
                    HP[i][j] = max(HP[i + 1][j] - v, 1)
                else:
                    HP[i][j] = max(min(HP[i + 1][j], HP[i][j + 1]) - v, 1)
        return HP[0][0]


s = Solution()
dungeon = [[0, -3]]
k = s.calculateMinimumHP(dungeon)
print(k)

