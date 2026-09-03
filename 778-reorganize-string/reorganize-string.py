class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

# -----------------heap + cooldown queue---------------
 # Approach: Greedy + Max Heap + Cooldown Queue
        #
        # Time: O(N log K)
        # K = number of distinct characters
        #
        # Space: O(N + K)
        # heap=[]
        # freq = {}
        # n=len(s)
        # string=""
        # prev =None 
        # for ch in s:
        #     freq[ch]=freq.get(ch,0)+1
        # queue = deque()
        # for ch,count in freq.items():
        #     heapq.heappush(heap,(-count,ch))
        # time = 0
        # while heap or queue:
        #     while queue and queue[0][2]<=time:
        #         count,ch,available_time = queue.popleft()
        #         heapq.heappush(heap,(count,ch))

        #     if heap:
        #         count,ch = heapq.heappop(heap)
        #         if prev == ch:
        #             return ""
        #         count+=1
        #         string+=ch
        #         prev = ch
            
        #         if count<0:
        #             queue.append((count,ch,time+2))
                 
        #     time+=1
        # return string



# ----------ABOVE APPROACH BUT ENHANCED ----------------
        # counts = Counter(s)
        # heap = [(-count,char) for char,count in counts.items()]
        # heapq.heapify(heap)

        # prev_char,prev_count='',0
        # res= []
        # while heap:
        #     count,char = heapq.heappop(heap)
        #     res.append(char)
        #     if prev_count<0:
        #         heapq.heappush(heap,(prev_count,prev_char))
        #     count+=1
        #     prev_count,prev_char=count,char
        # result = "".join(res)
        # return result if len(result)==len(s) else ""



        freq = Counter(s)
        n = len(s)

        # Find the most frequent character
        max_char = max(freq, key=freq.get)
        max_count = freq[max_char]

        # Impossible if the most frequent character
        # appears more than half of the positions
        if max_count > (n + 1) // 2:
            return ""

        res = [""] * n

        # Start with even positions
        idx = 0

        # Place the most frequent character first
        while freq[max_char] > 0:
            res[idx] = max_char
            freq[max_char] -= 1

            idx += 2

        # Place all remaining characters
        for char, count in freq.items():

            while count > 0:

                # Even positions are finished
                # Switch to odd positions
                if idx >= n:
                    idx = 1

                res[idx] = char
                count -= 1

                idx += 2

        return "".join(res)


# Time: O(N)
# Space: O(N + K) = O(N)
#
# N = length of s
# K = number of distinct characters
#
# Counter -> O(N)
# Finding max -> O(K)
# Filling result -> O(N)
#
# Total -> O(N)


# -------------Optimized greedy ---------------
        # freq = [0] * 26
        # for char in s:
        #     freq[ord(char)-ord("a")]+=1
        # max_idx = freq.index(max(freq))
        # max_freq = freq[max_idx]
        # if max_freq >(len(s)+1) //2:
        #     return ""
        # res = [''] * len(s)
        # idx = 0
        # max_char = chr(max_idx+ord("a"))
        # while freq[max_idx]>0:
        #     res[idx] = max_char
        #     idx +=2
        #     freq[max_idx] -=1
        # for i in range(26):
        #     while freq[i] >0:
        #         if idx >= len(s):
        #             idx = 1
        #         res[idx] = chr(i+ord("a"))
        #         idx+=2
        #         freq[i] -=1
        # return "".join(res)