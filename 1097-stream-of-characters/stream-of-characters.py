# =================TLE=========================
# class TrieNode(object):
#     def __init__(self):
#         self.children = {}
#         self.end = False

# # Time: O(N)
# # Space: O(N)  -> Trie


# class StreamChecker(object):

#     def __init__(self, words):
#         """
#         :type words: List[str]
#         """

#         self.root = TrieNode()
#         self.stream = ""

#         # Build Trie using reversed words
#         for word in words:

#             node = self.root

#             for j in range(len(word) - 1, -1, -1):

#                 ch = word[j]

#                 if ch not in node.children:
#                     node.children[ch] = TrieNode()

#                 node = node.children[ch]

#             node.end = True


#     def query(self, letter):
#         """
#         :type letter: str
#         :rtype: bool
#         """
# # Time: O(K)

#         self.stream += letter

#         node = self.root

#         # Start from the latest character
#         for j in range(len(self.stream) - 1, -1, -1):

#             ch = self.stream[j]

#             if ch not in node.children:
#                 return False

#             node = node.children[ch]

#             if node.end:
#                 return True

#         return False
# Overall:
# Time: O(N + Q*K)
# Space: O(N + Q)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """

        self.root = TrieNode()
        self.stream = ""
        self.maxLen = 0

        # Build reversed Trie
        for word in words:

            self.maxLen = max(self.maxLen, len(word))

            node = self.root

            for j in range(len(word) - 1, -1, -1):

                ch = word[j]

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.end = True


    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """

        # Add new character
        self.stream += letter

        # Keep only the useful part of the stream
        if len(self.stream) > self.maxLen:
            self.stream = self.stream[-self.maxLen:]

        node = self.root

        # Traverse stream backwards
        for j in range(len(self.stream) - 1, -1, -1):

            ch = self.stream[j]

            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.end:
                return True

        return False


# Time:
# __init__: O(N)
# query: O(K)
# Overall: O(N + Q*K)
#
# Space:
# Trie: O(N)
# Stream: O(K)
# Overall: O(N + K)
#
# N = total characters in all words
# Q = number of queries
# K = maximum word length
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)