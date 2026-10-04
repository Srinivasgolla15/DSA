class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        hm = {}
        left = 0
        maxfreq = 0
        ans = 0

        for right in range(len(s)):

            ch = s[right]

            if ch not in hm:
                hm[ch] = 0

            hm[ch] += 1

            maxfreq = max(maxfreq, hm[ch])

            window = right - left + 1
            replacements = window - maxfreq

            if replacements > k:
                hm[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# Time Complexity: O(N)
# Space Complexity: O(1)  # at most 26 uppercase English letters