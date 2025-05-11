from typing import List

# Problem 29.1 Search in sorted array
"""
Given a sorted array of integers, arr, and a target value, target, return the target's index if it exists in the
array or -1 if it doesn't.
▶ Example: arr = [-2, 0, 3, 4, 7, 9, 11], target = 3
Output: 2.
▶ Example: arr = [-2, 0, 3, 4, 7, 9, 11], target = 2
Output: -1.
"""
def binary_search(arr, target):
    result_idx = -1
    start_idx = 0
    end_idx = len(arr) - 1  # 6
    while start_idx <= end_idx:  # (0, 6), (0, 3) 
        mid_idx = (start_idx + end_idx) // 2  # 3, 2
        if arr[mid_idx] == target:  # arr[mid_idx] = 4 != 3 
            result_idx = mid_idx
            return result_idx
        elif arr[mid_idx] > target:
            end_idx = mid_idx  # 3
        elif arr[mid_idx] < target:
            start_idx = mid_idx
    return result_idx

# Git Commits
"""
Find the first commit that fails a test in a sequence of Git commits. We know the test was passing for every commit until it started failing at some point.
["pass", "pass", "pass", "pass", "fail", "fail", "fail"]
"""
"""
Target: first fail
target_index - 1 = pass and target_index + 1 = fail
Before region = before first fail
After region = after first fail
"""

def find_first_failed_commit(commits: List):
    # optimized binary search solution O(log n)
    result_idx = -1
    start_idx = 0
    end_idx = len(commits) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2

        if 

    # naive solution O(n)
    # result_idx = -1
    # for i in range(len(commits)):
    #     if commits[i] == "fail":
    #         result_idx = i
    #         return result_idx
    # return result_idx
    

# Squared Target
"""
Given a sorted array of positive integers and a target value, find the largest number in the array that can be squared and still be less than or equal to the target, if any. Return the number (not its index).
[2, 3, 4, 5, 6, 7, 8, 11, 20, 21, 23, 25, 25], target = 36
"""
"""
Target: largest number that when squared is still less than target
Before region: 
After region:
"""

# First non-negative
