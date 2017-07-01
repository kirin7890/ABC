from collections import deque

n = int(input())
b = deque()
flag = 1
for i in input().split():
    if flag > 0:
        b.append(i)
    else:
        b.appendleft(i)
    flag *= -1
if flag < 0:
    b.reverse()
print(' '.join(b))
