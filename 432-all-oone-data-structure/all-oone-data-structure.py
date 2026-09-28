class AllOne(object):

    def __init__(self):
        self.hm = {}
        self.freq = {}

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        old = self.hm.get(key,0)
        if old > 0:
            self.freq[old].remove(key)
            if not self.freq[old]:
                del self.freq[old]

        self.hm[key] = self.hm.get(key,0)+1
        value = self.hm[key]
        if value in self.freq:
            self.freq[value].append(key)
        else:
            self.freq[value] = [key]
        

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        old = self.hm[key]

        self.freq[old].remove(key)

        if not self.freq[old]:
            del self.freq[old]

        new = old - 1

        if new == 0:
            del self.hm[key]
        else:
            self.hm[key] = new

            if new not in self.freq:
                self.freq[new] = []

            self.freq[new].append(key)
        

    def getMaxKey(self):
        """
        :rtype: str
        """
        if not self.freq:
            return ""
        maxi = max(self.freq.keys())
        return self.freq[maxi][0]
        

    def getMinKey(self):
        """
        :rtype: str
        """
        if not self.freq:
            return ""
        mini = min(self.freq.keys())
        return self.freq[mini][0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()