class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        low = max(weights)
        high = sum(weights)

        while low < high:

            days_needed = 1
            wei = 0
            mid = (low + high) // 2

            for w in weights:
                if wei + w <= mid:
                    wei += w
                else:
                    days_needed += 1
                    wei = w

            if days_needed <= days:
                high = mid
            else:
                low = mid + 1

        return low