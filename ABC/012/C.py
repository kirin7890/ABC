n = int(input())

loss = 2025 - n
ans = []
count = 0
for i in range(9):
    i += 1
    for j in range(9):
        j += 1
        if i * j == loss:
            ans.append([i, j])

for i in range(len(ans)):
    print(str(ans[i][0]) + " x " + str(ans[i][1]))