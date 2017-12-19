n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
for i in range(n - m + 1):
    for j in range(len(a[0]) - len(b[0]) + 1):
        for k in range(m):
            # print()
            # print(a[i+k][j:(j+m)])
            # print(b[k])

            if a[i+k][j:(j+m)] != b[k]:
                # print('break')
                break
            # else:
                # print('pass')
            if k == m-1:
                print('Yes')
                quit()
print('No')
