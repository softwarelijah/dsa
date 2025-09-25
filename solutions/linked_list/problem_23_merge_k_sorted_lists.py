# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the input list is empty or None, just return None (no lists to merge)
        if not lists or len(lists) == 0:
            return None

        # Keep merging until we only have one final sorted list left
        while len(lists) > 1:
            merged_Lists = []  # this will temporarily hold the merged results

            # Go through the lists in pairs (two at a time)
            for i in range(0, len(lists), 2): 
                l1 = lists[i]  # first list in the pair
                # if there is a second list available, use it; otherwise, use None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # merge the two sorted lists into one and add to merged_Lists
                merged_Lists.append(self.mergeLists(l1, l2))

            # now merged_Lists replaces lists, and we repeat until one list remains
            lists = merged_Lists

        # when the loop finishes, only one list remains: the fully merged list
        return lists[0]



    # helper method that merges two sorted linked lists into one
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
