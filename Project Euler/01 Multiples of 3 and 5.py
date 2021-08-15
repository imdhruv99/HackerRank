def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2
  
def eulerFunc(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(eulerFunc(N - 1))