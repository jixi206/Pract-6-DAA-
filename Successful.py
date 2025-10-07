p = [0.1, 0.2, 0.4, 0.3]
n = len(p)


c = [[0.0]*(n+1) for _ in range(n+1)]
r = [[0]*(n+1) for _ in range(n+1)]

prefix_sum = [0]*(n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + p[i]

def sum_p(i, j):
    
    return prefix_sum[j+1] - prefix_sum[i]

for i in range(n):
    c[i][i] = p[i]
    r[i][i] = i
    c[i][i-1] = 0  
c[n][n-1] = 0  

for length in range(2, n+1):  
    for i in range(n - length + 1):
        j = i + length - 1
        c[i][j] = float('inf')
        
        for k in range(i, j+1):
            cost = 0
            if k > i:
                cost += c[i][k-1]
            if k < j:
                cost += c[k+1][j]
            cost += sum_p(i, j)  
            if cost < c[i][j]:
                c[i][j] = cost
                r[i][j] = k

print("Cost table c:")
for row in c:
    print(row)

print("Root table r:")
for row in r:
    print(row)
