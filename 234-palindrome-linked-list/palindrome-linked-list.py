class Solution(object):
    def isPalindrome(self, head):

# -----------Array + two pointers  O(n) O(n) ----------------------
        # arr = []
        # curr = head

        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next

        # left = 0
        # right = len(arr) - 1

        # while left < right:
        #     if arr[left] != arr[right]:
        #         return False
        #     left += 1
        #     right -= 1

        # return True

# ---------------Stack  O(n) O(n) -----------------
        # stack = []
        # curr = head

        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next

        # curr = head

        # while curr:
        #     if curr.val != stack.pop():
        #         return False
        #     curr = curr.next

        # return True



# ---------------------------Reverse the second half  O(n) O(1) --------------------------
 
        if not head or not head.next:
            return True

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Compare both halves
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True