class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

# --------------STANDARD BFS ------------------
# Time Complexity: O(N * L^2)
# N = number of words
# L = length of each word
# For each visited word, we try 26 substitutions at each position
# and build a new string of length L.

# Space Complexity: O(N)
# wordSet + visited + queue

        # wordSet = set(wordList)
        
        # # Step 1: If endWord not present → return 0
        # if endWord not in wordSet:
        #     return 0
        
        # # Step 2: BFS setup
        # queue = deque()
        # queue.append((beginWord, 1))  # (word, level)
        
        # visited = set()
        # visited.add(beginWord)
        
        # # Step 3: BFS traversal
        # while queue:
        #     word, level = queue.popleft()
            
        #     # Step 4: If reached endWord
        #     if word == endWord:
        #         return level
            
        #     # Step 5: Try all one-letter transformations
        #     for i in range(len(word)):
        #         for ch in "abcdefghijklmnopqrstuvwxyz":
        #             new_word = word[:i] + ch + word[i+1:]
                    
        #             if new_word in wordSet and new_word not in visited:
        #                 visited.add(new_word)
        #                 queue.append((new_word, level + 1))
        
        # return 0


# ------------BIDIRECTIONAL BFS----------------
# O(NL²) (better practical runtime)
# O(N) 

        # Convert list to set for O(1) lookup
        # words = set(wordList)

        # # If endWord doesn't exist, answer is impossible
        # if endWord not in words:
        #     return 0

        # # Two queues
        # beginQueue = deque([beginWord])
        # endQueue = deque([endWord])

        # # Store visited + distance
        # fromBegin = {beginWord: 1}
        # fromEnd = {endWord: 1}

        # alphabets = "abcdefghijklmnopqrstuvwxyz"

        # while beginQueue and endQueue:

        #     # Always expand the smaller side
        #     if len(beginQueue) > len(endQueue):
        #         beginQueue, endQueue = endQueue, beginQueue
        #         fromBegin, fromEnd = fromEnd, fromBegin

        #     # Process one level
        #     for _ in range(len(beginQueue)):

        #         word = beginQueue.popleft()
        #         level = fromBegin[word]

        #         # Change every character
        #         for i in range(len(word)):

        #             left = word[:i]
        #             right = word[i+1:]

        #             for ch in alphabets:

        #                 newWord = left + ch + right

        #                 # Searches meet
        #                 if newWord in fromEnd:
        #                     return level + fromEnd[newWord]

        #                 # Valid unseen word
        #                 if newWord in words and newWord not in fromBegin:

        #                     fromBegin[newWord] = level + 1
        #                     beginQueue.append(newWord)

        # return 0

# ---------------BFS+ WILDCARD PATTERN--------------------
# O(NL²)  
# O(N) 
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # Pattern -> words map
        patternMap = defaultdict(list)

        # Build wildcard patterns
        for word in wordList:

            for i in range(L):

                pattern = word[:i] + "*" + word[i+1:]

                patternMap[pattern].append(word)

        # BFS
        queue = deque([(beginWord, 1)])

        visited = set()
        visited.add(beginWord)

        while queue:

            word, level = queue.popleft()

            # Reached target
            if word == endWord:
                return level

            # Generate patterns
            for i in range(L):

                pattern = word[:i] + "*" + word[i+1:]

                # Visit all neighbors
                for neighbor in patternMap[pattern]:

                    if neighbor not in visited:

                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                # Optimization:
                # clear list after use
                patternMap[pattern] = []

        return 0

