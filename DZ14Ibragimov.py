seq = list(map(int, input().split()))
list(map(lambda x: print(x ** 2) if x % 2 == 1 else print(-x), range(seq[0], seq[1], seq[2])))