class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hashmap
        # iterate over the number array and keep track of index
        # create the complement equation
        # check if the complement is in the hashmap
        # if the complement is in the hashmap, return the index + the complement
        # store the current number as a key and its index as the value for future lookups
        # if nothing is found just return the empty list for the return type requirements


        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []