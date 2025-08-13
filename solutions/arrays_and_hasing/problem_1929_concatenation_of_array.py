class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans

# O(N) space and time complexity