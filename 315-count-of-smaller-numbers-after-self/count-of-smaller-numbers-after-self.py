class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
# ------------------BruteForce O(n2) O(n) TLE----------------
        # res = []
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             count+=1
        #     res.append(count)
        # return res

# ----------Sorted list + Binary Search + insertion--------------

# Time : Binary search: O(log n)
#     Insertion:     O(n)
#     Total:         O(n²)
# Space : O(n)

        # n = len(nums)
        # res = [0] * n

        # # Stores elements to the right in sorted order
        # sorted_list = []

        # # Traverse from right to left
        # for i in range(n - 1, -1, -1):

        #     # Binary search for the first position
        #     # where nums[i] can be inserted
        #     left = 0
        #     right = len(sorted_list)

        #     while left < right:
        #         mid = (left + right) // 2

        #         if sorted_list[mid] < nums[i]:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     # 'left' = number of elements smaller than nums[i]
        #     res[i] = left

        #     # Insert nums[i] while keeping sorted_list sorted
        #     sorted_list.insert(left, nums[i])

        # return res


# ----------sortedList just for learning ------------------
        res = []
        sorted_nums = SortedList(nums)
        for e in nums:
            idx = sorted_nums.index(e)
            res.append(idx)
            sorted_nums.remove(e)
        return res
        