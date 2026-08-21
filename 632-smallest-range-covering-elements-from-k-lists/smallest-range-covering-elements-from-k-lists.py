class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []

        # Put the first element of every list into the heap
        max_val = float('-inf')

        for i in range(len(nums)):
            val = nums[i][0]

            heapq.heappush(heap, (val, i, 0))

            max_val = max(max_val, val)

        # Initial best range
        best_left = heap[0][0]
        best_right = max_val

        while True:

            # Get the smallest current element
            min_val, list_idx, element_idx = heapq.heappop(heap)

            # Current range covers one element from every list
            if max_val - min_val < best_right - best_left:
                best_left = min_val
                best_right = max_val

            # Move to the next element in the same list
            next_idx = element_idx + 1

            # If this list has no more elements,
            # we can no longer have one element from every list
            if next_idx == len(nums[list_idx]):
                break

            next_val = nums[list_idx][next_idx]

            # Put next element from this list into heap
            heapq.heappush(
                heap,
                (next_val, list_idx, next_idx)
            )

            # Update maximum
            max_val = max(max_val, next_val)

        return [best_left, best_right]
        

