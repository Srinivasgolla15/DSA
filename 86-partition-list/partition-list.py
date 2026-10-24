# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        low = []
        high = []
        curr = head
        while curr:
            if curr.val<x:
                low.append(curr.val)
            else:
                high.append(curr.val)
            curr = curr.next
        values = low+high
        curr = head 
        i = 0
        while curr:
            curr.val = values[i]
            i+=1
            curr = curr.next
        return head

        
        