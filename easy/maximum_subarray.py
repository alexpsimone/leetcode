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

    # If the list is empty, return 0?
    # If the list contains one value only, return that value.

    # Initialize a sum with value 0.
    # Look at sliding windows of various lengths across the list?
    # Start with a window of length 1, go until window of length n.
    # Slide across nums and slice the list accordingly, calculating sums across each window.
    # If the value of the sum is greater than sum, then replace sum.
    # Return the value of sum.
    # I think this is more like an O(n) runtime, but there's a better way than this!

    # Initialize a sum with value 0.
    # Start at first item in the list.
    # Find sum of the item plus the next item in the list. Then add the one after that...
    # If a value higher than sum is found, then replace it with the new sum; otherwise keep going until the end of the list.
    # Now go to the 2nd item in the list.
    # Find the sum of that item plus the next item. Then add the one after that...
    # Until you reach the end of the list.

    # Return the value of sum.
    # Slow runtime here.


