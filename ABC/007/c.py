R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = []
for i in range(R):
    c.append(list(input()))
queue = [[sy - 1, sx - 1, 0]]

def move(yxc):
    y, x, cost = yxc[0], yxc[1], yxc[2]
    global queue
    for dy, dx in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        ny, nx = y + dy, x + dx
        if c[ny][nx] == '.':
            c[ny][nx] = cost + 1
            queue.append([ny, nx, cost + 1])

c[sy-1][sx-1] = 0
while len(queue) > 0:
    move(queue.pop(0))

print(c[gy-1][gx-1])
