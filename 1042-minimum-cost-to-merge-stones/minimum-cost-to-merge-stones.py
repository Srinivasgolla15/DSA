class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """

# -----------------BRUTEFORCE  
# Each state explores up to \(n-k+1\) possible merges, and the recursion can have depth up to \(n-1\)
# space:\(O(n^2)\)
        # def dfs(arr):
        #     if len(arr) == 1:
        #         return 0

        #     if len(arr) < k:
        #         return float('inf')

        #     mini = float('inf')

        #     for i in range(len(arr) - k + 1):
        #         window = arr[i:i + k]
        #         cost = sum(window)

        #         newarr = arr[:i] + [cost] + arr[i + k:]

        #         remaining = dfs(newarr)

        #         if remaining != float('inf'):
        #             mini = min(mini, cost + remaining)

        #     return mini

        # if (len(stones) - 1) % (k - 1) != 0:
        #     return -1

        # ans = dfs(stones)
        # return ans if ans != float('inf') else -1


# ----------------memoization Exponential Exponential--------------------
        # memo = {}

        # def dfs(arr):
        #     if len(arr) == 1:
        #         return 0

        #     if len(arr) < k:
        #         return float('inf')

        #     key = tuple(arr)

        #     if key in memo:
        #         return memo[key]

        #     mini = float('inf')

        #     for i in range(len(arr) - k + 1):
        #         cost = sum(arr[i:i+k])
        #         newarr = arr[:i] + [cost] + arr[i+k:]

        #         remaining = dfs(newarr)
        #         mini = min(mini, cost + remaining)

        #     memo[key] = mini
        #     return mini

        # if (len(stones) - 1) % (k - 1) != 0:
        #     return -1

        # ans = dfs(stones)
        # return ans if ans != float('inf') else -1

# ---------------memoization \(O(n^3)\) \(O(n^2k)\) for memo states, plus recursion stack-------------
        # n = len(stones)

        # if (n - 1) % (k - 1) != 0:
        #     return -1

        # prefix = [0] * (n + 1)

        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + stones[i]

        # def rangeSum(left, right):
        #     return prefix[right + 1] - prefix[left]

        # memo = {}

        # def dfs(left, right, piles):
        #     if right - left + 1 < piles:
        #         return float('inf')

        #     if left == right:
        #         if piles == 1:
        #             return 0
        #         return float('inf')

        #     key = (left, right, piles)

        #     if key in memo:
        #         return memo[key]

        #     if piles == 1:
        #         cost = dfs(left, right, k)

        #         if cost != float('inf'):
        #             cost += rangeSum(left, right)

        #         memo[key] = cost
        #         return cost

        #     mini = float('inf')

        #     mid = left

        #     while mid < right:
        #         left_cost = dfs(left, mid, 1)
        #         right_cost = dfs(mid + 1, right, piles - 1)

        #         mini = min(mini, left_cost + right_cost)

        #         mid += k - 1

        #     memo[key] = mini
        #     return mini

        # return dfs(0, n - 1, 1)

# -------------Bottom-up 2D interval DP    \(O(n^3)\) \(O(n^3)\)	\(O(n^2)\)-------------


        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                dp[left][right] = float('inf')

                for mid in range(left, right, k - 1):
                    cost = dp[left][mid] + dp[mid + 1][right]
                    dp[left][right] = min(dp[left][right], cost)

                if (length - 1) % (k - 1) == 0:
                    dp[left][right] += prefix[right + 1] - prefix[left]

        return dp[0][n - 1]       