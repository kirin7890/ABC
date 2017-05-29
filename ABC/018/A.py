abc = []
for i in range(3):
    abc.append(int(input()))

temp = sorted(abc, reverse=True)
for i in abc:
    print(temp.index(i)+1)
