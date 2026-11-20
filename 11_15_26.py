# Problem: Write a function find_pair(nums, target) that returns a tuple (i, j) of two different indices, 
# with i < j, where nums[i] + nums[j] == target. If no such pair exists, return None.

def find_pair(nums : list[int], target : int) -> tuple | None:
    possible_pairs : dict = {}
    for i in range(0, len(nums)):
        pair = target - nums[i]
        pair_index = possible_pairs.get(pair, -1)
        if pair_index != -1:
            return (min(pair_index, i), max(pair_index, i))
        possible_pairs[nums[i]] = i
    return None

nums : list[int] = [1, 2, 3, 5, 6, 2, 3]
target : int = 5

print("Spec examples")
print(find_pair([2, 7, 11, 15], 9), "expected (0, 1)")
print(find_pair([3, 2, 4], 6), "expected (1, 2)")
print(find_pair([3, 3], 6), "expected (0, 1)")
print(find_pair([1, 2, 3], 10), "expected None")
print(find_pair([5], 10), "expected None")
print(find_pair([-1, -2, -3, 4], 1), "expected (2, 3)")

print("Edge cases")
print(find_pair([], 5), "expected None")
print(find_pair([3, 3], 10), "expected None")          # equal numbers, wrong sum
print(find_pair([5], 10), "expected None")             # can't reuse the same element
print(find_pair([3, 1, 3], 6), "expected (0, 2)")      # half-target value, non-adjacent
print(find_pair([7, 2], 9), "expected (0, 1)")         # i < j even when values descend
print(find_pair([0, 4, 0], 0), "expected (0, 2)")      # zeros
print(find_pair([-3, -3], -6), "expected (0, 1)")      # all negative
print(find_pair([1, 5, 5, 1], 10), "expected (1, 2)")  # duplicates, one valid pair