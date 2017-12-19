n = int(input())
s = input()
ans = [0]
for i in range(n):
    if s[i] == 'I':
        ans.append(ans[-1] + 1)
    else:
        ans.append(ans[-1] - 1)
print(max(ans))
