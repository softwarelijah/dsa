"""
Problem: Two Sum (LeetCode #1)
Category: Arrays & Hashing (Neetcode 75)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Constraints:
- ...
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    This function takes an array of integers (nums) and a target integer,
    and returns the indices of the two numbers that add up to the target.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    prevmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevmap:
            return [prevmap[diff], i]
        prevmap[num] = i
    return []
