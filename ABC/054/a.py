a, b = map(int, input().split())
def change(x):
    if x == 1:
        return 14
    else:
        return x

a = change(a)
b = change(b)
if a > b:
    print('Alice')
elif a < b:
    print('Bob')
else:
    print('Draw')
