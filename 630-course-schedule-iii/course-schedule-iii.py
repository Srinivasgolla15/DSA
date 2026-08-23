class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
# ---------------Greedy + max heap to remove long dureation course --------
        courses.sort(key =  lambda x:x[1])
        total = 0
        heap = []
        for course in courses:
            total+=course[0]
            heapq.heappush(heap,-course[0])
             
            if total>course[1]:
                total+=heapq.heappop(heap)

        return len(heap)

            
        