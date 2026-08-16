class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """


# -------------------Brute-force Sliding Window Median using Sorting---
# Time: O((n-k+1) × k log k) ≈ O(nk log k)
# Space: O(k)
# Time Limit Exceeded 44 / 45 testcases passed


        # res=[]
        # def median(arr):
        #     arr.sort()
        #     if k%2==0:
        #         med = (arr[k//2]+arr[(k//2)-1])/2.0
        #     else:
        #         med = arr[k//2] 
        #     return med
        # for i in range(len(nums)-k+1):
        #     res.append(median(nums[i:i+k]))
        # return res


# ----------------Sliding window + Two-Heaps + lazy deletion--------------------

        # To store the medians
        # medians = []

        # # To keep track of the numbers that need to be removed from the heaps
        # outgoing_num = {}

        # # Max heap
        # small_list = []

        # # Min heap
        # large_list = []

        # # Initialize the max heap by multiplying each element by -1
        # for i in range(k):
        #     heappush(small_list, -nums[i])

        # # Transfer the top 50% of the numbers from max heap to min heap
        # # while restoring the sign of each number
        # for i in range(k // 2):
        #     element = heappop(small_list)
        #     heappush(large_list, -element)

        # # Variable to keep the heaps balanced
        # balance = 0

        # i = k
        # while True:
        #     # If the window size is odd
        #     if k % 2 == 1:
        #         medians.append(float(-small_list[0]))
        #     else:
        #         medians.append((-small_list[0] + large_list[0]) * 0.5)

        #     # Break the loop if all elements have been processed
        #     if i >= len(nums):
        #         break

        #     # Outgoing number
        #     out_num = nums[i - k]

        #     # Incoming number
        #     in_num = nums[i]
        #     i += 1

        #     # If the outgoing number is from max heap
        #     if out_num <= -small_list[0]:
        #         balance -= 1
        #     else:
        #         balance += 1

        #     # Add/Update the outgoing number in the hash map
        #     outgoing_num[out_num] = outgoing_num.get(out_num, 0) + 1

        #     # If the incoming number is less than the top of the max heap, add it in that heap
        #     # Otherwise, add it in the min heap
        #     if in_num <= -small_list[0]:
        #         balance += 1
        #         heappush(small_list, -in_num)
        #     else:
        #         balance -= 1
        #         heappush(large_list, in_num)

        #     # Re-balance the heaps
        #     if balance < 0:
        #         heappush(small_list, -heappop(large_list))
        #     elif balance > 0:
        #         heappush(large_list, -heappop(small_list))

        #     # Since the heaps have been balanced, we reset the balance variable to 0.
        #     balance = 0

        #     # Remove invalid numbers present in the hash map from top of max heap
        #     while (
        #         small_list
        #         and -small_list[0] in outgoing_num
        #         and outgoing_num[-small_list[0]] > 0
        #     ):
        #         outgoing_num[-small_list[0]] -= 1
        #         heappop(small_list)

        #     # Remove invalid numbers present in the hash map from top of min heap
        #     while (
        #         large_list
        #         and large_list[0] in outgoing_num
        #         and outgoing_num[large_list[0]] > 0
        #     ):
        #         outgoing_num[large_list[0]] -= 1
        #         heappop(large_list)

        # return medians

# --------2heaps + delay time chatgpt code O(n log k) O(k)------------


        # max heap → stores the smaller half of the window
        # Python only has a min heap, so we store negative values.
        small = []

        # min heap → stores the larger half of the window
        large = []

        # delayed[x] = number of times x has left the window
        # but is still physically present inside a heap.
        delayed = {}

        # These are the number of VALID elements in each heap.
        # We cannot always use len(small)/len(large) because
        # heaps can contain elements waiting for lazy deletion.
        small_size = 0
        large_size = 0

        result = []

        for i, x in enumerate(nums):

            # =====================================================
            # 1. REMOVE THE ELEMENT THAT LEFT THE SLIDING WINDOW
            # =====================================================

            if i >= k:

                # nums[i-k] is the element that is no longer
                # inside the current window.
                old = nums[i - k]

                # We don't search through the heap to remove it.
                # Instead, mark it for lazy deletion.
                delayed[old] = delayed.get(old, 0) + 1

                # Remove old from the logical size.
                # We decide which heap it belonged to using the
                # boundary between the two heaps.
                if old <= -small[0]:
                    small_size -= 1
                else:
                    large_size -= 1

            # =====================================================
            # 2. ADD THE NEW ELEMENT
            # =====================================================

            # small contains the smaller half.
            # If x belongs to the smaller half, put it in small.
            if not small or x <= -small[0]:

                # Store -x because heapq is a MIN heap.
                # Example: actual value 5 → store -5.
                heapq.heappush(small, -x)

                small_size += 1

            else:

                # x belongs to the larger half.
                heapq.heappush(large, x)

                large_size += 1

            # =====================================================
            # 3. REBALANCE THE TWO HEAPS
            # =====================================================

            # For odd k:
            #
            #     small has ONE more element than large
            #
            # For even k:
            #
            #     both have the same number of elements
            #
            # So small is allowed to have at most one extra element.

            if small_size > large_size + 1:

                # Move the largest element from small
                # to large.
                value = -heapq.heappop(small)

                heapq.heappush(large, value)

                small_size -= 1
                large_size += 1

            elif large_size > small_size:

                # Move the smallest element from large
                # to small.
                value = heapq.heappop(large)

                heapq.heappush(small, -value)

                large_size -= 1
                small_size += 1

            # =====================================================
            # 4. LAZY DELETION / PRUNING
            # =====================================================

            # If the top of small is an element that already
            # left the window, physically remove it now.
            #
            # We only remove it when it reaches the top because
            # heapq cannot efficiently delete an arbitrary element.

            while small and -small[0] in delayed:

                value = -heapq.heappop(small)

                delayed[value] -= 1

                if delayed[value] == 0:
                    del delayed[value]

            # Do the same thing for large.
            while large and large[0] in delayed:

                value = heapq.heappop(large)

                delayed[value] -= 1

                if delayed[value] == 0:
                    del delayed[value]

            # =====================================================
            # 5. CALCULATE MEDIAN
            # =====================================================

            # We only have a complete window once we've processed
            # at least k elements.
            if i >= k - 1:

                if k % 2 == 1:

                    # Odd window:
                    #
                    # small has one extra element.
                    # Its largest element is the median.
                    median = float(-small[0])

                else:

                    # Even window:
                    #
                    # median = average of:
                    # largest element in small
                    # smallest element in large
                    median = (-small[0] + large[0]) / 2.0

                result.append(median)

        return result




        