# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        start = head
        prev = None
        curr = head

        while curr:
            nxt = curr.next

            if nxt and curr.val == nxt.val:
                value = curr.val

                while curr and curr.val == value:
                    curr = curr.next

                if prev:
                    prev.next = curr
                else:
                    start = curr

            else:
                prev = curr
                curr = curr.next

        return start