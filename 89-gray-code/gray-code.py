class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        seen = set([0])
        res = [0]
        total = 1<<n
        def dfs(num,count):
            if count == total:
                diff = num ^ res[0]
                return diff != 0 and (diff & (diff - 1)) == 0
            
            for i in range(n):
                nxt = num^(1<<i)

                if nxt not in seen:
                    seen.add(nxt)
                    res.append(nxt)
                    if dfs(nxt,count+1):
                        return True
                
                    seen.remove(nxt)
                    res.pop()
            return False
        dfs(0,1)
        return res
                

                


        
        dfs(0,n)



        