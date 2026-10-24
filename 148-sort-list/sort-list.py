# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr = sorted(arr)
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            i+=1
            curr = curr.next
        return head
