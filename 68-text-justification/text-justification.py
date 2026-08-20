class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

#----------------------Greedy Line Packing + Space Distribution-------------


        res = []
        curr = []
        curr_len = 0

        for word in words:

            # Check whether this word can fit
            if curr_len + len(word) + len(curr) <= maxWidth:
                curr.append(word)
                curr_len += len(word)

            else:
                # Words in current line
                leng = len(curr)

                # Number of gaps
                no = leng - 1

                # Spaces that need to be distributed
                remaining = maxWidth - curr_len

                # Single-word case
                if no == 0:
                    line = curr[0] + " " * remaining

                else:
                    # Minimum spaces per gap
                    space = remaining // no

                    # Leftover spaces
                    extragap = remaining % no

                    line = ""

                    for i, w in enumerate(curr):
                        line += w

                        if i < no:
                            gap = space

                            if i < extragap:
                                gap += 1

                            line += " " * gap

                res.append(line)

                # Start next line
                curr = [word]
                curr_len = len(word)

        # Last line
        line = " ".join(curr)
        line += " " * (maxWidth - len(line))
        res.append(line)

        return res

 # Time Complexity:
        # O(N + L * maxWidth)
        # N = total number of characters in all words
        # L = number of output lines
        #
# Space Complexity:
        # O(maxWidth) auxiliary space
        # O(L * maxWidth) including the output `res`