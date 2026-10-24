# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ------------------CUT-REVERSE-JOIN ----------------------
# class Solution(object):

#     def reverse(self, head):
#         prev = None
#         curr = head

#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt

#         return prev

#     def reverseKGroup(self, head, k):

#         dummy = ListNode(0)
#         dummy.next = head

#         prevGroupTail = dummy

#         while True:

#             # Find kth node
#             kth = prevGroupTail

#             for _ in range(k):
#                 kth = kth.next
#                 if not kth:
#                     return dummy.next

#             groupHead = prevGroupTail.next
#             nextGroup = kth.next

#             # Cut the group
#             kth.next = None

#             # Reverse it
#             newHead = self.reverse(groupHead)

#             # Join
#             prevGroupTail.next = newHead   # connect previous part to new head
#             groupHead.next = nextGroup   # connect new tail to remaining list

#             # Move to next group
#             prevGroupTail = groupHead     # tail becomes the previous tail for the next group

# time : O(n), space : O(1)


# ------------------Head Insertion O(n) O(1)-----------------
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        Reverse nodes in k-sized groups using Head Insertion.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # # Dummy node helps handle the first group easily
        # dummy = ListNode(0)
        # dummy.next = head

        # # Tail of the previous processed group
        # prevGroup = dummy

        # while True:

        #     # ---------------------------------------------------
        #     # Step 1: Check whether k nodes exist
        #     # ---------------------------------------------------

        #     kth = prevGroup

        #     # Move k steps ahead
        #     for _ in range(k):
        #         kth = kth.next

        #         # Less than k nodes left -> don't reverse
        #         if not kth:
        #             return dummy.next

        #     # ---------------------------------------------------
        #     # Current group looks like:
        #     #
        #     # prevGroup
        #     #     |
        #     #     v
        #     # 1 -> 2 -> 3 -> 4 -> ...
        #     #
        #     # curr = 1
        #     # nxt  = 2
        #     # ---------------------------------------------------

        #     curr = prevGroup.next
        #     nxt = curr.next

        #     # ---------------------------------------------------
        #     # Step 2: Reverse the group using Head Insertion
        #     #
        #     # Example (k = 3)
        #     #
        #     # 1 -> 2 -> 3
        #     #
        #     # Move 2 to front
        #     # 2 -> 1 -> 3
        #     #
        #     # Move 3 to front
        #     # 3 -> 2 -> 1
        #     #
        #     # We perform (k-1) moves.
        #     # ---------------------------------------------------

        #     for _ in range(k - 1):

        #         # Remove nxt from its current position
        #         #
        #         # Before:
        #         # 1 -> 2 -> 3 -> 4
        #         #
        #         # After:
        #         # 1 -> 3 -> 4
        #         #
        #         curr.next = nxt.next

        #         # Insert nxt at the front of the current group
        #         #
        #         # Before:
        #         # dummy -> 1 -> 3 -> 4
        #         #
        #         # After:
        #         # 2 -> 1 -> 3 -> 4
        #         #
        #         nxt.next = prevGroup.next

        #         # Connect previous part to nxt
        #         #
        #         # Before:
        #         # dummy -> 1
        #         #
        #         # After:
        #         # dummy -> 2
        #         #
        #         prevGroup.next = nxt

        #         # Move nxt to the next node after curr
        #         #
        #         # curr never moves.
        #         #
        #         # Example:
        #         #
        #         # 2 -> 1 -> 3 -> 4
        #         #      ^
        #         #     curr
        #         #
        #         # nxt becomes 3
        #         #
        #         nxt = curr.next

        #     # ---------------------------------------------------
        #     # curr has become the tail of the reversed group
        #     #
        #     # Example:
        #     #
        #     # dummy
        #     #   |
        #     #   v
        #     # 3 -> 2 -> 1 -> 4 -> 5
        #     #           ^
        #     #        prevGroup
        #     #
        #     # ---------------------------------------------------

        #     prevGroup = curr


     
        if not head or k == 1:
            return head

        nodes = []
        curr = head

        # Step 1: Store all nodes in an array
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: Reverse each complete group of k nodes
        for i in range(0, len(nodes) - k + 1, k):
            nodes[i:i + k] = reversed(nodes[i:i + k])

        # Step 3: Reconnect the nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None

        return nodes[0]