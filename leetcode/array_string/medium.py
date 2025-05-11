from typing import List

class Solution:

    # 15. 3sum
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
    and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Example 2:

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Example 3:

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

    Constraints:
        3 <= nums.length <= 3000
        -105 <= nums[i] <= 105
    """
    """Boundary Thinking

    Lower bound:
    output-size lower bound: O(n) there are n triplets and each triplet has 3 numbers. O(3n) -> O(n)
    task-based lower bound: O(n) because we need to read every number.
    Upper bound:
    naive upper bound: We can generate all possible triplets using 3 nested loops. We just have to figure out how many
    have the sum of 0. O(n^3)
    TLE upper bound: O(n^3)

    max(O(n), O(n)) = O(n)
    min(O(n^3), O(n^3)) = O(n^3)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # naive solution
        # triplets = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             triplet = [nums[i], nums[j], nums[k]]
        #             triplets.append(triplet)
        # results = []
        # for triplet in triplets:
        #     if sum(triplet) == 0:
        #         results.append(triplet)
        # return results
        # improvement, but not on runtime.
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             triplet = [nums[i], nums[j], nums[k]]
        #             if sum(triplet) == 0:
        #                 result.append(triplet)

        # the limit of generating all possible triplets is O(n^3) and we can't do better than that.
        # Techniques: Sorting, how would sorting help? A sorted array means that we know where the smallest and largest element is at any given time. Knowing this relationship means that we can sum them together to try to cancel them out from both ends. All the numbers of similar magnitude would be close together.
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip non zero duplicates
                continue
            left = i + 1
            right = n - 1
            while left < right:
                triplet = [nums[i], nums[left], nums[right]] # [0, 1, 3]
                curr_sum = sum(triplet)
                if curr_sum == 0:
                    triplets.append(triplet)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                if curr_sum < 0:
                    left += 1
                if curr_sum > 0:
                    right -= 1
        return triplets
                
        # Technique: Hash map, how would hash map help? Given 1 number, we know all possible combinations that sum up to 0 and we can directly generate the valid triplets using math. The possible combinations also decrease significantly after we've chosen the second number.


    # 16. 3sum closest
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the 
    sum is closest to target.
    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:

    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    Example 2:

    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

    Constraints:

    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        min_diff = float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                triplet = [nums[i], nums[left], nums[right]]
                curr_sum = sum(triplet)
                diff = abs(target - curr_sum)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum
                    if min_diff == 0:
                        return closest_sum
                if curr_sum < target:
                    left += 1
                if curr_sum > target:
                    right -= 1
        return closest_sum