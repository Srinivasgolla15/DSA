# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # if not head or not head.next:
        #     return head

        # start = head
        # prev = None
        # curr = head

        # while curr:
        #     nxt = curr.next

        #     if nxt and curr.val == nxt.val:
        #         value = curr.val

        #         while curr and curr.val == value:
        #             curr = curr.next

        #         if prev:
        #             prev.next = curr
        #         else:
        #             start = curr

        #     else:
        #         prev = curr
        #         curr = curr.next

        # return start

 
        dummy = ListNode(0, head)        # (1)
        prev = dummy                     # (1)
        curr = head                      # (1)

        while curr:
            if curr.next and curr.val == curr.next.val:   # (2)
                dup = curr.val                            # (3)
                while curr and curr.val == dup:           # (3)
                    curr = curr.next
                prev.next = curr                          # (4)
            else:
                prev = curr                               # (5)
                curr = curr.next                          # (5)

        return dummy.next                                 # (6)