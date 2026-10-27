
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        hm = {}

        for ch in s1:
            hm[ch] = hm.get(ch, 0) + 1

        left = 0
        count = len(s1)

        for right in range(len(s2)):
            ch = s2[right]

            if ch in hm:
                if hm[ch] > 0:
                    count -= 1
                hm[ch] -= 1

            if right - left + 1 > len(s1):
                old = s2[left]

                if old in hm:
                    hm[old] += 1
                    if hm[old] > 0:
                        count += 1

                left += 1

            if count == 0:
                return True

        return False

