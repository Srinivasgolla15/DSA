class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
# ----------Brute Force + Palindrome Check (TLE)---------------
    # Time: O(n^2 * k)
        #   n^2 -> try every pair of words
        #   k   -> palindrome checking / length of combined string
        #
        # More precisely, if each word has maximum length k,
        # creating/checking words[i] + words[j] costs O(k).
        #
    # Space: O(k)
        #   temporary combined string + reversed string
        #   Output space O(ans) is not counted.
        # ans = []
        # def ispal(string):
        #     if string == string[::-1]:
        #         return True
        #     else:
        #         False
        # for i in range(len(words)):
        #     for j in range(len(words)):
        #         if j==i:
        #             continue
        #         string = words[i] + words[j]
        #         if ispal(string):
        #             ans.append([i,j])
        # return ans


        hm = {}
        ans = set()

        # Store word -> index
        for i, word in enumerate(words):
            hm[word] = i

        for i, word in enumerate(words):

            for j in range(len(word) + 1):

                left = word[:j]
                right = word[j:]

                # Case 1: left is palindrome
                if left == left[::-1]:
                    rev = right[::-1]

                    if rev in hm and hm[rev] != i:
                        ans.add((hm[rev], i))

                # Case 2: right is palindrome
                if right == right[::-1]:
                    rev = left[::-1]

                    if rev in hm and hm[rev] != i:
                        ans.add((i, hm[rev]))

        return [list(pair) for pair in ans]