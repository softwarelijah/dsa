class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums) # cache length to avoid recomputing len(nums)
        ans = [1] * n # initialize ans with 1s; will store final products

        # left pass
        # after this loop,
        left_prod = 1
        for i in range(n):
            ans[i] = left_prod
            left_prod *= nums[i]

        right_prod = 1
        for i in range(n -1, -1, -1):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans