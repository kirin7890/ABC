n = int(input())
a = list(map(int, input().split()))
count = 0
while True:
    for i in range(n):
        if a[i] % 2 != 0:
            print(count)
            quit()
        else:
            a[i] = a[i] / 2
    count += 1
