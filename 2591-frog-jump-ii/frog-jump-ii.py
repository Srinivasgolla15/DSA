
class Solution(object):
    def maxJump(self, stones):
        n = len(stones)

        if n == 2:
            return stones[1] - stones[0]

        answer = stones[1] - stones[0]

        for i in range(2, n):
            jump = stones[i] - stones[i - 2]
            answer = max(answer, jump)

        return answer
