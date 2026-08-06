class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):


# -----------------BACKTRACKING (BRUTEFORCE)------------------


        # # Convert list to set for O(1) lookup
        # wordSet = set(wordList)

        # # If endWord doesn't exist, no solution
        # if endWord not in wordSet:
        #     return []

        # # Stores all possible paths
        # allPaths = []

        # # Current path starts with beginWord
        # path = [beginWord]

        # # Prevent cycles (hit -> hot -> hit -> ...)
        # visited = set([beginWord])

        # # ---------------- DFS / Backtracking ----------------
        # def dfs(word):

        #     # Base Case
        #     if word == endWord:
        #         # Store a COPY of the current path
        #         allPaths.append(path[:])
        #         return

        #     # Try changing every character
        #     for i in range(len(word)):

        #         # Try all 26 letters
        #         for ch in "abcdefghijklmnopqrstuvwxyz":

        #             # Skip if same character
        #             if ch == word[i]:
        #                 continue

        #             # Generate new word
        #             newWord = word[:i] + ch + word[i+1:]

        #             # Only continue if valid
        #             if newWord in wordSet and newWord not in visited:

        #                 # Choose
        #                 visited.add(newWord)
        #                 path.append(newWord)

        #                 # Explore
        #                 dfs(newWord)

        #                 # Undo choice (Backtrack)
        #                 path.pop()
        #                 visited.remove(newWord)

        # dfs(beginWord)

        # # No path found
        # if not allPaths:
        #     return []

        # # Find shortest length
        # shortest = min(len(p) for p in allPaths)

        # # Return only shortest paths
        # ans = []

        # for p in allPaths:
        #     if len(p) == shortest:
        #         ans.append(p)

        # return ans

# Time Complexity:
# O((26 × L) × Number of possible paths)
# ≈ Exponential in the worst case.

# Space Complexity:
# O(N) auxiliary
# or O(N + K × M) including the returned paths.



# ---------------- BFS STORING COMPLETE PATHS ----------------
# Time Complexity: O(2^N * L)
# N = Number of words
# L = Length of each word
# Every stored path is expanded by generating all possible one-letter transformations.

# Space Complexity: O(2^N * N)
# Queue stores complete paths, each of length up to N.


        # Convert list to set for O(1) lookup
        # wordSet = set(wordList)

        # # If destination doesn't exist
        # if endWord not in wordSet:
        #     return []

        # # Queue stores COMPLETE PATHS
        # queue = deque([[beginWord]])

        # # Stores words used in current BFS level
        # usedOnLevel = set([beginWord])

        # # Current BFS level
        # level = 1

        # # Stores final answer
        # ans = []

        # while queue:

        #     # Remove one complete path
        #     path = queue.popleft()

        #     # If we entered next BFS level
        #     if len(path) > level:

        #         level += 1

        #         # Remove all words used in previous level
        #         for word in usedOnLevel:
        #             # wordSet.remove(word)----> creates errror
        #             wordSet.discard(word)

        #         # Reset for next level
        #         usedOnLevel = set()

        #     # Current word is last word of path
        #     word = path[-1]

        #     # Destination reached
        #     if word == endWord:

        #         # First shortest path
        #         if len(ans) == 0:
        #             ans.append(path)

        #         # Another shortest path
        #         elif len(path) == len(ans[0]):
        #             ans.append(path)

        #         continue

        #     # Try every character position
        #     for i in range(len(word)):

        #         # Try every alphabet
        #         for ch in "abcdefghijklmnopqrstuvwxyz":

        #             # Skip same character
        #             if ch == word[i]:
        #                 continue

        #             # Generate new word
        #             newWord = word[:i] + ch + word[i+1:]

        #             # Valid transformation
        #             if newWord in wordSet:

        #                 # Copy current path
        #                 newPath = path[:]

        #                 # Add new word
        #                 newPath.append(newWord)

        #                 # Push into queue
        #                 queue.append(newPath)

        #                 # Remember this word was used
        #                 usedOnLevel.add(newWord)

        # return ans


# ---------------- BFS + Distance Map + DFS ----------------


# Time Complexity: O(N * L * 26 + K * M)
# N = Number of words
# L = Length of each word
# K = Number of shortest paths
# M = Length of each path
#
# BFS computes the shortest distance of every reachable word.
# DFS reconstructs only the shortest paths.

# Space Complexity: O(N + K * M)
# O(N) for distance map and queue.
# O(K * M) for storing the final answers.

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Distance of each word from beginWord
        distance = {}

        queue = deque([beginWord])

        distance[beginWord] = 1

        wordSet.remove(beginWord) if beginWord in wordSet else None

        # ---------------- BFS ----------------
        while queue:

            word = queue.popleft()

            steps = distance[word]

            if word == endWord:
                break

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == word[i]:
                        continue

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:

                        queue.append(newWord)

                        wordSet.remove(newWord)

                        distance[newWord] = steps + 1

        ans = []

        path = [endWord]

        # ---------------- DFS ----------------
        def dfs(word):

            if word == beginWord:

                ans.append(path[::-1])

                return

            steps = distance[word]

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == word[i]:
                        continue

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in distance and distance[newWord] + 1 == steps:

                        path.append(newWord)

                        dfs(newWord)

                        path.pop()

        if endWord in distance:
            dfs(endWord)

        return ans