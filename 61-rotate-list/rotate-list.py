# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # if not head or k==0:
        #     return head
        # dummy = ListNode(0)
        # ro = dummy
        # curr = head
        # fast = curr
        # slow = curr
        # count = 0
        # while curr:
        #     count+=1
        #     curr = curr.next
        # k=k%count
        # if k == 0:
        #     return head
        # for _ in range(k):
        #     fast = fast.next
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next
        # dummy.next = slow.next
        # slow.next = None
        # fast.next = head
        # return ro.next

     
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 

 
        if not head or not head.next or k == 0:
            return head

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        k = k % count

        if k == 0:
            return head

        fast = head
        slow = head

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head