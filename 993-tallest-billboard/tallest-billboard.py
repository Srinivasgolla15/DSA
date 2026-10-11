class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """

# ------------  recursionO(3^n) O(n) -----------
        # if not rods:
        #     return 0
        # maxi = [0]
        # memo = {}
        # n = len(rods)
        # def dfs(idx,suma,sumb):
        #     diff = abs(suma-sumb)
        #     if idx == n:
        #         if suma == sumb:
        #             maxi[0] = max(maxi[0], suma)
        #         return
        #     rod = rods[idx]
        #     takea = dfs(idx+1,suma+rod,sumb)
        #     takeb = dfs(idx+1,suma,sumb+rod)
        #     skip = dfs(idx+1,suma,sumb)
        # dfs(0,0,0)
        # return maxi[0]

# ----------------memoization TLE -------------
# Time Complexity: O(n * S^2)
# Space Complexity: O(n * S^2) for memoization
# Recursion Stack: O(n)
# S = sum(rods)

        # if not rods:
        #     return 0

        # n = len(rods)
        # memo = {}

        # def dfs(idx, suma, sumb):
        #     if idx == n:
        #         if suma == sumb:
        #             return suma
        #         return 0

        #     key = (idx, suma, sumb)

        #     if key in memo:
        #         return memo[key]

        #     rod = rods[idx]

        #     takea = dfs(idx + 1, suma + rod, sumb)
        #     takeb = dfs(idx + 1, suma, sumb + rod)
        #     skip = dfs(idx + 1, suma, sumb)

        #     memo[key] = max(takea, takeb, skip)
        #     return memo[key]

        # return dfs(0, 0, 0)

# -------------------Memoization  --------------------------
        n = len(rods)
        memo = {}

        def dfs(idx, diff):
            if idx == n:
                if diff == 0:
                    return 0
                return float('-inf')

            key = (idx, diff)

            if key in memo:
                return memo[key]

            rod = rods[idx]

            # Put the rod on support A
            takea = dfs(idx + 1, diff + rod)

            # Put the rod on support B
            takeb = min(diff, rod) +dfs(idx + 1, abs(diff - rod))

            # Skip the rod
            skip = dfs(idx + 1, diff)

            memo[key] = max(takea, takeb, skip)
            return memo[key]

        return dfs(0, 0)


# Time Complexity: O(n * S), where S = sum(rods)
# Space Complexity: O(n * S) for memoization
# Recursion Stack: O(n)
            
            

         
     
