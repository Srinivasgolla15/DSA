# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        prev = head
        curr = head.next
        while curr :
            if curr.val == prev.val:
                nxt = curr.next
                prev.next = nxt
                curr=nxt
            else:
                nxt = curr.next
                prev = curr
                curr = nxt
        
        return head
        