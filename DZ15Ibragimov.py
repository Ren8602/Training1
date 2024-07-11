n = int(input())

def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    return (fibonachi(n-1) + fibonachi(n-2))

print(fibonachi(n))