class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        result = []
        for i in nums:
            running_sum += i
            result.append(running_sum)
        return result


# O(N) time and space complexity