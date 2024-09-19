h, w = map(int, input().split())
b = (w * 10000) / h ** 2
print(f"%d" % b)
if b >= 25:
    print("Obesity")