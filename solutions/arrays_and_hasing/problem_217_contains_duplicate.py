class Solution(object):
    def containsDuplicate(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set() # creating a hashset, there cannot be duplicates in this ds
        for num in nums: # iterating over the given integer array
            if num in seen: # if num is found in the hashset
                return True # we can return true
            else:
                seen.add(num) # if not, then we can add that value into the hashset
        return False # then return false