# one list of ints sorted in ASCENDING order
# return INDICES of values in list whose sum is a target number
# indices start at 1, not 0
# indices must be different
# only one solution possible

# how to handle empty list?
# how to handle unexpected data types in a list?
# can we expect any numbers to be repeated?
# are there only positive ints? don't think it should matter...
# how to handle list with 2 items that don't add to target? out of scope for this problem.

# Brute force method:
# if len(numbers) == 2, then return [1,2]
# set idx1 = 0, idx2 = 1
# loop through values of idx1 from 0 to len(numbers) - 2
# loop again through values for idx2 from (idx1 + 1) to len(numbers) - 1
# add numbers[idx1] + numbers[idx2]
# check sum against target
# if sum is smaller, then increment idx2
# if sum is greater, then increment idx1 and reset idx2 = idx1 + 1
# if sum is equal, then return [idx1+1, idx2+1]

# Binary Search Method:
# if len(numbers) == 2, then return [1,2]
# set idx1 = 0, idx2 = len(numbers)/2

    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        