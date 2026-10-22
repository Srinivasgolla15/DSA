# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # la = 0
        # lb = 0

        # curr = headA
        # currb = headB

        # while curr:
        #     la += 1
        #     curr = curr.next

        # while currb:
        #     lb += 1
        #     currb = currb.next

        # curr = headA
        # currb = headB

        # if la > lb:
        #     for i in range(la - lb):
        #         curr = curr.next
        # else:
        #     for i in range(lb - la):
        #         currb = currb.next

        # while curr and currb:
        #     if curr is currb:
        #         return curr

        #     curr = curr.next
        #     currb = currb.next

        # return None

        # curr = headA
        # la = 0
        # lb = 0
        # currb = headB
        # skipA = 0
        # skipB = 0

        # while curr:
        #     la += 1
        #     curr = curr.next

        # curr = headA

        # while currb:
        #     lb += 1
        #     currb = currb.next

        # currb = headB

        # # Align both lists
        # if la > lb:
        #     while skipA < la - lb:
        #         curr = curr.next
        #         skipA += 1
        # else:
        #     while skipB < lb - la:
        #         currb = currb.next
        #         skipB += 1

        # # Compare nodes
        # while curr and currb:
        #     if curr is currb:
        #         return curr

        #     curr = curr.next
        #     currb = currb.next

        # return None


        visited=set()
        while headA:
            visited.add(headA)
            headA=headA.next
        while headB:
            if headB in visited:
                return headB
            headB=headB.next
        return None