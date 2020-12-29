# can stringify the int and find the length of the string

# can divide by 10, 1000, 100000 and check mod/remainder;
    # if mod is less than the divisor then it has the same # digits as the divisor

# is list ordered?
    # if so, and first/last digits have same num digits, then we know how many digits the rest have

def findNumbers(nums: List[int]) -> int:

    # initialize a counter at zero
    even_digit_nums = 0
    # loop through each number in the list nums
    for num in nums:
    # find len(str(num)) % 2
        if len(str(num)) % 2 == 0:
            # if this is zero, then increment a counter
            even_digit_nums += 1
    # at the end, return the counter value
    return even_digit_nums