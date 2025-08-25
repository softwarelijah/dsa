# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a pointer to the previous node as None (since the new tail will point to None)
        prev = None 
        
        # Start with the head of the list as the current node
        curr = head
        
        # Iterate through the linked list until we reach the end (curr becomes None)
        while curr:
            # Save the next node so we don’t lose track of the rest of the list
            temp_next = curr.next
            
            # Reverse the current node’s pointer to point to the previous node
            curr.next = prev
            
            # Move the previous pointer forward to the current node
            prev = curr
            
            # Move the current pointer forward to the saved next node
            curr = temp_next
        
        # At the end, prev will be the new head of the reversed list
        return prev



# Time Complexity: O(n) 
  #  - Each node is visited exactly once, where n is the number of nodes in the linked list.

# Space Complexity: O(1) 
   # - Only a constant amount of extra memory is used (prev, curr, temp_next).
