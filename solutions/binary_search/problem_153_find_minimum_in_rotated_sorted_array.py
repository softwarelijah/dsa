class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Start by assuming the first number is the smallest
        res = nums[0]

        # Left and right pointers at the start and end of the list
        left = 0
        right = len(nums) - 1

        # Keep checking while the search window is valid
        while left <= right:
            # If the subarray is already sorted (no rotation in this part),
            # then the leftmost number is the smallest for this window.
            if nums[left] < nums[right]:
                res = min(res, nums[left])  # Update result if this is smaller
                break  # No need to continue since it’s sorted

            # Find the middle index
            mid = (left + right) // 2

            # Update result with the middle value (possible minimum)
            res = min(res, nums[mid])

            # If middle element is greater than or equal to the left element,
            # it means the left half is sorted, so the pivot must be on the right side
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # Otherwise, the pivot (minimum) is on the left side
                right = mid - 1

        # Return the minimum value found
        return res
