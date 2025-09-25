# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # STEP 1: Find the middle of the linked list
        # 'slow' moves one step at a time, 'fast' moves two steps.
        # When 'fast' reaches the end, 'slow' will be in the middle.
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2: Split the list into two halves
        # 'second' starts at the node after the middle.
        # Cut the list in half by setting slow.next = None.
        second = slow.next
        slow.next = None

        # STEP 3: Reverse the second half of the list
        # (So we can later weave it into the first half.)
        prev = None
        while second:
            tmp = second.next   # temporarily store next node
            second.next = prev  # reverse the pointer
            prev = second       # move prev forward
            second = tmp        # move second forward
        # At the end, 'prev' points to the head of the reversed second half.

        # STEP 4: Merge the two halves together
        # One node from the first half, then one from the reversed second half, etc.
        first = head
        second = prev
        while second:
            tmp1 = first.next   # store next node from first half
            tmp2 = second.next  # store next node from second half

            first.next = second # link current first node to current second node
            second.next = tmp1  # link current second node to next first node

            # move both pointers forward
            first = tmp1
            second = tmp2



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Fast and Slow Pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next # slow goes + 1
            fast = fast.next.next # fast goes + 2


        # splitting the list into halves
        # second starts at the node after the middle
        # cut the list in half by setting slow.next = None
        second = slow.next
        slow.next = None

        # Reverse the second half of the list
        prev = None
        while second: # reversing a linked list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # now we need to merge the two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next # store next node from the first half
            tmp2 = second.next # store next node from second half 

            first.next = second # link current first node to current second node
            second.next = tmp1 # link current second node to first node

            # move both pointers forward
            first = tmp1 
            second = tmp2



