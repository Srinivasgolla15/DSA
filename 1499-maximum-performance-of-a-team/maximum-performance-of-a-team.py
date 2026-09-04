class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """

# Greedy + Sorting + Min Heap
        # engineers = sorted(zip(efficiency, speed))

        # maxheap = []
        # maxi = 0
        # speed_sum = 0

        # for i in range(n - 1, -1, -1):

        #     e, s = engineers[i]

        #     heapq.heappush(maxheap, s)
        #     speed_sum += s

        #     if len(maxheap) > k:
        #         speed_sum -= heapq.heappop(maxheap)

        #     performance = speed_sum * e
        #     maxi = max(maxi, performance)

        # return maxi % (10**9 + 7)

# same but reversee sorting made easy code 

        # Keep efficiency and speed of each engineer together
        # Sort by efficiency in descending order
        engineers = sorted(zip(efficiency, speed), reverse=True)

        minheap = []
        speed_sum = 0
        maxi = 0

        for e, s in engineers:

            # Add current engineer's speed
            heapq.heappush(minheap, s)
            speed_sum += s

            # We can select at most k engineers
            # Remove the smallest speed if we have more than k
            if len(minheap) > k:
                speed_sum -= heapq.heappop(minheap)

            # Since efficiency is sorted descending,
            # current e is the minimum efficiency of this team
            performance = speed_sum * e

            maxi = max(maxi, performance)

        return maxi % (10**9 + 7)


# Time: O(n log n + n log k) = O(n log n)
# Space: O(n + k) = O(n)

        