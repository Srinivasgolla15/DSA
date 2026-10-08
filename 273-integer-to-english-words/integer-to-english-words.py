class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        hm = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def dfs(num):

            # 0 - 19
            if num < 20:
                return hm[num]

            # 20 - 99
            elif num < 100:
                tens = (num // 10) * 10
                ones = num % 10

                if ones == 0:
                    return hm[tens]

                return hm[tens] + " " + hm[ones]

            # 100 - 999
            elif num < 1000:
                hundred = num // 100
                remaining = num % 100

                if remaining == 0:
                    return hm[hundred] + " Hundred"

                return hm[hundred] + " Hundred " + dfs(remaining)

            # 1000 - ...
            elif num < 1000000:
                thousand = num // 1000
                remaining = num % 1000

                if remaining == 0:
                    return dfs(thousand) + " Thousand"

                return dfs(thousand) + " Thousand " + dfs(remaining)

            # Million
            elif num < 1000000000:
                million = num // 1000000
                remaining = num % 1000000

                if remaining == 0:
                    return dfs(million) + " Million"

                return dfs(million) + " Million " + dfs(remaining)

            # Billion
            else:
                billion = num // 1000000000
                remaining = num % 1000000000

                if remaining == 0:
                    return dfs(billion) + " Billion"

                return dfs(billion) + " Billion " + dfs(remaining)

        return dfs(num)