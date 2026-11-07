# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: Optional[ListNode]
#         :type k: int
#         :rtype: Optional[ListNode]
#         """
#         if not head or k==0:
#             return head
#         dummy = ListNode(0)
#         ro = dummy
#         curr = head
#         fast = curr
#         slow = curr
#         count = 0
#         while curr:
#             count+=1
#             curr = curr.next
#         k=k%count
#         if k == 0:
#             return head
#         for _ in range(k):
#             fast = fast.next
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
#         dummy.next = slow.next
#         # breaks the cycle
#         slow.next = None 
#         fast.next = head
#         return ro.next

     
  
 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and old tail
        count = 1
        fast = head

        while fast.next:
            count += 1
            fast = fast.next

        # Step 2: Remove unnecessary rotations
        k = k % count

        if k == 0:
            return head

        # Step 3: Find the new tail using one pointer
        steps = count - k
        curr = head

        for _ in range(steps - 1):
            curr = curr.next

        # Step 4: Change the links
        new_head = curr.next
        curr.next = None
        fast.next = head

        return new_head
       