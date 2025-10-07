def OptimalBST(p, q, n):
    E = [[0] * (n + 1) for _ in range(n + 1)]
    W = [[0] * (n + 1) for _ in range(n + 1)]
    R = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        E[i][i] = q[i]
        W[i][i] = q[i]
        R[i][i] = 0

    for d in range(1, n + 1):
        for i in range(n - d + 1):
            j = i + d
            E[i][j] = float('inf')
            W[i][j] = W[i][j - 1] + p[j - 1] + q[j]

            for k in range(i + 1, j + 1):
                cost = E[i][k - 1] + E[k][j] + W[i][j]
                if cost < E[i][j]:
                    E[i][j] = cost
                    R[i][j] = k

    return E, W, R


p = [0.1, 0.2, 0.4, 0.3]  
q = [0.05, 0.1, 0.05, 0.05, 0.1]  
n = 4

E, W, R = OptimalBST(p, q, n)

print("E matrix:")
for row in E:
    print(row)

print("\nW matrix:")
for row in W:
    print(row)

print("\nR matrix:")
for row in R:
    print(row)
