class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
# ---------wont work for all   
        # n = len(ratings)
        # chocos = [1] * n

        # def dfs(i):

        #     if i == n:
        #         return

        #     # Check left neighbor
        #     if i - 1 >= 0:
        #         if ratings[i - 1] < ratings[i]:
        #             chocos[i] = chocos[i - 1] + 1

        #     # Check right neighbor
        #     if i + 1 < n:
        #         if ratings[i + 1] < ratings[i]:
        #             chocos[i] = max(chocos[i], chocos[i + 1] + 1)

        #     dfs(i + 1)

        # dfs(0)

        # return sum(chocos)


# -------------DYNAMIC PROGRAMMING O(n) O(n)---------------------
        # n = len(ratings)

        # left = [1] * n
        # right = [1] * n

        # # DP from left
        # for i in range(1, n):
        #     if ratings[i] > ratings[i - 1]:
        #         left[i] = left[i - 1] + 1

        # # DP from right
        # for i in range(n - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]:
        #         right[i] = right[i + 1] + 1

        # # Each child must satisfy both directions
        # ans = 0

        # for i in range(n):
        #     ans += max(left[i], right[i])

        # return ans

# -----------------standard Two-Pass Greedy  O(n) O(n)------------
        # n = len(ratings)
        
        # candies = [1] * n

        # # Left to right
        # for i in range(1, n):
        #     if ratings[i] > ratings[i - 1]:
        #         candies[i] = candies[i - 1] + 1

        # # Right to left
        # for i in range(n - 2, -1, -1):
        #     if ratings[i] > ratings[i + 1]:
        #         candies[i] = max(candies[i], candies[i + 1] + 1)

        # return sum(candies)


#-------------SLOPE GREEDY O(n) O(1)----------------
        n = len(ratings)

        if n == 0:
            return 0

        total = 1
        i = 1

        while i < n:

            # Flat
            if ratings[i] == ratings[i - 1]:
                total += 1
                i += 1
                continue

            # Increasing
            up = 0
            while i < n and ratings[i] > ratings[i - 1]:
                up += 1
                total += up + 1
                i += 1

            # Decreasing
            down = 0
            while i < n and ratings[i] < ratings[i - 1]:
                down += 1
                total += down
                i += 1

            # Fix peak if descending side is longer
            if down > up:
                total += down - up

        return total