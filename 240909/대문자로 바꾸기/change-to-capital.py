for _ in range(5):
    row = input().split()
    row_upper = [char.upper() for char in row]
    print(" ".join(row_upper))