import numpy as np
def gauss_seidel(A, b, x0, max_iter=100, tol=0.001):
    n = len(A)
    x = x0.copy()

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        if all(abs(np.dot(A, x) - b) < tol):
            return x

    return x

A = [[9,1, 1], [1,9,1],[1,1,9]]
B = [11,11,11]
x0 = [0,0,0]

solution = gauss_seidel(A,B,x0)
print('gaus_seidle ',solution)