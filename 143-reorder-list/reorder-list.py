class Solution(object):
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        slow = head
        fast = head
        first = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Cut
        second = slow.next
        slow.next = None

        # Reverse
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        # Merge
        while first and second:
            first_nxt = first.next
            second_nxt = second.next

            first.next = second
            second.next = first_nxt

            first = first_nxt
            second = second_nxt