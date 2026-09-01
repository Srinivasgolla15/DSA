class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

# ---------------linear search -------------------
# Time: O(n * max(piles))
#       For each speed k, we scan all n piles.
#       In worst case, k goes from 1 to max(piles).

# Space: O(max(piles))
#        Due to recursive calls dfs(k + 1).

        # if h==len(piles):
        #     return max(piles)
        
        # def dfs(k):

        #     hours = 0

        #     for pile in piles:
        #         hours += (pile + k - 1) // k

        #     if hours <= h:
        #         return k

        #     return dfs(k + 1)

        # return dfs(1)
                    

# Approach: Binary Search on Answer
# Time: O(n * log(max(piles)))
# Space: O(1)
        low = 1
        high = max(piles)

        while low <= high:

            k = (low + high) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                # k works
                # But maybe a smaller speed also works
                high = k - 1

            else:
                # k is too slow
                # Need a bigger speed
                low = k + 1

        return low

        










