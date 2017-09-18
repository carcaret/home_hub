import collections

class Buffer:
    def __init__(self, size):
        self.buff = collections.deque([], maxlen=size)

    def put(self, l):
        for e in l:
            self.buff.append(e)

    def get(self):
        return list(self.buff)
