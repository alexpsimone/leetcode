# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle.

# What to return for empty array?
# Is the list ordered?
# Are all values positive/negative?
# Do we "wrap around" from 0th to -1st index ever? I'm guessing not?
# Range of int values: -2^31 <= nums[i] <= 2^31 - 1

def maxSubArray(nums: List[int]) -> int:
