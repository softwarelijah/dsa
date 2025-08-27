class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Time Complexity:
            - Worst case: O(log n), since the search space is halved each iteration
            - Best case: O(1), if the target is found on the first check
        Space Complexity:
            - O(1), since only a few integer variables are used (left, right, mid)
        """

        # Initialize two pointers for the search range
        left = 0                      # Start of array
        right = len(nums) - 1         # End of array

        # Continue searching while the window [left, right] is valid
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Case 1: Found the target at mid index
            if nums[mid] == target:
                return mid

            # Case 2: Middle value is less than target → search in the right half
            elif nums[mid] < target:
                left = mid + 1

            # Case 3: Middle value is greater than target → search in the left half
            else:
                right = mid - 1

        # Target not found, return -1
        return -1
