class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap=[]
        freq = {}
        n=len(s)
        string=""
        prev =None 
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        queue = deque()
        for ch,count in freq.items():
            heapq.heappush(heap,(-count,ch))
        time = 0
        while heap or queue:
            while queue and queue[0][2]<=time:
                count,ch,available_time = queue.popleft()
                heapq.heappush(heap,(count,ch))

            if heap:
                count,ch = heapq.heappop(heap)
                if prev == ch:
                    return ""
                count+=1
                string+=ch
                prev = ch
            
                if count<0:
                    queue.append((count,ch,time+2))
                 
            time+=1
        return string




        