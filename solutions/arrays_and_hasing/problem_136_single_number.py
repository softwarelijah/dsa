from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = defaultdict(int) # declaring hash table
        for i in nums: # iterate through given array
            hashtable[i] += 1 # increment the count for this number in the hashtable

        # iterate through the hashtable 
        for i in hashtable:
            # if the count of this number is exactly one, return it
            if hashtable[i] == 1:
                # this is the "single number that will appear"
                return i
        
        # Time Complexity O(N)
        # Space Complexity O(N)