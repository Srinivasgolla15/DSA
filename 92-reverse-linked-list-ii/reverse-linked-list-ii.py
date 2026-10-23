class Solution(object):
    def reverseBetween(self, head, left, right):
        # if not head or left == right:
        #     return head

        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy

        # # Move prev to the node before position left
        # for i in range(left - 1):
        #     prev = prev.next

        # curr = prev.next

        # # Reverse the section from left to right
        # for i in range(right - left):
        #     nxt = curr.next.next
        #     temp = curr.next

        #     curr.next.next = prev.next
        #     prev.next = temp
        #     curr.next = nxt

        # return dummy.next


        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        count = 1
        while count < left:
            prev = prev.next
            count += 1

        curr = prev.next

        count = 0
        while count < right - left:
            nxt = curr.next.next
            temp = curr.next

            curr.next.next = prev.next
            prev.next = temp
            curr.next = nxt

            count += 1

        return dummy.next