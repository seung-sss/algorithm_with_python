from collections import deque
enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]

def visiting(enter, leave):
    rel = dict()
    visit = []
    queue = deque(leave)

    for val in sorted(enter):
        rel[val] = 0

    for val in enter:
        if queue[0] == val:
            visit.append(val)
            while len(queue) != 0 and queue[0] in visit:
                visit.remove(queue[0])
                queue.popleft()

        else:
            for i in range(len(enter)):
                if queue[i] != val:
                    rel[val] += 1
                    rel[queue[i]] += 1
                else:
                    visit.append(val)
                    break

    return list(rel.values())

print(visiting(enter, leave))