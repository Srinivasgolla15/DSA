class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
# ----------------------BACKTRACKING + BITS --------------
# Time Complexity: O(n * 2^n) worst case (loose upper bound)
# Space Complexity: O(2^n) for seen, res, and recursion stack
        # seen = set([0])
        # res = [0]
        # total = 1<<n
        # def dfs(num,count):
        #     if count == total:
        #         diff = num ^ res[0]
        #         return diff != 0 and (diff & (diff - 1)) == 0
            
        #     for i in range(n):
        #         nxt = num^(1<<i)

        #         if nxt not in seen:
        #             seen.add(nxt)
        #             res.append(nxt)
        #             if dfs(nxt,count+1):
        #                 return True
                
        #             seen.remove(nxt)
        #             res.pop()
        #     return False
        # dfs(0,1)
        # return res
                

                
# ---------------------BITS -------------------
        return [i^(i>>1) for i in range(1<<n)]



        