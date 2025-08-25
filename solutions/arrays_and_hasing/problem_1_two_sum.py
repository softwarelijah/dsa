"""
Problem: Two Sum (LeetCode #1)
Category: Arrays & Hashing (Neetcode 75)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Constraints:
- ...
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dictionary to store {number: index}
        seen = {}

        # loop through array once
        for i, num in enumerate(nums):
            complement = target - num

            # if complement exists, we found the solution
            if complement in seen:
                return [seen[complement], i]

            # otherwise, store current number with its index
            seen[num] = i

