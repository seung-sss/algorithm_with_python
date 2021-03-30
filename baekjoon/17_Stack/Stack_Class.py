# stack class 정의

class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        tmp = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return tmp

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return self.list[-1] if self.size != 0 else -1
