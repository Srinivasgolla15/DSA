class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        curr = head

        # First traversal: create copies
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Second traversal: connect pointers
        while curr:
            copy = old_to_new[curr]

            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)

            curr = curr.next

        return old_to_new[head]