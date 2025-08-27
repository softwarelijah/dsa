class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Time Complexity:
            - O(n), where n = length of nums
              We scan through the list once, and each lookup in the hashmap is O(1) on average.
        Space Complexity:
            - O(n), since we may store up to n elements in the hashmap (in the worst case).
        """

        # Create an empty hashmap (dictionary in Python)
        # Key   → number from nums
        # Value → its index in the array
        hashmap = {}

        # Iterate through the nums array by index
        for i in range(len(nums)):
            # The "complement" is the number we need to reach the target
            # Example: if target = 9 and nums[i] = 2 → complement = 7
            complement = target - nums[i]

            # If complement is already in the hashmap, we found a pair
            # Return the current index and the index of the complement
            if complement in hashmap:
                return [i, hashmap[complement]]

            # Otherwise, store the current number with its index in the hashmap
            # So future iterations can find it as a complement
            hashmap[nums[i]] = i

        # If no pair is found (problem usually guarantees a solution, but just in case)
        return []
