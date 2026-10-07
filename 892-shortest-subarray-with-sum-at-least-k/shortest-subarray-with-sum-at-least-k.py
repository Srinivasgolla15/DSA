class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
# -------------BRUTE FORCE -------------------------
        # n = len(nums)

        # # Build prefix sum
        # prefix = [0] * (n + 1)

        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # ans = n + 1

        # for left in range(n):
        #     for right in range(left + 1, n + 1):

        #         # Sum of nums[left:right]
        #         total = prefix[right] - prefix[left]

        #         if total >= k:
        #             ans = min(ans, right - left)

        # if ans == n + 1:
        #     return -1

        # return ans


# Time Complexity: O(N^2)
# Space Complexity: O(N)



         
        n = len(nums)

        # Build prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = n + 1

        for i in range(n + 1):

            # Check if current prefix can form a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                
                # Valid subarray found
                ans = min(ans, i - dq.popleft())

            # Remove useless prefix indices
            # New prefix is smaller and index is later,
            # so the old index can never be better.
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            # Add current prefix index
            dq.append(i)

        if ans == n + 1:
            return -1

        return ans


# Time Complexity: O(N)
# Space Complexity: O(N)
        
        