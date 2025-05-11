# page 238 Boundary Thinking Problem Set
"""
Try to find a runtime lower bound and a runtime upper bound for each of the following problems.
- for lower bound, take the max between the output-size lower bound and the task-based lower bound
- for upper bound, take the min between the naive upper bound and the TLE upper bound
"""

# 1 Consecutive Letters
"""
Given a string s, with n lowercase English letters, return the longest sequence of consecutive letters in the
alphabet such that all the letters appear in the string.
e.g. 
s = "onion"
output = "no"

s = "axdxbxc"
output = "abcd"
constraints n <= 100,000
"""

"""
Work
Lower bound:
output-size lower bound: O(1), n = 26 because the longest consectuive sequence of letters is the alphabet
task-based lower bound: O(n) the task requires us to iterate through each character of the string.
Upper bound:
naive upper bound: O(n log n), we can sort the letters then look through the sorted list to find the longest sequence.
TLE upper bound: O(n), O(n log n), anything sub quadratic.

max(O(1), O(n)) = O(n)
min(O(n), O(n log n)) = O(n)
"""

# 2 Sorted Ternary Array
"""
Given an array, arr, of length n, return an array with the same elements but in sorted order. The array only contains 0s, 1s, and 2s.
e.g.
arr = [2, 2, 0, 2, 1]
output = [0, 1, 2, 2, 2]
constraints: n <= 100,000
"""

"""
Work
Lower bound:
output-size lower bound: O(n) output size is equal to input size
task-based lower bound: O(n) to read every index. O(n log n) doesn't apply because of the special case of an array having only three unique values.
Upper bound:
naive upper bound: O(n log n) built in naive sort function
TLE upper bound: O(n log n), O(n) sub quadratic.

max(O(n), O(n)) = O(n)
min(O(n), O(n log n)) = O(n)
"""

# 3 Valley Array Min
"""
Given a valley array, arr, of length n, return the smallest value. A valley array is an array of unique integers that first decreases
and then increases.
e.g.
arr = [8, 5, 2, 7, 13, 14, 19, 21]
output = 2
"""

"""
Work
Lower bound:
output-size lower bound: O(1) 
task-based lower bound: O(1), we don't need to always check every element.
Upper bound:
naive upper bound: O(n)
TLE upper bound: None

max(O(1), O(1)) = O(1)
min(O(n), None) = O(n)
"""

# 4 subsets
"""
Given a positive integer n, return an array with every possible subset of the numbers from 1 to n as a nested array. The order of the 
subarrays or the elements in each subarray doesn't matter.
e.g. 
n = 3
output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]  output length is 8, which is 2^n and not n!
constraints: 1 < n <= 15
Lower bound:
output-size lower bound: O(2^n * n), 2^n subsets, each subset has n elements
task-based lower bound: None
Upper bound:
naive upper bound: O(2^n * n) naive algorithm is to generate all subsets with backtracking.
TLE upper bound: Exponential, maybe factorial

max(O(2^n * n), None) = O(2^n * n)
min(O(2^n * n), Exponential) = O(2^n * n)
"""

# 5 Subarrays
"""
Given an array, arr, with n unique integers, return an array with every unique subarray (unlike subsets, subarrays are contiguous).
e.g.
arr = [8, 2, 4]
output = [[8], [2], [4], [8, 2], [2, 4], [8, 4], [8, 2, 4]]
constraints: 1 <= n <= 300
Lower bound:
output-size lower bound: O(n^3), there are O(n^2) subarrays, and each subarray has O(n) elements. O(n^2 * n)
task-based lower bound: O(n) because we need to read every number
Upper bound:
naive upper bound: O(n^3) we can solve this problem with three nested loops
TLE upper bound: O(n^3) = Cubic

max(O(n^3), O(n)) = O(n^3)
min(O(n^3), O(n^3)) = O(n^3)
"""

# 6 sum-k subarrays
"""
Given an array, arr, with n integers, and an integer, k, return the number of subarrays with a sum equal to k.
e.g.
arr = [2, 2, 4, -2], k = 4
output = 3, The subarrays with sum 4 are [2, 2], [4], [2, 4, -2]
constraints: 1 <= n <= 10^6

Lower bound:
output-size lower bound: O(1) just return an integer
task-based lower bound: O(n) we need to read every number
Upper bound:
naive upper bound: O(n^3), we can solve this problem with three nested loops
TLE upper bound: O(n log n)

max(O(1), O(n)) = O(n)
min(O(n^3), O(n log n)) = O(n log n)
"""

# 7 sum over 100
"""
Given an array, arr, of n positive integers, return whether their sum is greater than 100.
constraints: 1 < b <= 10^6
Lower bound:
output-size lower bound: O(1) just return a boolean
task-based lower bound: O(1) since we have positive integers, at most we only need to iterate through 100 numbers O(100) = O(1)
Upper bound:
naive upper bound: O(n)
TLE upper bound: O(n log n)

max(O(1), O(1)) = O(1)
min(O(n), O(n log n)) = O(n)
"""

# 8 Sudoku
"""
You are giecn a 9x9 grid representing a Sudoku puzzle. Your goal is to solve the Sudoku.
Lower bound:
output-size lower bound: O(81) => O(1) always return a 9x9 grid
task-based lower bound: need to at least iterate through each cell of the grid once.
Upper bound:
naive upper bound: O(9^9)
TLE upper bound: None

max(O(81), O(9^9)) = O(9^9)
min(O(9^9), None) = O(9^9)

Any algorithm technically takes O(1) time. Big O analysis is not very useful. We should focus on minimizing constant factors.
"""

# 9 connected points
"""
Given n points in the plane where each point consists of coordinates (x, y), find the shortest path in the plane that goes through every point and
return its length.
constraints: 2 <= n <= 10

Lower bound:
output-size lower bound: O(1)
task-based lower bound: O(n) since we need to at least know where all the points are.
Upper bound:
naive upper bound: O(n! * n) to consider all possible ordering of points with backtracking
TLE upper bound: O(n!)

max(O(1), O(n)) = O(n)
min(O(n! * n), O(n!)) = O(n!)

A versino of TSP, NP complete problem.
"""

