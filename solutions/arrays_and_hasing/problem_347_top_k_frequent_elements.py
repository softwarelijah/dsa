from collections import Counter
import heapq  # need to import this for nlargest to work

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Time Complexity:
            - Building the Counter: O(n), where n = len(nums)
            - heapq.nlargest on m unique elements: O(m log k), 
              where m is the number of distinct numbers
            - Overall: O(n + m log k)
              (since m ≤ n, this is effectively O(n log k) in the worst case)

        Space Complexity:
            - O(m) for the Counter (hashmap storing frequency counts)
            - O(k) for the heap created by nlargest
            - Overall: O(m + k)
        """

        # If k equals the size of nums, then every number is frequent,
        # so just return the original nums list
        if k == len(nums):
            return nums

        # Count the frequency of each number in nums
        # Example: nums = [1,1,1,2,2,3] → Counter = {1:3, 2:2, 3:1}
        count = Counter(nums)

        # Use heapq.nlargest to get the top k frequent elements
        # - count.keys() are the unique numbers
        # - key=count.get means elements are compared by their frequency
        # Example: topKFrequent([1,1,1,2,2,3], 2) → [1,2]
        return heapq.nlargest(k, count.keys(), key=count.get)
