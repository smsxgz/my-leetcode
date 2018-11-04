#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:56:09 2017

@author: smsxgz
"""


def convert(s, numRows):
    if numRows == 1:
        return s
    expert = [''] * numRows
    i = 0
    j = 1
    for ss in s:
        expert[i] += ss
        if i == numRows - 1 and j == 1:
            j = -1
        elif i == 0 and j == -1:
            j = 1

        i += j

    return ''.join(expert)


print(convert("PAYPALISHIRING", 3))
