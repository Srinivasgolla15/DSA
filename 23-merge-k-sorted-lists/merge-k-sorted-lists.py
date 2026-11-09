# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

# -----------------Sequential Merge O(NK) O(1)--------------------------
        # res = None
        # def rec( list1,list2):
        #     dummy = ListNode()
        #     tail =dummy
        #     while list1 and list2:
        #         if list1.val<list2.val:
        #             tail.next = list1 
        #             list1=list1.next
        #         else:
        #             tail.next = list2 
        #             list2 = list2.next
        #         tail=tail.next
        #     if list1:
        #         tail.next = list1 
        #     if list2:
        #         tail.next = list2 
            
        #     return dummy.next
        # for i in range(len(lists)):
        #     res =rec( res,lists[i])
        # return res

  # ---------------- MERGE TWO SORTED LINKED LISTS O(N log K) O(K) --------------
        # def merge(list1, list2):

        #     dummy = ListNode()
        #     tail = dummy

        #     while list1 and list2:

        #         if list1.val < list2.val:
        #             tail.next = list1
        #             list1 = list1.next
        #         else:
        #             tail.next = list2
        #             list2 = list2.next

        #         tail = tail.next

        #     # Attach the remaining nodes
        #     if list1:
        #         tail.next = list1

        #     if list2:
        #         tail.next = list2

        #     return dummy.next

        # # ---------------- EDGE CASE ----------------
        # if not lists:
        #     return None

        # # ---------------- DIVIDE & CONQUER ----------------
        # while len(lists) > 1:

        #     mergedLists = []

        #     # Merge lists in pairs
        #     for i in range(0, len(lists), 2):

        #         list1 = lists[i]

        #         # If there is no pair, use None
        #         list2 = lists[i + 1] if i + 1 < len(lists) else None

        #         mergedLists.append(merge(list1, list2))

        #     # Replace old lists with newly merged lists
        #     lists = mergedLists

        # return lists[0]


# ---------------- TIME COMPLEXITY ----------------
# O(N log K)
# N = Total number of nodes
# K = Number of linked lists

# ---------------- SPACE COMPLEXITY ----------------
# O(1) extra space (excluding the output list)
# O(K) temporary space for mergedLists in each round


# -------------------Min Heap O(N log K) O(K)-------------------
         # ---------------- CREATE AN EMPTY MIN HEAP ----------------
        # heap = []

        # # ---------------- PUT THE HEAD OF EVERY LIST INTO THE HEAP ----------------
        # for i, node in enumerate(lists):

        #     if node:
        #         heapq.heappush(heap, (node.val, i, node))

        # # ---------------- DUMMY NODE FOR THE RESULT ----------------
        # dummy = ListNode()
        # tail = dummy

        # # ---------------- PROCESS THE HEAP ----------------
        # while heap:

        #     # Remove the smallest node
        #     value, i, node = heapq.heappop(heap)

        #     # Add it to the answer
        #     tail.next = node
        #     tail = tail.next

        #     # Push the next node from the same list
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next))

        # return dummy.next

        

# ----------------COLLECT,SORT AND BUILd-------------------------------------
        values = []

        # ---------------- Collect all values ----------------
        for head in lists:

            while head:
                values.append(head.val)
                head = head.next

        # ---------------- Sort all values ----------------
        values.sort()

        # ---------------- Build a new linked list ----------------
        dummy = ListNode()
        tail = dummy

        for value in values:

            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next


# ---------------- TIME COMPLEXITY ----------------
# Collect all nodes : O(N)
# Sort all values   : O(N log N)
# Build new list    : O(N)
#
# Total Time: O(N log N)

# ---------------- SPACE COMPLEXITY ----------------
# values array : O(N)
# New linked list : O(N)
#
# Auxiliary Space: O(N)


