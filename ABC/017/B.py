x = str(input())
x = list(x)
count = 0
for i in range(len(x)):
    if x[i] == 'c' and i+1 <= len(x) and x[i+1] == 'h':
        x[i+1] = 'o'
        count += 1
    elif x[i] == 'o' or x[i] == 'k' or x[i] == 'u':
        count += 1
if count == len(x):
    print('YES')
else:
    print('NO')
