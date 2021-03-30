import sys

class Queue:
    def __init__(self):
        self.que = []

    def push(self, num):
        self.que.append(num)

    def pop(self):
        if not self.que:
            return -1
        tmp = self.que[0]
        self.que = self.que[1:]

        return tmp

    def size(self):
        return len(self.que)

    def empty(self):
        return 1 if not self.que else 0

    def front(self):
        if not self.que:
            return -1

        return self.que[0]

    def back(self):
        if not self.que:
            return -1

        return self.que[-1]

n = int(sys.stdin.readline())
que = Queue()

for _ in range(n):
    inp = sys.stdin.readline().split()
    ins = inp[0]

    if ins == 'push':
        que.push(int(inp[1]))
    elif ins == 'pop':
        print(que.pop())
    elif ins == 'size':
        print(que.size())
    elif ins == 'empty':
        print(que.empty())
    elif ins == 'front':
        print(que.front())
    elif ins == 'back':
        print(que.back())