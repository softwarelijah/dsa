class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        ans = 0

        leftmax, rightmax = 0, 0
        while left < right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                ans += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                ans += rightmax - height[right]
                right -= 1
        return ans