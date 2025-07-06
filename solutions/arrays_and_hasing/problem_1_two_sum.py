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

        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
