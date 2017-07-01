s = list(input())
k = int(input())
if len(s)<k:
    print(0)
    exit()
store = []
for i in range(len(s)):
    if s[i:i+k] not in store:
        store.append(s[i:i+k])
    if i+1+k > len(s):
        break
print(len(store))
