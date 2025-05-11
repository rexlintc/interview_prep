# 1 largest connected area
"""
Given an m x n binary matrix mat, find the largest region of ones and return its area.
e.g.
mat = [[0, 0, 1, 1],
       [0, 1, 0, 0],
       [1, 1, 0, 0]]
output = 3
Trigger: not a tree, potentially subarrays (sliding window), potentially greedy
"""

# consecutive ones are flip
"""
given a binary array, arr, return the mximum number of consecutive ones in the array if
you can flip at most one 0 to 1.
e.g.
arr = [1, 0, 0, 1, 0, 1]
output = 3
trigger: constraint, we can flip at most one 0 to 1, try two pointer
"""

# 3 power set
