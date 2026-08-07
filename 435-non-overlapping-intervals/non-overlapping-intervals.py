class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

# ---------------BRUTE FORCE ------------------
# Time = O(2ⁿ)
# space = O(n)
        # n = len(intervals)

        # def dfs(i, prev_end):
        #     # No intervals left
        #     if i == n:
        #         return 0

        #     # Choice 1: delete current interval
        #     delete = 1 + dfs(i + 1, prev_end)

        #     # Choice 2: keep current interval
        #     keep = float("inf")

        #     if intervals[i][0] >= prev_end:
        #         keep = dfs(i + 1, intervals[i][1])

        #     return min(delete, keep)

        # return dfs(0, float("-inf"))
            

# ---------------SORTING + GREEDY----------------
        intervals.sort(key = lambda x:x[1])
        count = 0
        prev = float("-inf")
        for arr in intervals:
            start = arr[0]
            end = arr[1]
            if start < prev:
                count+=1
            else:
                prev = end
        return count