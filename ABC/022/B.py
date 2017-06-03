n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a_num = len(a)
a_uni = len(set(a))
print(a_num - a_uni)
