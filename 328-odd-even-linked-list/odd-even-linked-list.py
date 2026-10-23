# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even  and  even.next:
            nxt = even.next
            odd.next = nxt
            odd = nxt
            even.next = nxt.next
            even = even.next
        odd.next = evenHead
        return head