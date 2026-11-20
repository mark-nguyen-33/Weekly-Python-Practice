# Problem: Write a function second_largest(nums) that takes a 
# list of integers and returns the second largest distinct value. 
# If there isn’t one, return None.
import math

def second_largest(nums: list[int]) -> int|None:
    if len(nums) < 2:
        return None
    
    largest_int : float = -math.inf
    second_largest_int : float = largest_int
    for num in nums:
        if num > largest_int: 
            second_largest_int = largest_int
            largest_int = num
        elif num < largest_int and num > second_largest_int:
            second_largest_int = num

    if second_largest_int == -math.inf: return None
    
    return int(second_largest_int)

nums : list[int] = [10, 10, 9]
print(f"{second_largest(nums)}")