a, b = map(int,input().split())
c = False
if (a >= b):
    for i in range(b, a + 1):
        if (1920 % i == 0) and (2880 % i == 0):
            c = True
            break
else:
    for i in range(a, b + 1):
        if (1920 % i == 0) and (2880 % i == 0):
            c = True
            break
if c == True:
    print(1)
else:
    print(0)