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

        # curr = head 
        # prev = ListNode(0)
        # dummy = prev
        # dummy.next = head
        # while curr:
        #     if curr.val == val:
        #         nxt = curr.next
        #         prev.next = nxt
        #         curr = nxt
        #     else:
        #         prev = curr
        #         curr = curr.next
        # return dummy.next
        if not head:
            return head
        dummy=ListNode(0,head)
        cur=dummy
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
                cur=cur
            else:
                cur=cur.next
        return dummy.next
            
        