from types import List

class Solution:


    # 35. Search Insert Position
    """
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2

    Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1

    Example 3:

    Input: nums = [1,3,5,6], target = 7
    Output: 4
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        [1, 3, 5, 7] target = 7 
        """
        start = 0  # 0
        end = len(nums) - 1  # 3
        while start <= end:
            mid_idx = (start + end) // 2  # 0 + 3 // 2 = 1, 1 + 3 // 2 = 2, 2 + 3 // 2 = 2
            mid_val = nums[mid_idx]  # 3, 5, 5
            if mid_val == target:
                return mid_idx
            elif mid_val < target:
                start = mid_idx + 1  # 1, 2, 2

            elif mid_val > target:
                end = mid_idx - 1
        return start