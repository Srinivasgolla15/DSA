class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
     
        result = []
        i = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            # count consecutive chars
            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1

            # add character
            result.append(ch)

            # add count if > 1
            if count > 1:
                for digit in str(count):
                    result.append(digit)

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
         