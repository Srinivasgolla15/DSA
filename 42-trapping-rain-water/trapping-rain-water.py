class Solution(object):

    def trap(self, height):

        # two-poiters approach (optimal)

        # Time Complexity : O(n)
        # Space Complexity: O(1)

        # left = 0
        # right = len(height) - 1

        # leftMax = 0
        # rightMax = 0

        # water = 0

        # while left < right:

        #     # process smaller side
        #     if height[left] < height[right]:

        #         # update left boundary
        #         if height[left] >= leftMax:
        #             leftMax = height[left]

        #         # trapped water
        #         else:
        #             water += leftMax - height[left]

        #         left += 1

        #     else:

        #         # update right boundary
        #         if height[right] >= rightMax:
        #             rightMax = height[right]

        #         # trapped water
        #         else:
        #             water += rightMax - height[right]

        #         right -= 1

        # return water

        # too difficult Monotonic Stack
        # stack = []
        # total = 0

        # for i in range(len(height)):

        #     while stack and height[i] > height[stack[-1]]:

        #         # valley / bottom
        #         bottom = stack.pop()

        #         # no left wall exists
        #         if not stack:
        #             break

        #         # left wall
        #         left = stack[-1]

        #         # distance between walls
        #         width = i - left - 1

        #         # water height
        #         bounded_height = min(height[left], height[i]) - height[bottom]

        #         # trapped water
        #         total += width * bounded_height

        #     stack.append(i)

        # return total


        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        # First pass: maximum height from the left
        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Second pass: maximum height from the right
        right_max[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate trapped water
        water = 0

        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water
