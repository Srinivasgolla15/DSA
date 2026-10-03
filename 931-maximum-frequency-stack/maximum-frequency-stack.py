class FreqStack(object):

    def __init__(self):
        self.count = {}
        self.freq = {}
        self.maxfreq = 0

    def push(self, val):
        old = self.count.get(val, 0)
        new = old + 1
        self.count[val] = new

        if new not in self.freq:
            self.freq[new] = []

        self.freq[new].append(val)

        if new > self.maxfreq:
            self.maxfreq = new

    def pop(self):
        val = self.freq[self.maxfreq].pop()

        self.count[val] -= 1

        if not self.freq[self.maxfreq]:
            self.maxfreq -= 1

        return val


# Time Complexity: O(1) average for push and pop
# Space Complexity: O(N)