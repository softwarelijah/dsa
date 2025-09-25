# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow and fast pointer approach

        # start at the same position
        slow = head
        fast = head

        while fast and fast.next: 
            slow = slow.next # by 1
            fast = fast.next.next # by 2
            if slow == fast:
                return True
        return False