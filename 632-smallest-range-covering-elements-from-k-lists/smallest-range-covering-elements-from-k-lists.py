class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

# --------------MIN - HEAP + SLIDING WINDOW ------------------
# Time  = O(N log k)
# Space = O(k)

        heap = []
        maxi = float('-inf')

        # take first element from every list
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            maxi = max(maxi, nums[i][0])

        ans = [heap[0][0], maxi]

        while True:

            mini, row, col = heapq.heappop(heap)

            # current range
            if maxi - mini < ans[1] - ans[0]:
                ans = [mini, maxi]

            # move to next element in the same list
            col += 1

            if col == len(nums[row]):
                break

            val = nums[row][col]
            heapq.heappush(heap, (val, row, col))

            maxi = max(maxi, val)

        return ans
        

