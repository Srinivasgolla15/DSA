class Solution(object):
    def groupAnagrams(self, strs):


# ------------------BRUTE FORCE O(n2×k) O(n×k) (wrong for some)------------------

        # res = []
        # visited = set()

        # for i in range(len(strs)):

        #     if strs[i] in visited:
        #         continue

        #     s = strs[i]

        #     hm = {}

        #     for ch in s:
        #         hm[ch] = hm.get(ch,0)+1

        #     arr = [s]

        #     for j in range(i+1,len(strs)):

        #         ns = strs[j]

        #         if ns in visited:
        #             continue

        #         temp = {}

        #         for ch in ns:
        #             temp[ch] = temp.get(ch,0)+1

        #         if temp == hm:
        #             arr.append(ns)
        #             visited.add(ns)

        #     visited.add(s)
        #     res.append(arr)

        # return res


# -------------Sorting + HashMap O(n×klogk) O(nk) --------------

        hm = {}

        for s in strs:

            key = ''.join(sorted(s))

            if key not in hm:
                hm[key] = [s]
            else:
                hm[key].append(s)

        return list(hm.values())



# -------------Character Count as Hash Key  O(n*k) O(n*k)---------------

        # hm = {}

        # for s in strs:

        #     count = [0]*26

        #     for ch in s:
        #         count[ord(ch)-ord('a')] += 1


        #     key = tuple(count)


        #     if key not in hm:
        #         hm[key] = [s]

        #     else:
        #         hm[key].append(s)


        # return list(hm.values())