a = list(map(int, input().split()))
if (a[0] > a[1]):
    print(a[0] * a[1])
elif(a[0] < a[1]):
    print(a[1] // a[0])