l = input().split()
list(map(lambda x: print(x**2) if x % 2 != 0 else print(-x), [x for x in range(int(l[0]), int(l[1]), int(l[2]))]))

