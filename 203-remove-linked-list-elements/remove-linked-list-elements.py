# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        curr = head 
        prev = ListNode(0)
        dummy = prev
        dummy.next = head
        while curr:
            if curr.val == val:
                nxt = curr.next
                prev.next = nxt
                curr = nxt
            else:
                prev = curr
                curr = curr.next
        return dummy.next

            
        