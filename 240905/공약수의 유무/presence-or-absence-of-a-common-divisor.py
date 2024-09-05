a, b = map(int,input().split())
cnt = 0
while True:
    for i in range(2, 1920):
        if (1920 % i == 0) or (2880 % i == 0) or ((1920 % i == 0) and (2880 % i == 0)):
            cnt += 1
    if cnt:
        print(1)
        break
    else:
        print(0)
        break