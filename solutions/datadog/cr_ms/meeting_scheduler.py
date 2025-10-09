from typing import List

"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

"""""


def meeting_scheduler(slot1: List[List[int]], slot2:List[List[int]], duration: int) -> List[int]:

  slot1.sort()
  slot2.sort()
  p1 = 0
  p2 = 0

  while p1 < len(slot1) and p2 < len(slot2):
    intersect_right = min(slot1[p1][1], slot2[p2][1])
    intersect_left = max(slot1[p1][0], slot2[p2][0])

    if intersect_right - intersect_left >= duration:
      return [intersect_left, intersect_left + duration]
    
    if slot1[p1][1] < slot2[p2][1]:
      p1 += 1
    else:
      p2 += 1
  return []


def test_meeting_scheduler():
  result = meeting_scheduler([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)
  assert result == [60, 68]
  print("input 1 passed")

  result = meeting_scheduler([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12)
  assert result == []
  print("input 2 passed")

test_meeting_scheduler()

"""
DATA STRUCTURES:
- Array (List of Lists): slot1 and slot2 represent time intervals as [start, end] pairs
  - Each inner array is a 2-element list representing a time slot
  - Sorted in ascending order by start time to enable chronological processing
- Two Pointers: p1 and p2 track current positions in slot1 and slot2 respectively
  - Enable simultaneous traversal of both sorted arrays without nested loops
- Integer Variables: intersect_left, intersect_right store boundaries of interval intersection

ALGORITHMS:
- Two-Pointer Technique: Traverse two sorted arrays simultaneously to find overlapping intervals
  - Move pointers independently based on which interval ends first
  - Avoids O(n*m) brute force comparison of all pairs
- Interval Intersection: Find overlapping portion of two time slots
  - Left boundary: max(start1, start2) - the later of the two start times
  - Right boundary: min(end1, end2) - the earlier of the two end times
  - Valid intersection when right >= left
- Greedy Algorithm: Return the first valid meeting slot found
  - Since arrays are sorted, the first match is automatically the earliest possible time
- Sorting: Pre-process both slot arrays in ascending order by start time
  - Enables chronological comparison and guarantees earliest slot is found first
- Pointer Advancement Strategy: Move the pointer whose slot ends earlier
  - If slot1[p1] ends before slot2[p2], increment p1 (no future overlap possible with current slot1)
  - Otherwise increment p2
  - Ensures all potential overlaps are checked

TIME COMPLEXITY: O(n log n + m log m)
- Where n is the length of slot1 and m is the length of slot2
- Sorting slot1: O(n log n)
- Sorting slot2: O(m log m)
- Two-pointer traversal: O(n + m)
  - Each pointer moves forward at most n or m times respectively
  - Each iteration performs constant-time operations (comparisons, min/max calculations)
- Total: O(n log n + m log m) since sorting dominates

SPACE COMPLEXITY: O(1) or O(n + m) depending on sorting implementation
- If the sort is in-place (like Python's Timsort in worst case): O(n + m) auxiliary space
- If we consider the sort as modifying input in-place: O(1) extra space
- Additional variables (p1, p2, intersect_right, intersect_left): O(1)
- No additional data structures that scale with input size

Typically reported as O(1) auxiliary space beyond the input arrays.

Algorithm Explanation:
- This is a classic two-pointer interval intersection problem
- We sort both slot arrays to process them in chronological order
- For each pair of slots, we find the intersection using:
  - Left boundary: max(start1, start2) - the later start time
  - Right boundary: min(end1, end2) - the earlier end time
- If the intersection is large enough for the meeting duration, we return it
- We advance the pointer whose slot ends earlier to look for the next potential intersection
- This greedy approach works because we process slots in order and return the first valid match
"""