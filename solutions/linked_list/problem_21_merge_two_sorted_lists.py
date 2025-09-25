# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a "dummy" node to start building our merged list.
        # Think of this as a placeholder at the front, so we don’t have to deal with special cases.
        dummy = ListNode()
        
        # Tail always points to the *last node* in the merged list as we build it.
        tail = dummy
        
        # While BOTH lists still have nodes to compare:
        while l1 and l2:
            # If l1’s value is smaller, attach it to the merged list
            if l1.val < l2.val:
                tail.next = l1       # connect tail to l1’s current node
                l1 = l1.next         # move l1 forward
            else:
                # Otherwise l2’s value is smaller (or equal), attach it instead
                tail.next = l2       # connect tail to l2’s current node
                l2 = l2.next         # move l2 forward
            
            # Move the tail forward so it always points to the last node we added
            tail = tail.next
        
        # At this point, at least one list is empty.
        # If l1 still has nodes, connect the rest of l1.
        if l1:
            tail.next = l1
        # Otherwise, if l2 still has nodes, connect the rest of l2.
        elif l2:
            tail.next = l2

        # Return the merged list, but skip the dummy placeholder at the front.
        return dummy.next
