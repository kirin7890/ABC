s = list(str(input()))
cl = []
for i in set(s):
    tar = i
    temp = s[:]
    count = 0
    while len(set(temp)) != 1:
        for j in range(len(temp)):
            if j < len(temp)-1:
                if temp[j + 1] == tar:
                    temp[j] = tar
            else:
                temp.pop()
        count += 1
    cl.append(count)
print(min(cl))
