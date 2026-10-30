class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hm = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        n = len(digits)
        res = []
        def dfs(arr,num):
            if len(arr)==n:
                res.append("".join(arr))
                return     
            for i in hm[digits[num]]:
                arr.append(i)
                dfs(arr,num+1)
                arr.pop()
        dfs([],0)
        return res
        