class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # get the length of the array
        # initialize the answer array (so the multiplication works correctly)
        # variable to hold running product from the left side
        # first pass: multiply everything to the left of current index
        # set ans[i] to product of all elements before it
        # update left_prod by multplying current number
        # second pass: return steps for right side
        # return ans

        n=len(nums)
        ans = [1] * n
        leftprod = 1
        for i in range(n):
            ans[i] = leftprod
            leftprod *= nums[i]
        rightprod = 1
        for i in range(n-1, -1, -1):
            ans[i] *= rightprod
            rightprod *= nums[i]
        return ans