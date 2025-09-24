class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Start with two pointers: left at the beginning, right at the end
        left = 0
        right = len(nums) - 1

        # Keep going as long as the search window is valid
        while left <= right: 
            # Find the middle index of the current search window
            mid = (left + right) // 2

            # If the middle element is exactly what we're looking for, return it
            if target == nums[mid]:
                return mid

            # ----- Check which side (left or right) is sorted -----

            # If the left half (from left to mid) is sorted:
            if nums[left] <= nums[mid]:
                # Now check if target is *not* in this left portion
                # - if it's bigger than the mid OR smaller than the left edge,
                #   then it must be on the right side
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1   # so shift the window to the right
                else:
                    right = mid - 1  # otherwise it must be in the left half

            # Otherwise, the right half (from mid to right) must be sorted:
            else:
                # Check if target is *not* in this right portion
                # - if it's smaller than mid OR bigger than the right edge,
                #   then it must be on the left side
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1  # so shift the window to the left
                else:
                    left = mid + 1   # otherwise it must be in the right half

        # If we searched everywhere and never found target, return -1
        return -1
