from typing import List  # Import List type for clearer type hints

# PROBLEM (plain words):
# We have two people's available meeting time slots.
# Each slot is [start, end] in minutes (end is NOT included).
# We want the earliest time range that BOTH are free for at least "duration" minutes.
# If such a shared time exists, return [start, start + duration].
# If not, return an empty list.

class Solution:
    def minAvailableDuration(
            self,
            slots1: List[List[int]],  # Person 1's available time slots
            slots2: List[List[int]],  # Person 2's available time slots
            duration: int             # Required meeting length in minutes
    ) -> List[int]:
        slots1.sort()  # Put person 1's slots in time order
        slots2.sort()  # Put person 2's slots in time order

        pointer1 = 0   # Index into slots1 (current slot we are checking)
        pointer2 = 0   # Index into slots2 (current slot we are checking)

        # Walk through both lists while neither pointer is past the end
        while pointer1 < len(slots1) and pointer2 < len(slots2):
            # Find the overlap window between the two current slots:
            intersect_right = min(slots1[pointer1][1], slots2[pointer2][1])  # Earliest ending time
            intersect_left = max(slots1[pointer1][0], slots2[pointer2][0])   # Latest starting time

            # Check if the overlap is big enough for the meeting
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]  # Return earliest valid meeting window

            # Move past the slot that ends first (it can't help anymore)
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1 += 1  # Advance in slots1
            else:
                pointer2 += 1  # Advance in slots2

        return []  # No shared slot long enough was found