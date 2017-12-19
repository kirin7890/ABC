w, h, n = map(int, input().split())
x1, y1, x2, y2 = 0, 0, w, h
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 :
        x1 = max(x, x1)
    elif a == 2:
        x2 = min(x, x2)
    elif a == 3:
        y1 = max(y, y1)
    else:
        y2 = min(y, y2)
print(max((x2-x1), 0) * max((y2-y1), 0))
