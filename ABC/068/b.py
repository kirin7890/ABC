n = int(input())
num = 1
while True:
    if num*2 > n:
        print(num)
        break
    elif num*2 == n:
        print(num*2)
        break
    else:
        num *= 2
