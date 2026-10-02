"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# class Solution(object):

#     def flatten(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """

#         if not head:
#             return None

#         self.flatten_list(head)

#         return head

#     def flatten_list(self, curr):

#         tail = curr

#         while curr:

#             next_node = curr.next

#             if curr.child:

#                 child = curr.child

#                 # Flatten child and get its tail
#                 child_tail = self.flatten_list(child)

#                 # curr -> child
#                 curr.next = child
#                 child.prev = curr

#                 # child_tail -> original next
#                 if next_node:
#                     child_tail.next = next_node
#                     next_node.prev = child_tail

#                 curr.child = None

#                 tail = child_tail

#             else:
#                 tail = curr

#             # Continue with original next node
#             curr = next_node

#         return tail



class Solution(object):
    def flatten(self, head):
        if not head:
            return None

        stack = []
        current = head

        while current or stack:
            if current.child:
                if current.next:
                    stack.append(current.next)
                current.next = current.child
                current.child.prev = current
                current.child = None
            if not current.next and stack:
                next_node = stack.pop()
                current.next = next_node
                next_node.prev = current
            current = current.next

        return head
        
        
        