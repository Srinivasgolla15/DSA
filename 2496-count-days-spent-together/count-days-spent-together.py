class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        def convert(date):
            lengths = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

            days = int(date[3:])
            months = int(date[:2])

            total = days
            for i in range(months-1):
                total+=lengths[i]
            return total
        
        a1 = convert(arriveAlice)
        a2 = convert(leaveAlice)
        b1 = convert(arriveBob)
        b2 = convert(leaveBob)

        start = max(a1,b1)
        end = min(a2,b2)

        return max(0,end - start+1)


        