a, b, k, l = map(int, input().split())
ans = []
ans.append(((k//l)+1)*b)
ans.append(k*a)
ans.append((k//l)*b+(k%l)*a)
print(min(ans))