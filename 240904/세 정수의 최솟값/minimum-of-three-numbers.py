a = list(map(int, input().split()))
min = a[0]
for i in range(len(a)):
    if (a[i] < min):
        min = a[i]
print(min)