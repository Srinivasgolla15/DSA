class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

# -----------------Brute Force (Insert → Sort → Merge)-----------
# Time: O(n log n)
# Space: O(n)
        # Step 1: Insert new interval
        # intervals.append(newInterval)

        # # Step 2: Sort by start time
        # intervals.sort(key=lambda x: x[0])

        # res = []

        # # Step 3: Merge intervals
        # for interval in intervals:

        #     if not res or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(res[-1][1], interval[1])

        # return res

# ----------------Linear Scan + Merge----------------
# Time: O(n)
# Space: O(n)
        res = []

        i = 0
        n = len(intervals)

        # Add intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add merged interval
        res.append(newInterval)

        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res







        