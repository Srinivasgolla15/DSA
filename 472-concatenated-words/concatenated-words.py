class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
# ---------------DP memoized split code ---------------------

# Let:
# n = number of words
# L = maximum length of a word
#
# For one word:
# There are O(L) possible starting positions.
# For each position, we try O(L) possible ending positions.
#
# Time for one word: O(L²)
#
# Checking "part in wordSet" is O(L) in Python in the worst case
# because 'part' is a substring of length up to L.
#
# Therefore, worst-case time for one word: O(L³)
#
# For all n words:
# Time: O(n * L³)
#
# Space:
# wordSet = O(n)
# memo = O(L²) because key = (start, count)
# Recursion stack = O(L)
#
# Total Space: O(n + L²)

        # wordSet = set(words)
        # memo = {}

        # def canForm(word, start, count):

        #     # We reached the end
        #     if start == len(word):
        #         return count >= 2

        #     # Already solved this state
        #     key = (start, count)

        #     if key in memo:
        #         return memo[key]

        #     # Try every possible next word
        #     for end in range(start + 1, len(word) + 1):

        #         part = word[start:end]

        #         if part in wordSet:
        #             if canForm(word, end, count + 1):
        #                 memo[key] = True
        #                 return True

        #     memo[key] = False
        #     return False

        # ans = []

        # for word in words:

        #     # Don't let the word use itself as one piece
        #     wordSet.remove(word)

        #     memo = {}

        #     if canForm(word, 0, 0):
        #         ans.append(word)

        #     wordSet.add(word)

        # return ans



        wordSet = set(words)
        ans = []

        def canForm(word):
            n = len(word)

            # dp[i] = can we form word[0:i]
            dp = [False] * (n + 1)
            dp[0] = True

            # Try every starting position
            for i in range(n):

                if not dp[i]:
                    continue

                # Try every possible next word
                for j in range(i + 1, n + 1):

                    part = word[i:j]

                    if part in wordSet:
                        dp[j] = True

            return dp[n]

        for word in words:

            # Temporarily remove the word itself
            # so it cannot use itself as the only word.
            wordSet.remove(word)

            if canForm(word):
                ans.append(word)

            wordSet.add(word)

        return ans