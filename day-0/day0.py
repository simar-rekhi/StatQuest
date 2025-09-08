import math

X = list(map(int, input().split()))
N = len(X)

print('mean: ', round(sum(X)/N, 1))

X = sorted(X)
if N % 2 == 0:
    print('median: ',X[int(N/2)], X[int(N/2)+1])
else:
    print('median: ',X[int((N+1)/2)])

print('mode: ', max(X))
