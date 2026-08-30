
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """


# ---------completely wrong but approach is correct 
        # arr = []
        # hm = {}

        # for ch in s:
        #     hm[ch] = hm.get(ch, 0) + 1

        # def dfs(i, curr, strr):

        #     if i == len(s):
        #         if sum(hm.values()) == len(s):
        #             arr.append(strr)
        #         return

        #     # Take current character
        #     hm[s[i]] = hm.get(s[i], 0) - 1
        #     curr.append(s[i])

        #     word = "".join(curr)

        #     if word in wordDict:

        #         if strr == "":
        #             dfs(i + 1, [], word)
        #         else:
        #             dfs(i + 1, [], strr + " " + word)

        #     # Continue building the current word
        #     dfs(i + 1, curr, strr)

        #     curr.pop()
        #     hm[s[i]] = hm.get(s[i], 0) + 1

        # dfs(0, [], "")

        # return arr


        arr = []

        def dfs(i, curr, strr):

            if i == len(s):
                if curr == []:
                    arr.append(strr)
                return

            curr.append(s[i])

            word = "".join(curr)

            if word in wordDict:

                if strr == "":
                    dfs(i + 1, [], word)
                else:
                    dfs(i + 1, [], strr + " " + word)

            dfs(i + 1, curr, strr)

            curr.pop()

        dfs(0, [], "")

        return arr
 
