# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # STEP 1: Create a dummy node that points to the head.
        # This helps handle edge cases (like removing the very first node).
        dummy = ListNode(0, head)

        # We'll use two pointers: 'left' and 'right'.
        # 'left' starts at dummy, 'right' starts at the real head.
        left = dummy
        right = head

        # STEP 2: Move 'right' pointer n steps forward.
        # This way, the gap between left and right will be n nodes.
        while n > 0 and right:
            right = right.next
            n -= 1

        # STEP 3: Move both pointers together until 'right' reaches the end.
        # After this, 'left' will be right before the node we want to delete.
        while right:
            left = left.next
            right = right.next

        # STEP 4: Delete the node.
        # 'left.next' is the node we want to remove,
        # so we skip it by linking left directly to left.next.next.
        left.next = left.next.next

        # STEP 5: Return the new head of the list (dummy.next handles the edge case).
        return dummy.next
