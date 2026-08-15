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


        # res = []
        # sorted_nums = SortedList(nums)
        # for e in nums:
        #     idx = sorted_nums.index(e)
        #     res.append(idx)
        #     sorted_nums.remove(e)
        # return res


        n = len(nums)

        # Answer for each original index
        res = [0] * n

        # (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):

            # Base case
            if left >= right:
                return

            mid = (left + right) // 2

            # Sort left half
            merge_sort(left, mid)

            # Sort right half
            merge_sort(mid + 1, right)

            # Merge
            temp = []

            i = left
            j = mid + 1

            # Number of elements taken from
            # the right half that are smaller
            right_count = 0

            while i <= mid and j <= right:

                if arr[j][0] < arr[i][0]:

                    # Right element is smaller
                    right_count += 1

                    temp.append(arr[j])
                    j += 1

                else:

                    # All previously taken right elements
                    # are smaller than arr[i]
                    res[arr[i][1]] += right_count

                    temp.append(arr[i])
                    i += 1

            # Left elements remaining
            while i <= mid:

                res[arr[i][1]] += right_count

                temp.append(arr[i])
                i += 1

            # Right elements remaining
            while j <= right:

                temp.append(arr[j])
                j += 1

            # Put sorted elements back into arr
            for k in range(len(temp)):
                arr[left + k] = temp[k]

        merge_sort(0, n - 1)

        return res
        