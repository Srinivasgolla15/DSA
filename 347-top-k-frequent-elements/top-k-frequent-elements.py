class Solution(object):
    def topKFrequent(self, nums, k):

# ---------------BRUTE FORCE  (time exceeds)--------------------------
 # Time Complexity:
        #   - Counting frequency using nested loops: O(n²)
        #   - Checking (count, num) not in freq: O(m) per iteration,
        #     where m is the number of unique elements (does not change
        #     the overall worst-case complexity).
        #   - Sorting the frequency list: O(m log m)
        #   - Collecting first k elements: O(k)
        #
        # Overall Time Complexity: O(n² + m log m)
        # Worst Case (m = n): O(n²)
        #
        # Space Complexity:
        #   - freq stores one entry per unique element: O(m)
        #   - res stores k elements: O(k)
        #
        # Overall Space Complexity: O(m + k)
        # Worst Case (m = n): O(n)

        # freq = []

        # # Count the frequency of every element
        # for num in nums:
        #     count = 0

        #     for value in nums:
        #         if value == num:
        #             count += 1

        #     # Avoid storing duplicates
        #     if (count, num) not in freq:
        #         freq.append((count, num))

        # # Sort by frequency in descending order
        # freq.sort(reverse=True)

        # res = []

        # # Take first k elements
        # for i in range(k):
        #     res.append(freq[i][1])

        # return res

# -------------Hash map with HEapq------------------------
 # Time Complexity:
        #   - Build frequency map: O(n)
        #   - Push each unique element into heap: O(m log k)
        #   - Extract k elements: O(k)
        #
        # Overall: O(n + m log k)
        # Worst Case (m = n): O(n log k)
        #
        # Space Complexity:
        #   - Frequency map: O(m)
        #   - Heap: O(k)
        #   - Result: O(k)
        #
        # Overall: O(m + k)
        # Worst Case: O(n)

        # Step 1: Count frequencies
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # # Step 2: Create a min heap
        # heap = []

        # # Step 3: Keep only the top k frequent elements
        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # # Step 4: Extract the numbers
        # res = []

        # while heap:
        #     res.append(heapq.heappop(heap)[1])

        # return res

# ---------------BUCKET SORT (optimal)----------------------------
 # Time Complexity:
        #   - Build frequency map: O(n)
        #   - Fill buckets: O(m)
        #   - Traverse buckets: O(n)
        #
        # Overall: O(n)
        #
        # Space Complexity:
        #   - Frequency map: O(m)
        #   - Buckets: O(n)
        #   - Result: O(k)
        #
        # Overall: O(n)

        # Step 1: Count frequencies
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # # Step 2: Create buckets
        # bucket = [[] for _ in range(len(nums) + 1)]

        # # Step 3: Place numbers into buckets
        # for num, count in freq.items():
        #     bucket[count].append(num)

        # res = []

        # # Step 4: Traverse buckets from highest frequency
        # for i in range(len(bucket) - 1, 0, -1):

        #     for num in bucket[i]:
        #         res.append(num)

        #         if len(res) == k:
        #             return res


        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for key,val in freq.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [key for val, key in heap]