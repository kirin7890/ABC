l, h = map(int, input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if a > h:
        print(-1)
    elif a < l:
        print(abs(a-l))
    else:
        print(0)