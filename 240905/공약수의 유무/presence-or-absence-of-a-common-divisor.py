a, b = map(int,input().split())
chk1 = 1920
chk2 = 2880
cnt = 0
while True:
    for i in range(a, b + 1):
        if (chk1 % i == 0) or (chk1 % i == 0) or ((chk1 % i == 0) and (chk1 % i == 0)):
            cnt += 1
        elif (chk2 % i == 0) or (chk2 % i == 0) or ((chk2 % i == 0) and (chk2 % i == 0)):
            cnt += 1
    if (cnt != 0):
        print(1)
        break
    else:
        print(0)
        break